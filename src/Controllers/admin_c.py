'''
Author: Alex Rogers
Date: 18/12/2023
Version: 1.0
'''

from Models.main_m import Model
from Views.main_v import View
from tkinter import messagebox

class AdminController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["admin"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_btn.config(command=self.home_btn)
        self.frame.staff_edit_side.config(command=self.staff_edit)
        self.frame.menu_edit_side.config(command=self.menu_edit)
    
        
        #edit staff tree buttons
        
        # self.saveButton = tk.Button(self.editWindow, text="Save", command=lambda: self.saveNewValue(tree, row_id, self.column_index, self.newValueUI.get(), self.editWindow))
        
        # self.add_inventory = tk.Button(self.inventory_frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5,command=self.add_inventory_pop)
       

        # self.remove_inventory = tk.Button(self.inventory_frame, text='Delete', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        
        
        #pop out buttons


    #staff tab
    def staff_edit(self):
        self.frame.staff_edit()
        self.frame.staff_tree.bind("<Double-1>", self.frame.onDoubleClickStaff)
        self.frame.add_staff_btn.config(command=self.add_staff_pop)
        self.frame.remove_staff_btn.config(command=self.remove_staff)
        

    #menu tab
    def menu_edit(self):
        self.frame.menu_edit()

    #home tab
    def home_btn(self) -> None:
        self.view.switch("home")
     
    #add staff   
    def add_staff_pop(self) -> None:
        self.frame.add_staff_pop(self.model.reservation.getRestaurantNames())
        self.frame.add_submit.config(command=self.add_staff)
        
    def add_staff(self):
        self.model.admin.add_new_staff(self.frame.name_box.get(),self.frame.role_box.get(),self.frame.password_box.get(),self.frame.chosen_restaurant_option.get())
        self.frame.staff_window.destroy()
        self.clear_edit_staff()
    
        
    #remove staff   
    def remove_staff(self):
        self.selectedItem = self.frame.staff_tree.selection() 
        if self.selectedItem:
            self.selectedStaffId = self.frame.staff_tree.item(self.selectedItem)['values'][0]  
            self.model.admin.remove_staff(self.selectedStaffId)
            self.clear_edit_staff()
        else:
            messagebox.showerror("Error", "No item selected")
        

        
    #edit staff
    def onDoubleClickStaff(self, event):
        self.rowId = self.frame.staff_tree.identify_row(event.y)
        self.columnId = self.frame.staff_tree.identify_column(event.x)
        if self.rowId and self.columnId:
            self.frame.editWindowPopup(self.frame.staff_tree, self.rowId, self.columnId)
        
        
        
    
    
    
    
    #update view
    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f" User: {current_user.getName()} ")
            self.frame.user_id.config(text=f" ID: {current_user.getStaffId()} ")
            self.clear_edit_staff()
            self.staff_edit()
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
            
    def clear_edit_staff(self):
        self.frame.clear_staff_table()
        self.frame.insert_data_staff(data = self.model.admin.get_employee_list())