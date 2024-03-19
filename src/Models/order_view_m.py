from .base_m import ObservableModel
from database import dbfunc
from tkinter import messagebox
import mysql.connector
import tkinter as tk


class OrderView(ObservableModel):
    

    # def getTableOrders(self):
    #     tableOrders = {
    #         "Table 1": [("Starter 1", 1), ("Main 3", 2), ("Desert 2", 2)],
    #         "Table 2": [("Starter 1", 1), ("Main 6", 1, "No egg"), ("Main 2", 1), ("Main 10", 1, "Medium Spice", "No salt")],
    #         "Table 3": [("Main 6", 1), ("Main 2", 1, "No tomatoes"), ("Desert 8", 1), ("Desert 4", 1)],
    #         "Table 4": [("Main 6", 1), ("Main 2", 1, "No tomatoes"), ("Desert 8", 1), ("Desert 4", 1)],
    #         "Table 5": [("Starter 3", 2), ("Main 5", 1), ("Desert 1", 1)],
    #         "Table 6": [("Starter 2", 1), ("Main 1", 2, "Extra cheese"), ("Main 4", 1, "Less spice"), ("Desert 3", 2)],
    #         "Table 7": [("Main 7", 1), ("Main 8", 2, "Gluten-free"), ("Desert 5", 1)],
    #         "Table 8": [("Starter 4", 1, "Vegan"), ("Main 9", 1), ("Main 11", 1, "No onion"), ("Desert 6", 1, "Sugar-free")]
    #     }
    #     return tableOrders  
    
    def updateOrder(self, column_index, newValue,restaurant_ID, tableNum):
        try:
            with dbfunc.getConnection() as conn:
                if conn.is_connected():
                    if column_index == 1:
                        query = """
                                UPDATE orders 
                                SET order_menu_item = %s 
                                WHERE restaurant_id = %s AND order_table_num = %s;
                                """
                    
                    elif column_index == 2:
                        query = """
                                UPDATE orders 
                                SET order_menu_item_qty = %s 
                                WHERE restaurant_id = %s AND order_table_num = %s;
                                """

                    elif column_index == 3:
                        query = """
                                UPDATE orders 
                                SET order_menu_item_desc = %s 
                                WHERE restaurant_id = %s AND order_table_num = %s;
                                """
                    params = (newValue, restaurant_ID, tableNum)
                    with conn.cursor() as cursor:
                        cursor.execute(query, params)
                        conn.commit()
                        messagebox.showinfo("Success", "Order updated successfully.")
                        return True 
                else:
                    print("Database connection failed.")
                    return False
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            return False
            
            
    
    # def updateOrder(self, column_index, newValue, orderID):
    #     try:
    #         with dbfunc.getConnection() as conn:
    #             if conn.is_connected():
    #                 if column_index == 1:
    #                     query = """
    #                             UPDATE orders 
    #                             SET order_menu_item = %s 
    #                             WHERE order_id = %s;
    #                             """
                        
    #                 elif column_index == 2:
    #                     query = """
    #                             UPDATE orders 
    #                             SET order_menu_item_qty = %s 
    #                             WHERE order_id = %s;
    #                             """

    #                 elif column_index == 3:
    #                     query = """
    #                             UPDATE orders 
    #                             SET order_menu_item_desc = %s 
    #                             WHERE order_id = %s;
    #                             """
    #                 params = (newValue, orderID)
    #                 with conn.cursor() as cursor:
    #                     cursor.execute(query, params)
    #                     conn.commit()
    #                     messagebox.showinfo("Success", "Order updated successfully.")
    #                     return True
                    
                    
    #             else:
    #                 print("Database connection failed.")
    #                 return False
    #     except mysql.connector.Error as err:
    #         print(f"Database Error: {err}")
    #         return False
       
    
    def getSingleOrder(self, restaurant_ID, tableNum) -> tuple:
        try:
            with dbfunc.getConnection() as conn:
                if conn.is_connected():
                    query = """
                            SELECT order_menu_item, order_menu_item_qty, order_menu_item_desc
                            FROM orders 
                            WHERE restaurant_id = %s AND order_table_num = %s AND order_status = 'PENDING';
                            """
                    params = (restaurant_ID, tableNum)
                    with conn.cursor() as cursor:
                        cursor.execute(query, params)
                        order_details = {}
                        for row in cursor:
                            order_details[row[0]] = (row[1], row[2])
                    return order_details
                else:
                    print("Database connection failed.")
                    return {}
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            return {}
    
    def getTableOrders(self, restaurant_ID) -> dict:

        table_orders = {}
        try:
            with dbfunc.getConnection() as conn:
                if conn.is_connected():
                    query = """
                            SELECT order_table_num, order_menu_item, order_menu_item_qty, order_menu_item_desc
                            FROM orders 
                            WHERE restaurant_id = %s AND order_status = 'PENDING';
                            """
                    params = (restaurant_ID,)
                    with conn.cursor() as cursor:
                        cursor.execute(query, params)
                        for row in cursor:
                            table_num = f"Table {row[0]}"
                            order_details = (row[1], row[2], row[3])  
                            if table_num not in table_orders:
                                table_orders[table_num] = []
                            table_orders[table_num].append(order_details)

                    return table_orders
                else:
                    print("Database connection failed.")
                    return table_orders
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            return table_orders
    
    def completeOrder(self, restaurant_ID, tableNum):
        
        try:
            with dbfunc.getConnection() as conn:
                if conn.is_connected():
                    query = """
                            UPDATE orders 
                            SET order_status = 'COMPLETED' 
                            WHERE restaurant_id = %s AND order_table_num = %s;
                            """
                    params = (restaurant_ID, tableNum)
                    with conn.cursor() as cursor:
                        cursor.execute(query, params)
                        conn.commit()
                        return True
                else:
                    print("Database connection failed.")
                    return False
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            return False
    
    def cancelOrder(self, restaurant_ID, tableNum):
            try:
                with dbfunc.getConnection() as conn:
                    if conn.is_connected():
                        query = """
                                DELETE FROM orders 
                                WHERE restaurant_id = %s AND order_table_num = %s;
                                """
                        params = (restaurant_ID, tableNum)
                        with conn.cursor() as cursor:
                            cursor.execute(query, params)
                            conn.commit()
                            return True
                    else:
                        print("Database connection failed.")
                        return False
            except mysql.connector.Error as err:
                print(f"Database Error: {err}")
                return False


    # def getOrders(self, restaurant_ID) -> None:
    #     # Create the connection and cursor object
    #     try:
    #         # Create the connection and cursor object
    #         conn = dbfunc.getConnection()

    #         if conn is not None and conn.is_connected():
    #             dbcursor = conn.cursor()

    #             # Fetch the orders from the database for the restaurant specified
    #             query = "SELECT * FROM orders WHERE restaurant_id = %s AND order_status = 'PENDING';"
    #             # query = "SELECT order_id, order_table_num, order_menu_item, order_menu_item_qty, order_menu_item_desc, order_price FROM orders WHERE restaurant_id = %s AND order_status = 'PENDING';"

    #             params = (restaurant_ID)

    #             dbcursor.execute(query, params) # parameter ized query to avoid SQl injection
    #             self.inventory = dbcursor.fetchall()

    #             dbcursor.close()
    #             conn.close()

    #             if not self.inventory:
    #                 print("No Orders found.")

    #             return self.inventory

    #         else:
    #             print("Database connection failed.")

    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")
        
    # def markOrderAsComplete(self,restaurant_ID, order_id) -> None:
    #     # Create the connection and cursor object
    #     try:
    #         # Create the connection and cursor object
    #         conn = dbfunc.getConnection()

    #         if conn is not None and conn.is_connected():
    #             dbcursor = conn.cursor()

    #             # Fetch the orders from the database for the restaurant specified
    #             query = "UPDATE orders SET order_status = 'COMPLETE' WHERE restaurant_id = %s AND order_id = %s;"
            
    #             params = (restaurant_ID, order_id)

    #             dbcursor.execute(query, params) # parameterized query to avoid SQl injection
    #             conn.commit()
    #             dbcursor.close()
    #             conn.close()

    #             if not self.inventory:
    #                 print("No Orders found.")

    #             return self.inventory

    #         else:
    #             print("Database connection failed.")

    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")
        