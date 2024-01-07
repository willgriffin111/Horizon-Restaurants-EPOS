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

    def clear_order(self):
        self.order = {}

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
        bill_id = self.create_bill(sub_total, discount_applied)

        # Get integer part using regex
        table_num = re.sub(r'\D', '', table)

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

                        # Deduct items from inventory
                        items_out_of_stock = {}
                        for menu_item, details in order.items():
                            # Extracting details from the dictionary
                            name = details.get('name', '')
                            quantity = details.get('quantity', 0)
                            price = details.get('price', 0.0)
                            description = details.get('description', '')

                            # Check stock availability
                            dbcursor.execute("SELECT inventory_item_stock FROM inventory WHERE restaurant_id = %s AND inventory_item_name = %s",
                                            (restaurant_ID, name))
                            current_stock = dbcursor.fetchone()

                            if current_stock:
                                current_stock = current_stock[0]

                                # Deduct the maximum possible quantity from the inventory
                                quantity_to_deduct = min(quantity, current_stock)

                                # Update the inventory with the new stock quantity
                                new_stock = current_stock - quantity_to_deduct
                                dbcursor.execute("UPDATE inventory SET inventory_item_stock = %s WHERE restaurant_id = %s AND inventory_item_name = %s",
                                                (new_stock, restaurant_ID, name))

                                # Log a message (you can customize this based on your needs)
                                print(f"Deducted {quantity_to_deduct} units of {name} from stock.")

                                # Insert into the orders table with the deducted quantity
                                dbcursor.execute("INSERT INTO orders (restaurant_id, bill_id, order_table_num, order_status, order_menu_item, order_menu_item_qty, order_author, order_time_created, order_price, order_menu_item_desc) \
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                                (restaurant_ID, bill_id, table_num, ORDER_STATUS[0], name, quantity_to_deduct, author, date_time_created_str, price, description))

                                # Check if there is remaining quantity
                                remaining_quantity = quantity - quantity_to_deduct
                                if remaining_quantity > 0:
                                    # Append the item individually to items_out_of_stock
                                    items_out_of_stock[name] = {
                                        'quantity': remaining_quantity,
                                        'price': price,
                                        'description': description
                                    }

                            else:
                                # Item is out of stock
                                items_out_of_stock[name] = {
                                    'quantity': quantity,
                                    'price': price,
                                    'description': description
                                }

                                # Log a message (you can customize this based on your needs)
                                print(f"Inventory item {name} not found or insufficient stock. Refunding {quantity} items.")


                        # Update the bill with the updated price
                        # Update the bill with the updated price
                        remaining_price = sum(item['quantity'] * item['price'] for item in items_out_of_stock.values())
                        dbcursor.execute("UPDATE bill SET bill_sub_total = %s WHERE bill_id = %s",
                                        (sub_total - remaining_price, bill_id))


                        conn.commit()
                        dbcursor.close()
                        conn.close()

                        if items_out_of_stock:
                            # Handle remaining quantity as needed
                            # You can customize this part based on your requirements
                            print("Items out of stock:", items_out_of_stock)

                        print("Order created")
                        return items_out_of_stock

                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    return 'DB Error'

        except ValueError:
            # Letting staff know about erroneous value
            return 'Table value selected has no number'
