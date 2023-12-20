"""
File name: order_c.py
Author: Shahbaz
Date created: 17/12/2023
"""

from Models.main_m import Model
from Views.main_v import View

class OrderController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["order"]
        self.updateCategories()
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.homeButton.config(command=self.home)
        self.frame.modify.config(command=self.modify)

        # Bind categoryButtons to displayCategoryOptions function
        # for category, button in self.frame.categoryButtons.items():
        #     button.config(command=lambda c=category: self.displayCategoryOptions(c)) 
        

    def updateCategories(self):
        menu = self.model.menu.getMenu()
        self.frame.createMenuCategories(menu) # running this view function again to load it with the updated category list

    def home(self) -> None:
        self.view.switch("home")
    
    def modify(self):
        order = self.frame.order
        self.model.order.saveOrder(order)
        self.view.switch("order-modify")
    
    def updateOrder(self):
        order = self.model.order.getSavedOrder()
        self.frame.setOrder(order)
        self.frame.updateOrderSummary()

    # def displayCategoryOptions(self, category):
    #     print(f"Displaying options for category: {category}")
    #     options = self.model.menu.getMenuItemsForCategory(category)
    #     self.frame.displayCategoryOptions(category, options)

    # def login(self) -> None:
    #     staffId = self.frame.staffId_entry.get() #getting staffID
    #     password = self.frame.password_entry.get() # getting Password
    #     self.frame.password_entry.delete(0, last=len(password))
    #     self.model.auth.login(staffId,password)
