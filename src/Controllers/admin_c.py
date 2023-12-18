'''
Author: Alex Rogers
Date: 18/12/2023
Version: 1.0
'''

from Models.main_m import Model
from Views.main_v import View

class AdminController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["admin"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_btn.config(command=self.home_btn)
        self.frame.staff_edit_btn.config(command=self.staff_edit)
        self.frame.menu_edit_btn.config(command=self.menu_edit)


    # button functions
    def staff_edit(self):
        print("staff edit button clicked")

    def menu_edit(self):
        print("menu edit button clicked")

    def home_btn(self) -> None:
        print("home button clicked")
        self.view.switch("home")
    
    #update view
    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f" User: {current_user.getName()} ")
            self.frame.user_id.config(text=f" ID: {current_user.getStaffId()} ")
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")