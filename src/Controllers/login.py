# from Models.main import Model
# from Views.main import View
# from database import dbfunc
# from passlib.hash import sha256_crypt
# from Class.EmployeeClass import EmployeeAccount


# class LoginController:
#     def __init__(self, model: Model, view: View) -> None:
#         self.model = model
#         self.view = view
#         self.frame = self.view.frames["login"]
#         self._bind()

#     def _bind(self) -> None:
#         """Binds controller functions with respective buttons in the view"""
#         self.frame.login_btn.config(command=self.login)

#     def login(self) -> None:
#         staffId = self.frame.staffId_entry.get() #getting staffID
#         password = self.frame.password_entry.get() # getting Password
#         error = "" #reseting error   
#         print('login start 1.1')
#         if staffId != None and password != None:  #check if em or pw is none          
#             conn = dbfunc.getConnection() 
#             if conn != None:    #Checking if connection is None                  
#                 if conn.is_connected(): #Checking if connection is established                        
#                     print('MySQL Connection is established')                          
#                     dbcursor = conn.cursor()    #Creating cursor object                                                 
#                     dbcursor.execute("SELECT employee_password, employee_name, employee_account_type \
#                         FROM employee WHERE employee_id = %s;", (staffId,))                                                
#                     staffdata = dbcursor.fetchone()
#                     if dbcursor.rowcount < 1: #this mean no user exists                         
#                         error = "Staff ID / password does not exist, login again"
#                         #DISPLAY ERROR MESSAGE
#                     else:                            
#                         #data = dbcursor.fetchone()[0] #extracting password   
#                         # verify passowrd hash and password received from user                                                             
#                         if sha256_crypt.verify(password, str(staffdata[0])):
#                             dbcursor.close()
#                             conn.close()
#                             #Creates employee class with id name and account type all stored 
#                             employee = EmployeeAccount(staffId,staffdata[1],staffdata[2])                   
#                             print("You are now logged in")                                
#                             #REDIRECT TO ACCOUNT PAGE
#                             #clears password from frame so its not there when logining out
#                             self.frame.password_entry.delete(0, last=len(password))
#                             password = '' # clears password vairable
#                             self.model.auth.login(employee) #changes account type to logged in and passes employee class
#                         else:
#                             error = "Invalid credentials username/password, try again."
#                             dbcursor.close()
#                             conn.close()
#         if(error != ""):
#             print(error)

from Models.main import Model
from Views.main import View

class LoginController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["login"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.login_btn.config(command=self.login)

    def login(self) -> None:
        staffId = self.frame.staffId_entry.get() #getting staffID
        password = self.frame.password_entry.get() # getting Password
        self.frame.password_entry.delete(0, last=len(password))
        self.model.auth.login(staffId,password)
