""""
File name: order_m.py
Author: Shahbaz
Date Created: 18/12/2023
"""
from enum import Enum

import mysql.connector
import copy
import datetime
import re

from .base_m import ObservableModel
from database import dbfunc

# Mock data



ORDER_STATUS = ['PENDING', 'COMPLETED', 'CANCELLED']

class Order(ObservableModel):
    def __init__(self):
        super().__init__()
        self.order = {}
    
    def saveOrder(self, order):
        self.order = copy.deepcopy(order)
        self.trigger_event("order_saved")
    
    def getSavedOrder(self):
        return self.order

    def create_bill(self, sub_total, discount_applied):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()
                dbcursor.execute("INSERT INTO bill (bill_sub_total, bill_discount_applied) \
                                 VALUES (%s, %s)", (sub_total, discount_applied))
                conn.commit()

                # Get the last inserted bill_id
                dbcursor.execute("SELECT LAST_INSERT_ID()")
                bill_id = dbcursor.fetchone()[0]

                dbcursor.close()
                conn.close() 

                print(f"Bill created with ID: {bill_id}")
            return bill_id

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def create_order(self, restaurant_ID, order, table, author, sub_total, discount_applied):
        bill_id =  self.create_bill(sub_total, discount_applied)
        # Get integer part using regex
        table_num = re.sub(r'\D', '', table)    # could've used lstrip but this is way cooler
        
        try:
            # Convert to integer safely
            table_num = int(table_num)

            if bill_id is not None:
                try:
                    # Create the connection and cursor object
                    conn = dbfunc.getConnection()
                    if conn is not None and conn.is_connected():
                        dbcursor = conn.cursor()

                        # Get the current date and time
                        date_time_created = datetime.datetime.now()
                        # Have to convert to a string and format it to MySQL's datetime format
                        date_time_created_str = date_time_created.strftime('%Y-%m-%d %H:%M:%S')
                        
                        # Insert each menu item from the order
                        for menu_item, details in order.items():
                            # Extracting details from the dictionary
                            name = details.get('name', '')
                            quantity = details.get('quantity', 0)
                            price = details.get('price', 0.0)
                            description = details.get('description', '')



                            # Inserting into the orders table
                            dbcursor.execute("INSERT INTO orders (restaurant_id, bill_id, order_table_num, order_status, order_menu_item, order_menu_item_qty, order_author, order_time_created, order_price, order_menu_item_desc) \
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                            (restaurant_ID, bill_id, table_num, ORDER_STATUS[0], name, quantity, author, date_time_created_str, price, description))

                        conn.commit()
                        dbcursor.close()
                        conn.close() 

                        print("Order created")
                        return True

                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    return False
            
        except ValueError:
            # Letting staff know about erroneous value
            return 'Table value selected has no number'

        
        
        

        