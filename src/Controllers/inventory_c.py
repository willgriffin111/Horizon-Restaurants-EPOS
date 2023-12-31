"""
File name: inventory_c.py
Author: Shahbaz Bokhari
Date created: 30/12/2023
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
        self.frame.add_inventory_item_btn.config(command=self.create_inventory_popup)
        self.frame.remove_inventory_item_btn.config(command=self.remove_inventory_item)
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
        item_type = self.frame.selected_option.get()
        restaurant_ID = self.model.auth.current_user.getRestrantID()
        self.inventory = self.model.inventory.get_items_of_type(item_type, restaurant_ID)
        self.frame.clear_tree_view()
        self.frame.insert_tree_view(self.inventory)
    
    def create_inventory_popup(self): # creates pop up window to add details for the new item
        self.frame.add_inventory_pop()
        self.frame.submit_new_item_btn.configure(command=self.create_inventory_item) # calls function to insert into db and update view
    
    def create_inventory_item(self):    # inserts values into db and updates view (data form pop up window)
        # Get values for new item to be added
        self.item_name = self.frame.name_entry_field.get()
        self.item_stock = self.frame.qty_entry_field.get()
        self.reorder_lvl = self.frame.reorder_entry_field.get()
        self.item_type = self.frame.type_entry_field.get()
        
        # Check if data is missing
        if not all([self.item_name, self.item_stock, self.reorder_lvl, self.item_type]):
            messagebox.showerror("Error", "All fields are required")
            return

        # Inserts inventory item into db
        self.restaurant_ID = self.model.auth.current_user.getRestrantID()
        self.model.inventory.create_inventory_item(self.restaurant_ID, self.item_name, self.item_stock, self.reorder_lvl, self.item_type)

        # Updates view for new inventory item and gets rid of pop up window
        item_filter_selected = self.frame.selected_option.get()
        self.refresh_tree_view(item_filter_selected)
        self.frame.inventory_window.destroy()

    def remove_inventory_item(self):    # deletes values from db and updates view
        #  Use the selected item's id to remove it from the db
        self.selected_item = self.frame.inventory_tree.selection()
        if self.selected_item:
            self.selected_inventory_id = self.frame.inventory_tree.item(self.selected_item)['values'][0]
            self.restaurant_ID = self.model.auth.current_user.getRestrantID()
            self.model.inventory.remove_inventory_item(self.restaurant_ID, self.selected_inventory_id)
            # Update the view
            item_filter_selected = self.frame.selected_option.get()
            self.refresh_tree_view(item_filter_selected)
        else:
            messagebox.showerror("Error", "No item Selected")
        

    def on_double_click(self, event):
        self.row_ID = self.frame.inventory_tree.identify_row(event.y)       # self explanatory, gets the row and column id's based on what value in the tree-view you double clicked
        self.column_ID = self.frame.inventory_tree.identify_column(event.x)
        if self.row_ID and self.column_ID:
            #print(f"row: {self.row_ID}, col: {self.column_ID}")
            if self.column_ID != "#1":  # Checking if they haven't clicked on the inventory_id cause we are NOT letting you edit that buddy. Editing the id is a big no-no
                # Bring up a window where they can edit the value then update the db and view
                self.frame.editWindowPopup(self.row_ID, self.column_ID)
                self.frame.save_changes_button.config(command=lambda row_id=self.row_ID: self.update_inventory_item(row_id))
    
    def update_inventory_item(self, row_ID):
        # Get values from view
        new_value = self.frame.new_value_entry.get()
        column_index = self.frame.column_index
        inventory_ID = self.frame.inventory_tree.item(row_ID, 'values')[0]
        restaurant_ID = self.model.auth.current_user.getRestrantID()
        # Update db
        self.model.inventory.update_inventory_item(column_index, new_value, inventory_ID, restaurant_ID)
        # Update the view and get rid of the pop-up window
        item_filter_selected = self.frame.selected_option.get()
        self.refresh_tree_view(item_filter_selected)
        self.frame.edit_window.destroy()

    
