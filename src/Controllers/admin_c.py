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
        
        #pop out buttons


    # button functions
    def staff_edit(self):
        print("staff edit button clicked")

    def menu_edit(self):
        print("menu edit button clicked")

    def home_btn(self) -> None:
        self.view.switch("home")
        
    def add_staff_pop(self) -> None:
        self.frame.add_staff_pop()
        self.frame.add_submit_btn.config(command=self.add_staff)
        
    def add_staff(self):
        self.model.admin.add_new_staff(self.frame.name_box.get(),self.frame.role_box.get(),self.frame.password_box.get())
        self.frame.add_staff_window.destroy()
        self.frame.clear_table()
        self.frame.insert_data(data = self.model.admin.get_employee_list())
        print("pressed")
    
    def remove_staff_pop(self) -> None:
        self.frame.remove_staff_pop()
        self.frame.remove_submit_btn.config(command=self.remove_staff)
        
    def remove_staff(self) -> None:
        self.model.admin.remove_staff(self.frame.id_entry.get())
        self.frame.remove_staff_window.destroy()
        self.frame.clear_table()
        self.frame.insert_data(data = self.model.admin.get_employee_list())
        
    def edit_staff_pop(self) -> None:
        print("bttons pressed")
    
    
    
    #update view
    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        self.frame.clear_table()
        if current_user:
            self.frame.username.config(text=f" User: {current_user.getName()} ")
            self.frame.user_id.config(text=f" ID: {current_user.getStaffId()} ")
            self.frame.insert_data(data = self.model.admin.get_employee_list())
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
            
    def clear_edit_staff(self):
        for widgit in self.frame.mid_frame.winfo_children():
            widgit.destroy()