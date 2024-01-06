"""
File name: order_c.py
Author: Shahbaz
Date created: 17/12/2023
"""
from tkinter import messagebox

from Models.main_m import Model
from Views.main_v import View

class OrderController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["order"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.homeButton.config(command=self.home)
        self.frame.modify.config(command=self.modify)
        self.frame.pay_button.config(command=self.pay)

    def update_categories(self):
        self.restaurant_ID = self.model.auth.current_user.getRestrantID()
        self.menu = self.model.menu.get_menu(self.restaurant_ID)
        print(self.menu)
        self.frame.create_menu_categories(self.menu) # running this view function again to load it with the updated category list
    
    def update_view(self):
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f"User: {current_user.getName()}")
            self.frame.user_id.config(text=f"ID: {current_user.getStaffId()}")
            self.update_categories()
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")

    def home(self) -> None:
        # Clear the order variable in the view and model, then update the view
        self.model.order.clear_order()
        self.frame.setOrder({})
        self.frame.updateOrderSummary()
        self.view.switch("home")
    
    def modify(self):
        self.order = self.frame.order
        self.model.order.saveOrder(self.order)
        self.view.switch("order-modify")
    
    def updateOrder(self):
        self.order = self.model.order.getSavedOrder()
        self.frame.setOrder(self.order)
        self.frame.updateOrderSummary()


    def pay(self):
        """
        Get the order
        If table is selected or order is not empty
            pass it to the model to insert into db
        else send an error messagebox

        ez and thats done
        """
        # Get data from view
        self.selected_table = self.frame.selected_table.get()
        self.order = self.frame.order
        self.author = self.model.auth.current_user.getStaffId()  
        self.sub_total = self.frame.discounted_price
        self.discount_applied = self.frame.total_discount / 100
        # Error checking, table has to be selected and order cant be empty
        if self.selected_table == 'Select Table':
            messagebox.showerror("Error", "Select a table.")
        elif len(self.order) < 1: 
            messagebox.showerror("Error", "Order cannot be left empty.")
        else:
            print(f'table: {self.selected_table}\norder: {self.order}')
            restaurant_ID = self.model.auth.current_user.getRestrantID()
            if self.model.order.create_order(restaurant_ID,self.order, self.selected_table, self.author, self.sub_total, self.discount_applied):
                messagebox.showinfo("Success", "Order has been created!")
                # Clear the order variable in the view and model, then update the view
                self.model.order.clear_order()
                self.frame.setOrder({})
                self.frame.updateOrderSummary()
            elif 'Table value selected has no number':
                messagebox.showerror("Error", "Table value selected has no number.")
            else:
                messagebox.showerror("Error", "Database error, there's nothing we can do... *becomes Napolean 2.0* ")
        
        
        
