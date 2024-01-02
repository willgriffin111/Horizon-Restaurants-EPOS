'''
Author: Alex Rogers
Date: 18/12/2023
Version: 1.0
'''

from Models.main_m import Model
from Views.main_v import View
from tkinter import messagebox

class AccountController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["account"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_btn.config(command=self.home_btn)
        self.frame.editname_btn.config(command=self.update_account_pop)
        self.frame.editpassword_btn.config(command=self.change_pass_pop)
        self.frame.log_off.config(command=self.logoff)
    

    #name update
    def update_account_pop(self):
        self.frame.update_account_pop()
        self.frame.submit_name_btn.config(command=self.name_update)
    
    def name_update(self):
        self.model.account.updateName(self.frame.name_box.get(), self.model.auth.current_user)
        self.frame.staff_window.destroy()
        print("updateing name")
        

    #password update
    def change_pass_pop(self):
        self.frame.change_pass_pop()
        self.frame.submit_password_btn.config(command=self.password_update)
    
    def password_update(self):
        self.model.account.updatePassword(self.frame.new_password_box.get(),self.frame.re_password_box.get(), self.model.auth.current_user)
        self.frame.staff_window.destroy()
        print("updateing password")

    #home tab
    def home_btn(self) -> None:
        self.view.switch("home")
        print("going home")
     
    def logoff(self) -> None:
        print("log off")
        self.model.auth.logout()
    
    #update view
    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.staff_name.config(text=f"Hey, {current_user.getName()} ")
            self.frame.staff_id.config(text=f"ID: {current_user.getStaffId()} ")
            self.frame.staff_role.config(text=f"Role: {current_user.getAccountType()} ")
            self.frame.staff_location.config(text=f"Store ID: {current_user.getRestrantID()} ")
        else:
            self.frame.staff_name.config(text=f"Hey, Name ")
            self.frame.staff_id.config(text=f"ID: 12345678 ")
            
