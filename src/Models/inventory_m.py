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
                query = "SELECT inventory_id, inventory_item_name, inventory_item_stock, inventory_item_reorder_level, inventory_item_type FROM inventory WHERE restaurant_id = %s;"
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
                query = "SELECT DISTINCT inventory_item_type FROM inventory WHERE restaurant_id = %s;"
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
                dbcursor.execute("INSERT INTO inventory (restaurant_id, inventory_item_name, inventory_item_stock, inventory_item_reorder_level, inventory_item_type) \
                                 VALUES (%s, %s, %s, %s, %s)", (restaurant_ID, name, stock, reorder_lvl, item_type))
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
                query = ("DELETE FROM inventory WHERE restaurant_id = %s AND inventory_id = %s;")
                params = (restaurant_ID, inventory_id)
                dbcursor.execute(query, params)
                conn.commit()
                dbcursor.close()
                conn.close() 

                print("Inventory item deleted")

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def update_inventory_item(self, column_index, new_value, inventory_ID, restaurant_ID):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

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
                query = "SELECT inventory_id, inventory_item_name, inventory_item_stock, inventory_item_reorder_level, inventory_item_type FROM inventory WHERE inventory_item_type = %s AND restaurant_id = %s;"
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




