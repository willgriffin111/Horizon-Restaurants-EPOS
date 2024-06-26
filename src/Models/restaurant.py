"""
file name: Restaurant.py
Author: Shahbaz, Alex Rogers 
Date Created: 27/12/2022
"""

import datetime
from database import dbfunc
from enum import Enum
import mysql.connector

class OrderStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class PaymentStatus(Enum):
    PENDING = "Pending"
    PAID = "Paid"
    ABANDONED = "Abandoned"

class ReservationStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    


# ------------------MENU ---------------------------
class MenuItem:
    def __init__(self, ID, categoryID, name, desc, price, ingredients, isAvailable) -> None:
       self.menuItemID = ID
       self.categoryID = categoryID
       self.name = name
       self.desc = desc
       self.price = price
       self.ingredients = ingredients
       self.isAvailable = isAvailable

class MenuCategory:

    def __init__(self, ID, name) -> None:
        self.categoryID = ID
        self.name = name
        self.menuItems = []
        self.menuItems = []
    
    def addItem(self, name, desc, price, ingredients, isAvailable):
        menuItemID = len(self.menuItems) + 1
        newItem = MenuItem(menuItemID, self.categoryID, name, desc, price, ingredients, isAvailable)
        self.menuItems.append(newItem)
        return newItem

    def removeItem(self, ID):
        itemToRemove = next((item for item in self.menuItems if item.menuItemID ==ID), None)
        if itemToRemove:
            self.menuItems.remove(itemToRemove)
            return itemToRemove
        else:
            return None
        
        
        
