"""
File name: menu_edit_m.py
Author: Shahbaz Bokhari
Date Created: 05/01/2024
"""
import mysql.connector

from .base_m import ObservableModel
from database import dbfunc

class MenuEdit(ObservableModel):
    def __init__(self):
        super().__init__()
    
    def create_menu_item(self, restaurant_ID, name, category, price, desc):
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Check if the menu item with the given name already exists
                dbcursor.execute("SELECT menu_item_name FROM menu WHERE restaurant_id = %s AND menu_item_name = %s AND is_available = 1;", (restaurant_ID, name))
                existing_name = dbcursor.fetchone()

                if existing_name:
                    print("Menu item with the same name already exists.")
                    return "Name already exists"
                else:
                    # Insert the new menu item
                    dbcursor.execute("INSERT INTO menu (restaurant_id, menu_item_name, menu_item_category, menu_item_notes, menu_item_price, is_available) \
                                    VALUES (%s, %s, %s, %s, %s, True)", (restaurant_ID, name, category, desc, price))
                    # Insert menu item into inventory but have default values for stock and re order level
                    dbcursor.execute("INSERT INTO inventory (restaurant_id, inventory_item_name, inventory_item_stock, inventory_item_reorder_level, inventory_item_type, is_available) \
                                 VALUES (%s, %s, 0, 0, %s, True)", (restaurant_ID, name, category))
                    conn.commit()


                dbcursor.close()
                conn.close()
                
                print("Menu item created and added to inventory")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def remove_menu_item(self, restaurant_ID, item_id):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Check if the item exists (just in case theres some weird tkinter edge case where its still showing in the view and the manager hasnt refreshed the page, look at me caring, so W)
                dbcursor.execute("SELECT menu_item_name FROM menu WHERE restaurant_id = %s AND menu_id = %s", (restaurant_ID, item_id))
                menu_item_name = dbcursor.fetchone() # idk why im even doing this check for an edge case that'll never happen, but oh well 

                if menu_item_name:
                    # Update is_available to False in the menu table
                    dbcursor.execute("UPDATE menu SET is_available = 0 WHERE restaurant_id = %s AND menu_id = %s", (restaurant_ID, item_id))
                    conn.commit()

                    # Update is_available to False in the inventory table
                    dbcursor.execute("UPDATE inventory SET is_available = 0 WHERE restaurant_id = %s AND inventory_item_name = %s", (restaurant_ID, menu_item_name[0]))
                    conn.commit()

                    dbcursor.close()
                    conn.close()

                    print("Menu item deleted")
                else:
                    print("Menu item not found")

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def update_menu_item(self, restaurant_ID, item_id, name, category, price, desc):
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Get the current menu item details
                dbcursor.execute("SELECT menu_item_name, menu_item_category FROM menu WHERE restaurant_id = %s AND menu_id = %s", (restaurant_ID, item_id))
                current_menu_item = dbcursor.fetchone()

                if current_menu_item:
                    current_name, current_category = current_menu_item

                    if not (name.isspace() or name == ""):
                        # Check if the new name already exists for a DIFFERENT menu item
                        dbcursor.execute("SELECT menu_id FROM menu WHERE restaurant_id = %s AND menu_item_name = %s AND menu_id != %s", (restaurant_ID, name, item_id))
                        duplicate_item = dbcursor.fetchone()
                        if not duplicate_item:
                            # Update the name only if it's not a duplicate
                            dbcursor.execute("UPDATE menu SET menu_item_name = %s WHERE menu_id = %s AND restaurant_id = %s", (name, item_id, restaurant_ID))

                            # Update the corresponding entry in the inventory table
                            dbcursor.execute("UPDATE inventory SET inventory_item_name = %s WHERE restaurant_id = %s AND inventory_item_name = %s", (name, restaurant_ID, current_name))
                        else:
                            return "Name already exists"

                    if not (category.isspace() or category == ""):
                        dbcursor.execute("UPDATE menu SET menu_item_category = %s WHERE menu_id = %s AND restaurant_id = %s", (category, item_id, restaurant_ID))

                        # Update the corresponding entry in the inventory table
                        dbcursor.execute("UPDATE inventory SET inventory_item_type = %s WHERE restaurant_id = %s AND inventory_item_name = %s", (category, restaurant_ID, current_name))

                    if not (price.isspace() or price == ""):
                        dbcursor.execute("UPDATE menu SET menu_item_price = %s WHERE menu_id = %s AND restaurant_id = %s", (price, item_id, restaurant_ID))
                    
                    if not (desc.isspace() or desc == ""):
                        dbcursor.execute("UPDATE menu SET menu_item_notes = %s WHERE menu_id = %s AND restaurant_id = %s", (desc, item_id, restaurant_ID))

                    conn.commit()
                    dbcursor.close()
                    conn.close() 

                    print("Menu item updated")
                else:
                    print("Menu item not found")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
