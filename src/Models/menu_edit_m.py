"""
File name: menu_edit_m.py
Author: Shahbaz Bokhari
Date Created: 05/01/2024
"""

from .base_m import ObservableModel
from database import dbfunc

class MenuEdit(ObservableModel):
    def __init__(self):
        super().__init__()