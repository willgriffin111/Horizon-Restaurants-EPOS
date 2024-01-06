"""
Author: Shahbaz Bokhari
File name: inventory_m.py
Date: 28/12/2023
"""
import mysql.connector

from .base_m import ObservableModel
from database import dbfunc


class Inventory(ObservableModel):
    def __init__(self):
        super().__init__()
        self.inventory = None
    
    def get_inventory(self, restaurant_ID):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()

            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Fetch the inventory from the database for the restaurant specified
                query = "SELECT inventory_id, inventory_item_name, inventory_item_stock, inventory_item_reorder_level, inventory_item_type, is_available FROM inventory WHERE restaurant_id = %s;"
                params = (restaurant_ID,)

                dbcursor.execute(query, params) # parameterized query to avoid SQl injection
                self.inventory = dbcursor.fetchall()

                dbcursor.close()
                conn.close()

                if not self.inventory:
                    print("No inventory data found.")

                return self.inventory

            else:
                print("Database connection failed.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    

    def get_inventory_type_list(self, restaurant_ID):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()
                # Fetch the list of item types
                query = "SELECT DISTINCT inventory_item_type FROM inventory WHERE restaurant_id = %s AND is_available = 1;"
                params = (restaurant_ID,)

                dbcursor.execute(query, params) # parameterized query to avoid SQl injection
                distinct_item_types = dbcursor.fetchall()
                dbcursor.close()
                conn.close()

                if not distinct_item_types:
                    print("No data found.")
                
                cleaned_item_types =  [item_type[0] for item_type in distinct_item_types]  # converting list of tuples -> list of string values |||  [('Ingredient',), ('Beverage',), ('Cutlery',)] -> ['Ingredient', 'Beverage', 'Cutlery']
                item_types = ['All']    #   a default value 
                item_types.extend(cleaned_item_types)   
                return item_types
            
            else:
                print("Database connection failed.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def create_inventory_item(self, restaurant_ID, name, stock, reorder_lvl, item_type):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Check if the inventory item with the given name already exists
                dbcursor.execute("SELECT inventory_item_name FROM inventory WHERE restaurant_id = %s AND inventory_item_name = %s", (restaurant_ID, name))
                existing_name = dbcursor.fetchone()

                if existing_name:
                    print("Inventory item with the same name already exists.")
                    return "Name already exists"
                else:
                    # Insert the new inventory item
                    dbcursor.execute("INSERT INTO inventory (restaurant_id, inventory_item_name, inventory_item_stock, inventory_item_reorder_level, inventory_item_type, is_available) \
                                    VALUES (%s, %s, %s, %s, %s, True)", (restaurant_ID, name, stock, reorder_lvl, item_type))
                    conn.commit()
                    dbcursor.close()
                    conn.close()

                    print("Inventory item created")

        except mysql.connector.Error as err:
            print(f"Error: {err}")



    def remove_inventory_item(self, restaurant_ID, inventory_id):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Retrieve the inventory item name so we can find the corresponding item in the menu table
                dbcursor.execute("SELECT inventory_item_name FROM inventory WHERE restaurant_id = %s AND inventory_id = %s", (restaurant_ID, inventory_id))
                inventory_item_name = dbcursor.fetchone()

                if inventory_item_name:
                    menu_name = inventory_item_name[0]

                    try:
                        # Check if the inventory item name exists in the menu table (this is the corresponding menu item)
                        dbcursor.execute("SELECT menu_item_name FROM menu WHERE restaurant_id = %s AND menu_item_name = %s", (restaurant_ID, menu_name))
                        existing_menu_item = dbcursor.fetchone()

                        if existing_menu_item:
                            # If a corresponding menu item is found then delete from both menu and inventory
                            dbcursor.execute("DELETE FROM menu WHERE restaurant_id = %s AND menu_item_name = %s AND is_available = 0", (restaurant_ID, menu_name))
                            conn.commit()
                            # However, if the menu item isn't 'removed' from the menu by CHEF then you can't delete the inventory and menu item
                            # You can only delete if its been 'removed' by CHEF, and then you can delete the corresponding item from the inventory as well
                            rows_affected = dbcursor.rowcount
                            if rows_affected > 0:
                                print("Corresponding menu item deleted")
                            else:
                                return "Item exists in menu cannot delete"  # this is to display messagebox

                            dbcursor.execute("DELETE FROM inventory WHERE restaurant_id = %s AND inventory_id = %s AND is_available = 0", (restaurant_ID, inventory_id))
                            conn.commit()

                            print("Inventory item deleted")
                        else:
                            # Delete only from inventory
                            dbcursor.execute("DELETE FROM inventory WHERE restaurant_id = %s AND inventory_id = %s", (restaurant_ID, inventory_id))
                            conn.commit()
                            print("Corresponding menu item not found or is not available")

                    except mysql.connector.Error as inner_err:
                        print(f"Error during select from menu: {inner_err}")

                    dbcursor.close()
                    conn.close()

                else:
                    print("Inventory item not found")

        except mysql.connector.Error as err:
            print(f"Error: {err}")


                



    def update_inventory_item(self, column_index, new_value, inventory_ID, restaurant_ID):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Get the current inventory item name
                dbcursor.execute("SELECT inventory_item_name FROM inventory WHERE inventory_id = %s AND restaurant_id = %s", (inventory_ID, restaurant_ID))
                current_item_name = dbcursor.fetchone()

                if current_item_name:
                    current_item_name = current_item_name[0]

                    # Check if the same name exists in the menu table
                    dbcursor.execute("SELECT menu_item_name FROM menu WHERE restaurant_id = %s AND menu_item_name = %s", (restaurant_ID, current_item_name))
                    existing_menu_item = dbcursor.fetchone()

                    if existing_menu_item:
                        # If it's an existing menu item, and the update involves name or type, return an error message
                        if column_index == 1 or column_index == 4:
                            return "Cannot edit name or type, item exists in menu. Edit the name or type of the item there."

                    # If statements map column_index from self.inventory_tree(inventory_v.py) to the column in the db
                    if column_index == 1:
                        dbcursor.execute("UPDATE inventory SET inventory_item_name = %s WHERE inventory_id = %s AND restaurant_id = %s", (new_value, inventory_ID, restaurant_ID))
                    elif column_index == 2:
                        dbcursor.execute("UPDATE inventory SET inventory_item_stock = %s WHERE inventory_id = %s AND restaurant_id = %s", (new_value, inventory_ID, restaurant_ID))
                    elif column_index == 3:
                        dbcursor.execute("UPDATE inventory SET inventory_item_reorder_level = %s WHERE inventory_id = %s AND restaurant_id = %s", (new_value, inventory_ID, restaurant_ID))
                    elif column_index == 4:
                        dbcursor.execute("UPDATE inventory SET inventory_item_type = %s WHERE inventory_id = %s AND restaurant_id = %s", (new_value, inventory_ID, restaurant_ID))
                    
                    conn.commit()
                    dbcursor.close()
                    conn.close() 

                    print("Inventory item updated")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

            
    
    def get_items_of_type(self, item_type, restaurant_ID):

        if item_type == 'All':
            return self.get_inventory(restaurant_ID) 


        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()

            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()
                
                # Fetch the inventory from the database for the restaurant specified
                query = "SELECT inventory_id, inventory_item_name, inventory_item_stock, inventory_item_reorder_level, inventory_item_type, is_available FROM inventory WHERE inventory_item_type = %s AND restaurant_id = %s;"
                params = (item_type, restaurant_ID)

                dbcursor.execute(query, params) # parameterized query to avoid SQl injection
                self.inventory = dbcursor.fetchall()

                dbcursor.close()
                conn.close()

                if not self.inventory:
                    print("No inventory data found.")

                return self.inventory

            else:
                print("Database connection failed.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def send_reorder_email(self, item_data):
        # I'm not gonna actually put my email details in here lol but we can make a dummy email for the demonstration, just simulate for now
        # item_data will let the manager know which item to re-order
        # For now I'm just going to return true to signal the email has been sent without errors
        return True
