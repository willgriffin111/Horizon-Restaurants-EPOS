"""
Author: Shahbaz Bokhari
File name: discount_c.py
Date: 07/01/2023
"""

from tkinter import messagebox
from datetime import datetime

from Models.main_m import Model
from Views.main_v import View

class DiscountController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["discount"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_button.config(command=self.home)
        self.frame.refresh_button.config(command=self.refresh_tree_view)
        self.frame.add_discount_button.config(command=self.create_discount_popup)
        self.frame.remove_discount_button.config(command=self.remove_discount)
        self.frame.discount_tree.bind("<Double-1>", self.on_double_click)
    
    def home(self):
        self.view.switch("home")

    def update_view(self) -> None:     # updates the username, userid and the latest discount data on log in
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f"User: {current_user.getName()}")
            self.frame.user_id.config(text=f"ID: {current_user.getStaffId()}")
            self.refresh_tree_view()
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
    
    def refresh_tree_view(self):
        # Update the discounts table with the discount data from the database
        self.frame.clear_tree_view()
        self.restaurant_ID = self.model.auth.current_user.getRestrantID()
        self.discounts = self.model.discount.get_discounts(self.restaurant_ID)
        self.frame.insert_tree_view(self.discounts)
    
    def create_discount_popup(self):
        # Get values for new item to be added
        self.name_value = self.frame.discount_name_entry_field.get()
        self.value_percentage = self.frame.discount_value_entry_field.get()
        self.start_date = self.frame.start_date_entry.get()
        self.end_date = self.frame.end_date_entry.get()

        print(self.start_date)

        # Check if data is missing
        if not all([self.name_value, self.value_percentage, self.start_date, self.end_date]):
            messagebox.showerror("Error", "All fields are required")
            return
        else:
            # Check if end date is after or the same as start date
            if self.is_end_date_valid(self.start_date, self.end_date):
                self.create_discount()
            else:
                messagebox.showerror("Error", "End date cannot be before start date")

    def is_end_date_valid(self, start_date, end_date):
        # Convert strings to datetime objects for comparison, this took me a while to figure out, thankyou indian guy on youtube
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

        # Check if end date is after or the same as the start date 
        return end_date_obj >= start_date_obj
        
    def create_discount(self):
        result = messagebox.askokcancel("Add Discount", "Do you want to add this discount?")
        if result:
            # Insert new discount info to db
            self.restaurant_ID = self.model.auth.current_user.getRestrantID()
            completion_message = self.model.discount.create_discount(self.restaurant_ID, self.name_value, self.value_percentage, self.start_date, self.end_date)
            if completion_message == "Name already exists":
                messagebox.showerror("Error", "Discount name already exists!")
                return
            elif completion_message == "Discount created":
                self.refresh_tree_view()
                messagebox.showinfo("Success", "Discount created!")


    def remove_discount(self):  # deletes discount selected from the db and updates view
        # Use the selected discount's id to remove it from the db, after confirmation (messagebox)
        self.selected_discount = self.frame.discount_tree.selection()
        if self.selected_discount:
            self.confirmation = messagebox.askquestion("Delete Discount", "Are you sure you want to remove this discount?")
            if self.confirmation == 'yes':
                self.selected_discount_id = self.frame.discount_tree.item(self.selected_discount)['values'][0]
                self.restaurant_ID = self.model.auth.current_user.getRestrantID()
                self.remove_message = self.model.discount.remove_discount(self.restaurant_ID, self.selected_discount_id)
                # just some error messages that won't ever show up in the demo but doing it anyways, cause its funny? ...this projects made my humour stoop real low
                if self.remove_message == "Discount not found":
                    messagebox.showerror("L Error", "Congrats you got a really rare error, just refresh the page you muppet") # now im even making a messagebox for it... *sigh.. *DEEEP SSIIIIGGHHHHHHHHHHHHHhhhhhhhhhh..........
                elif self.remove_message == "DB Error":
                    messagebox.showerror("DB Error", "DB Error, yea I can't help you with this one bud")

                # Update the tree view
                self.refresh_tree_view()

    def on_double_click(self, event):
        self.row_ID = self.frame.discount_tree.identify_row(event.y)       # self explanatory, gets the row and column id's based on what value in the tree-view you double clicked
        self.column_ID = self.frame.discount_tree.identify_column(event.x)
        if self.row_ID and self.column_ID:
            #print(f"row: {self.row_ID}, col: {self.column_ID}")
            if self.column_ID != "#1":  # Checking if they haven't clicked on the inventory_id cause we are NOT letting you edit that buddy. Editing the id is a big no-no
                # Bring up a window where they can edit the value then update the db and view, also just ask for confirmation (messagebox in update_discount)
                # Make the entry box a date picker if they click on start or end dates otherise just make it normal text entry
                if self.column_ID in ["#3", "#4"]:
                    self.frame.date_edit_window_popup(self.row_ID, self.column_ID)
                else:
                    self.frame.edit_window_popup(self.row_ID, self.column_ID)
                self.frame.save_changes_button.config(command=lambda row_id=self.row_ID, col_id=self.column_ID: self.update_discount(row_id, col_id))
                

        
    def update_discount(self, row_ID, col_id):
        self.click_confirm = messagebox.askquestion("Edit Discount", "Are you sure you want to edit the discount info?")
        if self.click_confirm == 'yes':
            # Get values from view
            new_value = self.frame.new_value_entry.get()
            column_index = self.frame.column_index
            discount_ID = self.frame.discount_tree.item(row_ID, 'values')[0]
            restaurant_ID = self.model.auth.current_user.getRestrantID()

            if col_id == "#3":  #  column_index 3 corresponds to the start date
                # Compare the new_value with the end date from the treeview
                print("3")
                start_date = new_value
                end_date = self.frame.discount_tree.item(row_ID, 'values')[3]
                if not self.is_end_date_valid(start_date, end_date):
                    messagebox.showerror("Invalid Dates", "End date must be after or the same as start date.")
                    return
            elif col_id == "#4":  #  column_index 4 corresponds to the end date
                print("4")
                # Compare the new_value with the start date from the tree view
                start_date = self.frame.discount_tree.item(row_ID, 'values')[2]
                end_date = new_value
                if not self.is_end_date_valid(start_date, end_date):
                    messagebox.showerror("Invalid Dates", "End date must be after or the same as start date.")
                    return

            # Update db
            self.update_message = self.model.discount.update_discount(column_index, new_value, discount_ID, restaurant_ID)
            if self.update_message == "DB Error":
                messagebox.showerror("DB L", "DB Error, theres nothing we can do...")
            # Update the tree view and get rid of the pop-up window
            self.refresh_tree_view()
            self.frame.edit_window.destroy() 
        else:
            return
    

   
