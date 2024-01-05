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
