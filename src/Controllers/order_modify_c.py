"""
File name: order_c.py
Author: Shahbaz
Date created: 17/12/2023
"""

from Models.main_m import Model
from Views.main_v import View

class OrderModifyController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["order-modify"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.homeButton.config(command=self.home)
        self.frame.continue_btn.config(command=self.order)
        self.frame.Cancel_btn.config(command=self.cancelChanges)

    def home(self) -> None:
        self.view.switch("home")
    
    def order(self):
        print("\nChanges made to order")
        modifiedOrder = self.frame.getOrder()
        print(modifiedOrder)
        self.model.order.saveOrder(modifiedOrder)
        self.view.switch("order")
    
    def cancelChanges(self):
        print("\nChanges cancelled\n")
        originalOrder = self.frame.getOriginalOrder()
        self.model.order.saveOrder(originalOrder)
        self.view.switch("order")
    
    def updateOrder(self):
        order = self.model.order.getSavedOrder()
        self.frame.setOrder(order)
        self.frame.updateItemList()
