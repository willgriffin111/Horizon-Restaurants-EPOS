"""
file name: Restaurant.py
Author: Shahbaz, Alex Rogers 
Date Created: 27/12/2022
"""

import datetime
from database import dbfunc
from enum import Enum


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
    def __init__(self) -> None:
        self.menuID = None
        self.name = None
        self.description = None
        self.categories = []
    
    def addCategory(self, name):
        categoryID = len(self.categories) + 1
        newCategory = MenuCategory(categoryID, name)
        newCategory = MenuCategory(categoryID, name)
        self.categories.append(newCategory)
        return newCategory

    def removeCategory(self, ID):
        categoryToRemove = next((cat for cat in self.categories if cat.categoryID == ID), None)
        if categoryToRemove:
            self.categories.remove(categoryToRemove)
            return categoryToRemove
        else:
            return None
    
    def getMenu(self):
        menu = {}

        for category in self.categories:
            categoryName = category.name
            categoryItems = []
        
            for item in category.menuItems:
                itemDetails = {
                    'name': item.name,
                    'description': item.desc,
                    'price': item.price,
                    'ingredients': item.ingredients,
                    'isAvailable': item.isAvailable
                }
                categoryItems.append(itemDetails)

            menu[categoryName] = categoryItems
        
        return menu

    def getCategories(self):
        return [category.name for category in self.categories]
    
    def getMenuItemsForCategory(self, categoryName):
        category = next((cat for cat in self.categories if cat.name == categoryName), None)
        if category:
            return [item.name for item in category.menuItems]
        else:
            return []

    def getMenuItemDetails(self, menuItem):
        pass
    
    
    def getMenu(self):
        menu = {}

        for category in self.categories:
            categoryName = category.name
            categoryItems = []
        
            for item in category.menuItems:
                itemDetails = {
                    'name': item.name,
                    'description': item.desc,
                    'price': item.price,
                    'ingredients': item.ingredients,
                    'isAvailable': item.isAvailable
                }
                categoryItems.append(itemDetails)

            menu[categoryName] = categoryItems
        
        return menu

    def getCategories(self):
        return [category.name for category in self.categories]
    
    def getMenuItemsForCategory(self, categoryName):
        category = next((cat for cat in self.categories if cat.name == categoryName), None)
        if category:
            return [item.name for item in category.menuItems]
        else:
            return []

    def getMenuItemDetails(self, menuItem):
        pass
    

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
        
    def updateReservation(self, column_index, newValueUI):
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
                dbcursor.execute("UPDATE reservation SET %s = %s WHERE reservation_id = %s;", (self.columnName,newValueUI,self.reservationID)) 
                conn.commit()
                dbcursor.close()
                conn.close() 
                
    def checkAvailability(self):
        # Calculate the start and end times
        self.beforeReservationTime = self.reservationTime - datetime.timedelta(hours=3)
        self.afterReservationTime = self.reservationTime + datetime.timedelta(hours=3)

        # Format the times as strings in the format MySQL expects
        self.beforeReservationTime = self.beforeReservationTime.strftime("%H:%M:%S")
        self.afterReservationTime = self.afterReservationTime.strftime("%H:%M:%S")
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("SELECT * FROM reservation WHERE reservation_date = %s \
                AND reservation_time BETWEEN (%s) AND (%s);", (self.reservationDate,self.beforeReservationTime,self.afterReservationTime))
                if(dbcursor.rowcount > 0):
                    dbcursor.close()
                    conn.close() 
                    return False
                else:
                    dbcursor.close()
                    conn.close() 
                    return True
                
        
    def getReservationDetails():
        print("")
        
    def reservationToJSON():
        print("")
    
    # def insertToDB(self):
    #     print('Adding New Reservation')          
    #     conn = dbfunc.getConnection() 
    #     if conn != None:    #Checking if connection is None                  
    #         if conn.is_connected(): #Checking if connection is established                        
    #             print('MySQL Connection is established')                          
    #             dbcursor = conn.cursor()    #Creating cursor object                                                 
    #             dbcursor.execute("INSERT INTO employee (employee_name, employee_account_type, \
    #                              employee_password) VALUES (%s, %s, %s)", (staffName, staffType, staffPass))                                        
    #             conn.commit() 
    #             print("User created sucsesfully")
    #             dbcursor.close()       
    #             conn.close()
    #     print("")
    
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



