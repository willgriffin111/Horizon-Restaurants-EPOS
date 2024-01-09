'''
*    Title: How To Organize Multi-frame TKinter Application With MVC Pattern
*    Author: Nazmul Ahsan
*    Date: Jan 6, 2023
*    Code version: 1.0
*    Availability: https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
*
'''

from .auth_m import Auth
from .admin_m import Admin
from .order_m import Order
from .restaurant import Restaurant, Menu
from .reservation_m import ReservationManager
from .inventory_m import Inventory
from .account_m import Account
from .menu_edit_m import MenuEdit
from .reports_m import Reports
from .order_view_m import OrderView
from .discount_m import Discount

class Model:
    def __init__(self):
        self.auth = Auth()
        self.admin = Admin()
        self.order = Order()
        self.orderView = OrderView()
        self.menu = Menu()
        self.reservation = ReservationManager()
        self.inventory = Inventory()
        self.restaurant = Restaurant(self.menu) 
        self.account = Account()
        self.menu_edit = MenuEdit()
        self.reports = Reports()
        self.discount = Discount()
