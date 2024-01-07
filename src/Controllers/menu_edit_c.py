"""
File name: menu_edit_c.py
Author: Shahbaz Bokhari
Date created: 05/01/2024
"""
from tkinter import messagebox

from Models.main_m import Model
from Views.main_v import View

class MenuEditController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["menu-edit"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_btn.config(command=self.home)
        self.frame.refresh_btn.config(command=self.refresh_tree_view)
        self.frame.add_menu_item_btn.config(command=self.create_menu_item_popup)
        self.frame.remove_menu_item_btn.config(command=self.remove_menu_item)
        self.frame.edit_menu_item_btn.config(command=self.edit_menu_item_popup)
    
    def home(self) -> None:
        self.view.switch("home")

    def update_view(self):
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f"User: {current_user.getName()}")
            self.frame.user_id.config(text=f"ID: {current_user.getStaffId()}")
            self.refresh_tree_view()
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
        
    def refresh_tree_view(self, category_filter_selected='All'):
        self.frame.clear_tree_view()
        restaurant_ID = self.model.auth.current_user.getRestrantID()
        self.menu = self.model.menu.get_menu_items_of_type(category_filter_selected, restaurant_ID)
        self.menu_category_list = self.model.menu.get_menu_category_list(restaurant_ID)
        self.frame.insert_tree_view(self.menu)
        if category_filter_selected:
            self.frame.update_category_option_list(self.menu_category_list, category_filter_selected)
        else:
            category_filter_selected = self.frame.selected_category_option.get()
            self.frame.update_category_option_list(self.menu_category_list, category_filter_selected)
        self.frame.category_filter_combobox.bind("<<ComboboxSelected>>", self.filter_treeview)
    
    def filter_treeview(self, event):
        # Gets the current filter, then fetched required items from menu and updates view
        category = self.frame.selected_category_option.get()
        restaurant_ID = self.model.auth.current_user.getRestrantID()
        self.menu = self.model.menu.get_menu_items_of_type(category, restaurant_ID)
        self.frame.clear_tree_view()
        self.frame.insert_tree_view(self.menu)
    
    def create_menu_item_popup(self): # created pop up window to add details for the new item
        self.frame.add_menu_item_popup()
        self.frame.submit_new_item_btn.configure(command=self.create_menu_item) # calls function to insert into db and update view
    
    def create_menu_item(self): # inserts values into db and updates view (data form pop up window)
        # Get values of new items to be added
        self.item_name = self.frame.add_menu_item_name_entry.get()
        self.item_category = self.frame.add_menu_item_category_entry.get()
        self.item_price = self.frame.add_menu_item_price_entry.get()
        self.item_desc = self.frame.add_menu_item_desc_entry.get()

        # Check if data is missing
        if not all([self.item_name, self.item_category, self.item_price, self.item_desc]):
            messagebox.showerror("Error", "All fields are required")
            return

        # Insert new menu item into db
        restaurant_ID = self.model.auth.current_user.getRestrantID()
        completion_message = self.model.menu_edit.create_menu_item(restaurant_ID, self.item_name, self.item_category, self.item_price, self.item_desc)
        if completion_message == "Name already exists":
            messagebox.showerror("Error", "Item name already exists!")
            return

        # Updates view for new menu item and gets rid of pop up window
        category_filter_selected = self.frame.selected_category_option.get()
        self.refresh_tree_view(category_filter_selected)
        self.frame.add_menu_item_window.destroy()
    
    def remove_menu_item(self): # deletes menu item from db and updates view
        #   Use the selected item's id to remove it from the db
        self.selected_item = self.frame.menu_tree.selection()
        if self.selected_item:
            self.confirmation = messagebox.askquestion('Delete Item', 'Are you sure you want to remove this item?')
            if self.confirmation == 'yes':
                self.selected_menu_item_id = self.frame.menu_tree.item(self.selected_item)['values'][0]
                self.restaurant_ID = self.model.auth.current_user.getRestrantID()
                self.model.menu_edit.remove_menu_item(self.restaurant_ID, self.selected_menu_item_id)
                # Update the view
                category_filter_selected = self.frame.selected_category_option.get()
                self.refresh_tree_view(category_filter_selected)
        else:
            messagebox.showerror("Error", "No Item Selected")

    def edit_menu_item_popup(self):
        self.selected_item = self.frame.menu_tree.selection()
        if self.selected_item:
            self.selected_item_data = []
            self.selected_item_data.append(self.frame.menu_tree.item(self.selected_item)['values'][0])
            self.selected_item_data.append(self.frame.menu_tree.item(self.selected_item)['values'][1])
            self.selected_item_data.append(self.frame.menu_tree.item(self.selected_item)['values'][2])
            self.selected_item_data.append(self.frame.menu_tree.item(self.selected_item)['values'][3])
            self.selected_item_data.append(self.frame.menu_tree.item(self.selected_item)['values'][5])
            self.frame.edit_menu_popup(self.selected_item_data)
            self.frame.submit_item_changes_btn.config(command=self.edit_menu_item)
        else:
            messagebox.showerror("Error", "No Item Selected")
    
    def edit_menu_item(self):   # Updates values in db and updates view
        # Get values for item to be updated
        self.updated_item_name = self.frame.update_item_name_entry.get()
        self.updated_item_category = self.frame.update_item_category_entry.get()
        self.updated_item_price = self.frame.update_item_price_entry.get()
        self.updated_item_desc = self.frame.update_item_desc_entry.get()

        self.item_id = self.selected_item_data[0]   # item ID for the menu item selected

        # Check if atleast one field is filled
        if not any([self.updated_item_name, self.updated_item_category, self.updated_item_price, self.updated_item_desc]):
            messagebox.showerror("Error", "At least one field is required.")
            return

        # Update new menu item into db
        restaurant_ID = self.model.auth.current_user.getRestrantID()
        completion_message = self.model.menu_edit.update_menu_item(restaurant_ID, self.item_id, self.updated_item_name, self.updated_item_category, self.updated_item_price, self.updated_item_desc)
        if completion_message == "Name already exists":
            messagebox.showerror("Error", "Item name already exists!")
            return
        
        # Updates view for new menu item and gets rid of pop up window
        category_filter_selected = self.frame.selected_category_option.get()
        self.refresh_tree_view(category_filter_selected)
        self.frame.menu_edit_window.destroy()