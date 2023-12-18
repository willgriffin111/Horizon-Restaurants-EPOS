from .auth_m import Auth
from .admin_m import Admin
from .restaurant import Restaurant, Menu


class Model:
    def __init__(self):
        self.auth = Auth()
        self.admin = Admin()
        #self.menu = Menu(menuID, menuName, menuDesc, menuCategories, restaurantName)
        #self.restaurant = Restaurant(restaurantName, self.menu) 
