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
        self.frame.pay_button.config(command=self.pay_popup)

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
    
    def pay_popup(self):
        # Error checking, table has to be selected and order cant be empty
        self.selected_table = self.frame.selected_table.get()
        self.order = self.frame.order
        if self.selected_table == 'Select Table':
            messagebox.showerror("Error", "Select a table.")
        elif len(self.order) < 1: 
            messagebox.showerror("Error", "Order cannot be left empty.")
        # If everythings fine proceed with payment bro bro
        else:
            self.confirm_pay = messagebox.askquestion("Payment", "Enter payment details..")
            if self.confirm_pay == 'yes':
                self.pay()
            else:
                messagebox.showinfo("Payment Cancelled", "Payment was cancelled..")


    def pay(self):
        """
        Get the order
        If table is selected or order is not empty
            pass it to the model to insert into db
        else send an error messagebox

        ez and thats done
        """
        # Get data from view
        self.order = self.frame.order
        self.author = self.model.auth.current_user.getStaffId()  
        self.sub_total = self.frame.discounted_price
        self.discount_applied = self.frame.total_discount / 100
        
        
        print(f'table: {self.selected_table}\norder: {self.order}')
        restaurant_ID = self.model.auth.current_user.getRestrantID()
        self.message = self.model.order.create_order(restaurant_ID,self.order, self.selected_table, self.author, self.sub_total, self.discount_applied)

        # ok now this one is a little tough to explain but here goes, 
        # so the first if statement is checking for a dictionary returned called items_out_of_stock, now its important to check if its more than 0 cause that means some menu items could not be part of the order cause stock ran out
        # the other two are self explanatory..
        if isinstance(self.message, dict) and len(self.message) > 0:
            message = "The following items are out of stock or partially deducted:\n"
            for item_name, item_info in self.message.items():
                quantity = item_info['quantity']
                price = item_info['price']
                message += f"{quantity} units of {item_name} at £{price} each.\n"
            
            messagebox.showwarning("Items not fully deducted from stock.", message)
            
        elif self.message == 'Table value selected has no number':
            messagebox.showerror("Error", "Table value selected has no number.")
        elif self.message == 'DB Error':
            messagebox.showerror("Error", "Database error, there's nothing we can do... *becomes Napolean 2.0* ")
        else:
            # Order created successfully
            messagebox.showinfo("Success", "Order has been created!")
            messagebox.showinfo("Inventory Update.", "All items successfully deducted from inventory.")
            # Clear the order variable in the view and model, then update the view
            # self.model.order.clear_order()
            # self.frame.setOrder({})
            # self.frame.updateOrderSummary()
    
    
    
