"""
File name: menu_edit_c.py
Author: Shahbaz Bokhari
Date created: 05/01/2024
"""
from tkinter import messagebox

from Models.main_m import Model
from Views.main_v import View

class MenuEditController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["menu-edit"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_btn.config(command=self.home)
    
    def home(self) -> None:
        self.view.switch("home")