class Menu:
    def __init__(self) -> None:
        self.menuID = None
        self.name = None
        self.description = None
        self.categories = []
    
    """
    old format: {'Starter 1': {'name': 'Starter 1', 'description': '', 'price': 9.99, 'ingredients': {'Ingredient 1': 1, 'Ingredient 2': 2}, 'isAvailable': True, 'quantity': 2}, 'Starter 4': {'name': 'Starter 4', 'description': '', 'price': 9.99, 'ingredients': {'Ingredient 1': 1, 'Ingredient 2': 2}, 'isAvailable': True, 'quantity': 1}, 'Starter 3': {'name': 'Starter 3', 'description': '', 'price': 9.99, 'ingredients': {'Ingredient 1': 1, 'Ingredient 2': 2}, 'isAvailable': True, 'quantity': 3}, 'Main 1': {'name': 'Main 1', 'description': '', 'price': 15.99, 'ingredients': {'Ingredient 5': 3, 'Ingredient 6': 1}, 'isAvailable': True, 'quantity': 1}, 'Main 4': {'name': 'Main 4', 'description': '', 'price': 15.99, 'ingredients': {'Ingredient 5': 3, 'Ingredient 6': 1}, 'isAvailable': True, 'quantity': 2}, 'Drink 2': {'name': 'Drink 2', 'description': '', 'price': 4.99, 'ingredients': {'Ingredient 9': 3, 'Ingredient 10': 4}, 'isAvailable': True, 'quantity': 2}}
    """
    
    def get_menu(self, restaurant_ID):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()

            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()

                # Fetch the menu from the database for the restaurant specified
                query = "SELECT menu_item_name, menu_item_category, menu_item_price FROM menu WHERE restaurant_id = %s AND is_available = 1;"
                params = (restaurant_ID,)

                dbcursor.execute(query, params) # parameterized query to avoid SQl injection
                self.menu = dbcursor.fetchall()
                print(f'db menu:\n {self.menu}\n')

                dbcursor.close()
                conn.close()

                if not self.menu:
                    print("No menu data found.")

                # Formatting the menu data into a dictionary to make it more readable, W W 
                formatted_menu = {}
                for item in self.menu:
                    name, category, price = item[0], item[1], item[2]
                    item_details = {
                        'name': name,
                        'description': '',
                        'price': price,
                    }
                    # Check if the category key already exists in formatted_menu
                    if category not in formatted_menu:
                        formatted_menu[category] = []

                    # Append the item to the corresponding category list
                    formatted_menu[category].append(item_details)
                print(f'formatted menu:\n{formatted_menu}')

                return formatted_menu

            else:
                print("Database connection failed.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def get_menu_items_of_type(self, item_category, restaurant_ID):
        try:
            conn = dbfunc.getConnection()

            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()
                
                if item_category == 'All':
                    query = "SELECT menu_id, menu_item_name, menu_item_category, menu_item_price, menu_item_notes FROM menu WHERE restaurant_id = %s AND is_available = 1;"
                    params = (restaurant_ID,)
                else:
                    query = "SELECT menu_id, menu_item_name, menu_item_category, menu_item_price, menu_item_notes FROM menu WHERE menu_item_category = %s AND restaurant_id = %s AND is_available = 1;"
                    params = (item_category, restaurant_ID)

                dbcursor.execute(query, params)
                self.menu = dbcursor.fetchall()

                dbcursor.close()
                conn.close()

                if not self.menu:
                    print("No menu data found.")

                return self.menu

            else:
                print("Database connection failed.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        
    def get_menu_category_list(self, restaurant_ID):
        # Create the connection and cursor object
        try:
            # Create the connection and cursor object
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()
                # Fetch the list of item types
                query = "SELECT DISTINCT menu_item_category FROM menu WHERE restaurant_id = %s AND is_available = 1;"
                params = (restaurant_ID,)

                dbcursor.execute(query, params) # parameterized query to avoid SQl injection
                distinct_menu_categories = dbcursor.fetchall()
                dbcursor.close()
                conn.close()

                if not distinct_menu_categories:
                    print("No data found.")
                
                cleaned_menu_categories =  [category[0] for category in distinct_menu_categories]  # converting list of tuples -> list of string values |||  [('Ingredient',), ('Beverage',), ('Cutlery',)] -> ['Ingredient', 'Beverage', 'Cutlery']
                item_types = ['All']    #   a default value 
                item_types.extend(cleaned_menu_categories)   
                return item_types
            
            else:
                print("Database connection failed.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

# --------------------ORDER-----------------------
class Order:
    def __init__(self, ID, tableNum, status: OrderStatus, menuItems, paymentStatus: PaymentStatus, createdBy, price) -> None:
        self.orderID = ID
        self.tableNum = tableNum
        self.status = status
        self.menuItems = menuItems
        self.paymentStatus = paymentStatus
        self.createdBy = createdBy
        self.price = price

#-----------------------RESERVATION-----------------------
class Reservation:
    def __init__(self, ID, restaurantID, customerName, customerPhone, partySize, tableNum , createdBy, createdAt, reservationDate, reservationTime,reservationStatus:ReservationStatus, specialRequests=None) -> None:
        self.reservationID = ID
        self.restaurantID = restaurantID
        self.customerName = customerName
        self.customerPhone = customerPhone
        self.reservationDate = reservationDate
        self.reservationTime = reservationTime
        self.specialRequests = specialRequests
        self.partySize = partySize
        self.tableNum = tableNum
        self.reservationStatus = reservationStatus
        self.createdBy = createdBy
        self.createdAt = createdAt
        
    def cancelReservation():
        print("")
        
    def updateReservation(self, column_index, newValue):
        print("")
        self.columnName == ""
        if column_index == 1:
            self.columnName == "reservation_customer_name"
        elif column_index == 2:
            self.columnName == "reservation_customer_phone"
        elif column_index == 4:
            self.columnName == "reservation_date"
        elif column_index == 5:
            self.columnName == "reservation_time"
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("UPDATE reservation SET %s = %s WHERE reservation_id = %s;", (self.columnName,newValue,self.reservationID)) 
                conn.commit()
                dbcursor.close()
                conn.close() 
                
    
                
        
    def getReservationDetails():
        print("")
        
    def reservationToJSON():
        print("")
    
    
    
    def removeFromDB():
        print("")

#---------------------------RESTAURANT------------------------------
class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.restaurantID = None
        self.name = None
        self.name = None
        self.capacity = None
        self.numStaff = None
        self.managerName = None
        self.employees = None
        self.reports = None
        self.reservations = None
        self.inventory = None
        self.orders = None
        self.tables = None

    def createOrder(self, tableNum, status, menuItems, paymentStatus, createdBy, price):
        orderID = len(self.orders) + 1  
        newOrder = Order(orderID, tableNum, status, menuItems, paymentStatus, createdBy, price)
        self.orders.append(newOrder)
        return newOrder
    
    def removeOrder(self, orderID):
        orderToRemove = next((order for order in self.orders if order.orderID == orderID), None)
        if orderToRemove:
            self.orders.remove(orderToRemove)
            return orderToRemove
        else:
            return None



