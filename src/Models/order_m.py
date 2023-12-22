""""
File name: order_m.py
Author: Shahbaz
Date Created: 18/12/2023
"""
from .base_m import ObservableModel
import copy

# Mock data


class Order(ObservableModel):
    def __init__(self):
        super().__init__()
        self.order = {}
    
    def saveOrder(self, order):
        self.order = copy.deepcopy(order)
        self.trigger_event("order_saved")
    
    def getSavedOrder(self):
        return self.order
