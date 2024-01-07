"""
Author: Shahbaz Bokhari
File name: discount_m.py
Date: 07/01/2023
"""
import mysql.connector

from .base_m import ObservableModel
from database import dbfunc


class Discount(ObservableModel):
    def __init__(self):
        super().__init__()
    

    def get_discounts(self, restaurant_ID):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()

            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Fetch the inventory from the database for the restaurant specified
                query = "SELECT discount_id, discount_name, discount_start, discount_end, discount_value FROM discounts WHERE restaurant_id = %s;"
                params = (restaurant_ID,)

                dbcursor.execute(query, params) # parameterized query to avoid SQl injection
                self.discounts = dbcursor.fetchall()

                dbcursor.close()
                conn.close()

                if not self.discounts:
                    print("No discount data found.")
                print(self.discounts)
                return self.discounts

            else:
                print("Database connection failed.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def get_discounts_for_orders(self, restaurant_ID):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()

            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Fetch the inventory from the database for the restaurant specified and that its not expired
                query = "SELECT discount_name, discount_value FROM discounts WHERE restaurant_id = %s AND discount_end >= CURDATE();"
                params = (restaurant_ID,)

                dbcursor.execute(query, params) # parameterized query to avoid SQl injection
                self.discounts = dbcursor.fetchall()

                dbcursor.close()
                conn.close()

                if not self.discounts:
                    print("No unexpired discount data found.")
                print(self.discounts)
                return self.discounts

            else:
                print("Database connection failed.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    #     self.model.discount.create_discount(self.restaurant_ID, self.name_value, self.value_percentage, self.start_date, self.end_date)
    def create_discount(self, restaurant_ID, name, value_percentage, start_date, end_date):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()
                print(start_date)
                # Check if the discount name already exists
                dbcursor.execute("SELECT discount_name FROM discounts WHERE restaurant_id = %s AND discount_name = %s", (restaurant_ID, name))
                existing_name = dbcursor.fetchone()

                if existing_name:
                    print("Discount with the same name already exists.")
                    return "Name already exists"
                else:
                    # Insert the new discount
                    dbcursor.execute("INSERT INTO discounts (restaurant_id, discount_name, discount_value, discount_start, discount_end) \
                                    VALUES (%s, %s, %s, %s, %s)", (restaurant_ID, name, value_percentage, start_date, end_date))
                    conn.commit()
                    dbcursor.close()
                    conn.close()

                    print("Discount created")
                    return "Discount created"
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "DB Error"
        
    def remove_discount(self, restaurant_ID, discount_id):
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Check if the discount exists (just in case theres some weird tkinter edge case where its still showing in the view and the manager hasnt refreshed the page, look at me caring, so W)
                dbcursor.execute("SELECT * FROM discounts WHERE restaurant_id = %s AND discount_id = %s", (restaurant_ID, discount_id))
                existing_discount = dbcursor.fetchone() # idk why im even doing this check for an edge case that'll never happen, but oh well 

                if existing_discount:
                    # Remove the discount
                    dbcursor.execute("DELETE FROM discounts WHERE restaurant_id = %s AND discount_id = %s", (restaurant_ID, discount_id))
                    conn.commit()
                    dbcursor.close()
                    conn.close()

                    print("Discount removed")
                    return "Discount removed"
                else:
                    print("Discount not found.")
                    return "Discount not found"

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "DB Error"
    
    def update_discount(self, column_index, new_value, discount_ID, restaurant_ID):
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # If statements map column_index to the column in the discounts table
                if column_index == 1:
                    dbcursor.execute("UPDATE discounts SET discount_name = %s WHERE discount_id = %s AND restaurant_id = %s", (new_value, discount_ID, restaurant_ID))
                elif column_index == 2:
                    dbcursor.execute("UPDATE discounts SET discount_start = %s WHERE discount_id = %s AND restaurant_id = %s", (new_value, discount_ID, restaurant_ID))
                elif column_index == 3:
                    dbcursor.execute("UPDATE discounts SET discount_end = %s WHERE discount_id = %s AND restaurant_id = %s", (new_value, discount_ID, restaurant_ID))
                elif column_index == 4:
                    dbcursor.execute("UPDATE discounts SET discount_value = %s WHERE discount_id = %s AND restaurant_id = %s", (new_value, discount_ID, restaurant_ID))

                conn.commit()
                dbcursor.close()
                conn.close()

                print("Discount updated")
                return "Discount updated"

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "DB Error"



