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
        
        #edit staff tree buttons
        self.frame.add_staff_btn.config(command=self.add_staff_pop)
        self.frame.remove_staff_btn.config(command=self.remove_staff_pop)
        self.frame.edit_staff_btn.config(command=self.edit_staff_pop)


    # button functions
    def staff_edit(self):
        print("staff edit button clicked")

    def menu_edit(self):
        print("menu edit button clicked")
        self.clear_edit_staff()
        employeeList = self.model.admin.get_employee_list()
        print(employeeList)
        self.frame.mid_frame = self.frame.edit_staff_table(data = employeeList)

    def home_btn(self) -> None:
        print("home button clicked")
        self.view.switch("home")
        
    def add_staff_pop(self) -> None:
        self.frame.add_staff_pop()
        print("button pressed")
    
    def remove_staff_pop(self) -> None:
        print("button")
        
    def edit_staff_pop(self) -> None:
        print("bttons pressed")
    
    
    
    #update view
    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        self.clear_edit_staff()
        if current_user:
            self.frame.username.config(text=f" User: {current_user.getName()} ")
            self.frame.user_id.config(text=f" ID: {current_user.getStaffId()} ")
            employeeList = self.model.admin.get_employee_list()
            self.frame.mid_frame = self.frame.edit_staff_table(data = employeeList)
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
            
    def clear_edit_staff(self):
        for widgit in self.frame.mid_frame.winfo_children():
            widgit.destroy()