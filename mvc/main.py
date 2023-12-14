from Models.main import Model
from Views.main import View
from Controllers.main import Controller


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == "__main__":
    main()


#dw about this i just all the code i oringinally wrote while testing but i need some of it later.

# import tkinter as tk
# from GUI.login import LoginFrame
# from GUI.kitchenStaff import KitchenFrame
# from database import dbfunc


# class MainApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("800x600")  
#         self.title('Horizon Restaurant')
#         self.configure(bg='#2976E9')  
#         self.show_login()

#     def show_login(self):
#         self.login_frame = LoginFrame(self)  # Create an instance of LoginFrame
#         self.login_frame.pack(fill=tk.BOTH, expand=True)
#         self.login_frame.set_login_callback(self.perform_login)

#     def perform_login(self, staffId, password):
#         self.login_frame.destroy()
#         self.show_kitchen()
        
#     def perform_logi(self, staffId, password):
#         # Your login logic from main.py
#         try:	          
#                 print('login start 1.1')
#                 if staffId != None and password != None:  #check if em or pw is none          
#                     conn = dbfunc.getConnection() 
#                     if conn != None:    #Checking if connection is None                    
#                         if conn.is_connected(): #Checking if connection is established                        
#                             print('MySQL Connection is established')                          
#                             dbcursor = conn.cursor()    #Creating cursor object                                                 
#                             dbcursor.execute("SELECT employee_password, employee_name, employee_account_type \
#                                 FROM employee WHERE employee_id = %s;", (staffId,))                                                
#                             data = dbcursor.fetchone()
#                             #print(data[0])
#                             if dbcursor.rowcount < 1: #this mean no user exists                         
#                                 error = "Email / password does not exist, login again"
#                                 #DISPLAY ERROR MESSAGE
#                             else:                            
#                                 #data = dbcursor.fetchone()[0] #extracting password   
#                                 # verify passowrd hash and password received from user                                                             
#                                 if sha256_crypt.verify(password, str(data[0])):
#                                     dbcursor.close()
#                                     conn.close()
#                                     #call employee class here and place in name, id and account type (alex)                       
#                                     print("You are now logged in")                                
#                                     #REDIRECT TO ACCOUNT PAGE
#                                     self.login_frame.destroy()
#                                     self.show_kitchen()
#                                 else:
#                                     error = "Invalid credentials username/password, try again."
#                                     dbcursor.close()
#                                     conn.close()
#                         print('login start 1.10')
#                         #RETURN WITH ERROR
#         except Exception as e:                
#             error = str(e) + " <br/> Invalid credentials, try again."
#             #RETURN INVALID   

#         #RETURN NO ERROR

#         # For example, after successful login, destroy the login screen and open the kitchen screen

#     def show_kitchen(self):
#         self.kitchen_frame = KitchenFrame(self)
#         self.kitchen_frame.pack(fill=tk.BOTH, expand=True)

# if __name__ == "__main__":
#     app = MainApp()
#     app.mainloop()




