"""
file name: Restaurant.py
Author: Shahbaz 
Date Created: 18/12/2022
"""
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
    CANCELLED = "Cancelled"


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
    
    def addCategory(self, name):
        categoryID = len(self.categories) + 1
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
    def __init__(self, ID, restaurantID, customerName, customerPhone, reservationTime, partySize, tableNum, reservationStatus:ReservationStatus, createdBy, createdAt, specialRequests=None) -> None:
        self.reservationID = ID
        self.restaurantID = restaurantID
        self.customerName = customerName
        self.customerPhone = customerPhone
        self.reservationTime = reservationTime
        self.specialRequests = specialRequests
        self.partySize = partySize
        self.tableNum = tableNum
        self.reservationStatus = reservationStatus
        self.createdBy = createdBy
        self.createdAt = createdAt

#---------------------------RESTAURANT------------------------------
class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.restaurantID = None
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



