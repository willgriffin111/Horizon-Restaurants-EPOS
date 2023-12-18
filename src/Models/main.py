from .auth import Auth
from .restaurant import Restaurant, Menu


class Model:
    def __init__(self, menuID=None, menuName=None, menuDesc=None, menuCategories=None, restaurantName=None):
        self.auth = Auth()
        self.menu = Menu(menuID, menuName, menuDesc, menuCategories, restaurantName)
        self.restaurant = Restaurant(restaurantName, self.menu) 


    