"""
File name: inventory_c.py
Author: Shahbaz Bokhari
Date created: 31/12/2023
"""
from tkinter import messagebox

from Models.main_m import Model
from Views.main_v import View

class InventoryController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["inventory"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_button.config(command=self.home)
        self.frame.refresh_button.config(command=self.refresh_tree_view) 
        self.frame.inventory_tree.bind("<Double-1>", self.on_double_click)
    
    def home(self):
        self.view.switch("home")

    def update_view(self) -> None:     # updates the username, userid and the latest inventory data on log in
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f"User: {current_user.getName()}")
            self.frame.user_id.config(text=f"ID: {current_user.getStaffId()}")
            self.refresh_tree_view()
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
    
    def refresh_tree_view(self, item_filter_selected='All'):
        # Update the inventory table with the inventory data from the database and the inventory item dropdown filter
        # inventory data returned is what the filter is currently set to
        self.frame.clear_tree_view()
        self.inventory = self.model.inventory.get_items_of_type(item_filter_selected, restaurant_ID=self.model.auth.current_user.getRestrantID()) # managers can only see their branch's inventory
        self.inventory_item_types_list = self.model.inventory.get_inventory_type_list(restaurant_ID=self.model.auth.current_user.getRestrantID()) # this is for the item type filter combobox
        self.frame.insert_tree_view(self.inventory)

        if item_filter_selected:    # Just update the filter to 'All' when the refresh button is clicked since that's what item_filter_selected defaults to
            self.frame.update_item_option_list(self.inventory_item_types_list, item_filter_selected)
        else:                       # This is so the filter doesn't change after they add, delete or update an item
            item_filter_selected = self.frame.selected_option.get()     
            self.frame.update_item_option_list(self.inventory_item_types_list, item_filter_selected)
        self.frame.type_filter_combobox.bind("<<ComboboxSelected>>", self.filter_treeview)
    
    def filter_treeview(self, event):
        # Gets the current filter, then fetches required items from inventory and updates view
        item_type = self.frame.selected_option.get() # get current filter
        restaurant_ID = self.model.auth.current_user.getRestrantID()
        self.inventory = self.model.inventory.get_items_of_type(item_type, restaurant_ID) # get items from current filter type
        self.frame.clear_tree_view()    # then update view like bruh its easy to understand
        self.frame.insert_tree_view(self.inventory)

    def on_double_click(self, event):
        self.row_ID = self.frame.inventory_tree.identify_row(event.y)       # self explanatory, gets the row id based on what value in the tree-view you double clicked
        #print(f"row: {self.row_ID}, col: {self.column_ID}") # this is a W way to check what row and column id cells are, very W

        # Get the tag for the row double clicked on and check if it has the 'lowstock' tag
        # If it does have the tag send an email to the manager with the ITEM DATA letting 'em know to stop slacking and get more in stock, spam the emails if you have to lool
        tags = self.frame.inventory_tree.item(self.row_ID, 'tags')
        has_lowstock_tag = 'lowstock' in tags
        if has_lowstock_tag:
            item_data = self.frame.inventory_tree.item(self.row_ID, 'values')
            #item_data: ('31', 'Spork', '1', '10', 'Cutlery')
            is_email_successful = self.model.inventory.send_reorder_email(item_data)

            if is_email_successful:
                messagebox.showinfo("Success", "Email has been sent!")
            else:
                messagebox.showerror("Error", "Email could not be sent. Sorry, not sorry.")
    
    