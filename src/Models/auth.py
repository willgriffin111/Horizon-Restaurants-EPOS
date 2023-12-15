from typing import TypedDict, Union
from .base import ObservableModel
from passlib.hash import sha256_crypt
from Class.EmployeeClass import EmployeeAccount
from database import dbfunc



class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.current_user = None

    def login(self, staffId, password) -> None:
        error = "" #reseting error   
        print('login start 1.1')
        if staffId != None and password != None:  #check if em or pw is none          
            conn = dbfunc.getConnection() 
            if conn != None:    #Checking if connection is None                  
                if conn.is_connected(): #Checking if connection is established                        
                    print('MySQL Connection is established')                          
                    dbcursor = conn.cursor()    #Creating cursor object                                                 
                    dbcursor.execute("SELECT employee_password, employee_name, employee_account_type \
                        FROM employee WHERE employee_id = %s;", (staffId,))                                                
                    staffdata = dbcursor.fetchone()
                    if dbcursor.rowcount < 1: #this mean no user exists                         
                        error = "Staff ID / password does not exist, login again"
                        #DISPLAY ERROR MESSAGE
                    else:                            
                        #data = dbcursor.fetchone()[0] #extracting password   
                        # verify passowrd hash and password received from user                                                             
                        if sha256_crypt.verify(password, str(staffdata[0])):
                            dbcursor.close()
                            conn.close()
                            #Creates employee class with id name and account type all stored 
                            employee = EmployeeAccount(staffId,staffdata[1],staffdata[2])                   
                            print("You are now logged in")                                
                            #REDIRECT TO ACCOUNT PAGE
                            #clears password from frame so its not there when logining out
                            password = '' # clears password vairable
                            #changes account type to logged in and passes employee class
                            self.is_logged_in = True
                            self.current_user = employee #takes employee class with all stored info 
                            self.trigger_event("auth_changed")
                        else:
                            error = "Invalid credentials username/password, try again."
                            dbcursor.close()
                            conn.close()
        if(error != ""):
            print(error)


    def logout(self) -> None:
        self.is_logged_in = False
        self.current_user = None
        self.trigger_event("auth_changed")