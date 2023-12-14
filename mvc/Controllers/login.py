from Models.main import Model
from Models.auth import User
from Views.main import View
from database import dbfunc
from passlib.hash import sha256_crypt


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
        staffId = self.frame.staffId_entry.get()
        password = self.frame.password_entry.get()
        data = {"username": staffId, "password": password}
        print(data)
        #temp spot for login verification code uncomment below if you want it to run normally and then comment out all the try stuff
        self.frame.password_entry.delete(0, last=len(password))
        user: User = {"username": data["username"]}
        self.model.auth.login(user)
        # try:	          
        #     print('login start 1.1')
        #     if staffId != None and password != None:  #check if em or pw is none          
        #         conn = dbfunc.getConnection() 
        #         print('login 1.2')
        #         if conn != None:    #Checking if connection is None
        #             print('login 1.3')                    
        #             if conn.is_connected(): #Checking if connection is established                        
        #                 print('MySQL Connection is established')                          
        #                 dbcursor = conn.cursor()    #Creating cursor object                                                 
        #                 dbcursor.execute("SELECT employee_password, employee_name, employee_account_type \
        #                     FROM employee WHERE employee_id = %s;", (staffId,))                                                
        #                 data = dbcursor.fetchone()
        #                 print(data[0])
        #                 if dbcursor.rowcount < 1: #this mean no user exists                         
        #                     error = "Email / password does not exist, login again"
        #                     #DISPLAY ERROR MESSAGE
        #                 else:                            
        #                     #data = dbcursor.fetchone()[0] #extracting password   
        #                     # verify passowrd hash and password received from user                                                             
        #                     if (password == data[0]):
        #                         dbcursor.close()
        #                         conn.close()
        #                         #call employee class here and place in name, id and account type (alex)                       
        #                         print("You are now logged in")                                
        #                         #REDIRECT TO ACCOUNT PAGE
                                
        #                         self.frame.password_entry.delete(0, last=len(password))
                                
        #                         user: User = {"username": data["username"]}
               
        #                         self.model.auth.login(user)
        #                     else:
        #                         error = "Invalid credentials username/password, try again."
        #                         dbcursor.close()
        #                         conn.close()

        #             #RETURN WITH ERROR
        #             print(error)
        # except Exception as e:                
        #     error = str(e) + " <br/> Invalid credentials, try again."
        #     #RETURN INVALID 
        #     print(error)

        #RETURN NO ERROR
       
