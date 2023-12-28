from .auth_m import Auth
from .admin_m import Admin
from .order_m import Order
from .restaurant import Restaurant, Menu
from .reservation_m import ReservationManager


class Model:
    def __init__(self):
        self.auth = Auth()
        self.admin = Admin()
        self.order = Order()
        self.menu = Menu()
        self.reservation = ReservationManager()
        self.restaurant = Restaurant(self.menu) 

        self.menu.addCategory("Starters")
        self.menu.addCategory("Mains")
        self.menu.addCategory("Drinks")
    

        # Adding mock menu items
        # For the "Starter" category
        starter_category = self.menu.categories[0] 
        starter_category.addItem("Starter 1", "", 9.99, {"Ingredient 1" : 1, "Ingredient 2" : 2}, True)
        starter_category.addItem("Starter 2", "", 9.99, {"Ingredient 1" : 1, "Ingredient 2" : 2}, True)
        starter_category.addItem("Starter 3", "", 9.99, {"Ingredient 1" : 1, "Ingredient 2" : 2}, True)
        starter_category.addItem("Starter 4", "", 9.99, {"Ingredient 1" : 1, "Ingredient 2" : 2}, True)
        

        # For the "Main" category
        main_category = self.menu.categories[1]
        main_category.addItem("Main 1", "", 15.99, {"Ingredient 5":3, "Ingredient 6":1}, True)
        main_category.addItem("Main 2", "", 15.99, {"Ingredient 5":3, "Ingredient 6":1}, True)
        main_category.addItem("Main 3", "", 15.99, {"Ingredient 5":3, "Ingredient 6":1}, True)
        main_category.addItem("Main 4", "", 15.99, {"Ingredient 5":3, "Ingredient 6":1}, True)
        

        # For the "Drinks" category
        drinks_category = self.menu.categories[2]
        drinks_category.addItem("Drink 1", "", 4.99, {"Ingredient 9":3, "Ingredient 10":4}, True)
        drinks_category.addItem("Drink 2", "", 4.99, {"Ingredient 9":3, "Ingredient 10":4}, True)
        drinks_category.addItem("Drink 3", "", 4.99, {"Ingredient 9":3, "Ingredient 10":4}, True)
        drinks_category.addItem("Drink 4", "", 4.99, {"Ingredient 9":3, "Ingredient 10":4}, True)
        
        
