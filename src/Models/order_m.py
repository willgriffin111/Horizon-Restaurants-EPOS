""""
File name: order_m.py
Author: Shahbaz
Date Created: 18/12/2023
"""
from .base_m import ObservableModel


# Mock data


class Order(ObservableModel):
    def __init__(self):
        super().__init__()
        