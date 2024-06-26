'''
*    Title: How To Organize Multi-frame TKinter Application With MVC Pattern
*    Author: Nazmul Ahsan
*    Date: Jan 6, 2023
*    Code version: 1.0
*    Availability: https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
*
'''


from typing import TypedDict
from .root_v import Root
from .home_v import HomeView
from .login_v import LoginView
from .order_v import OrderCreate
from .order_modify_v import OrderModifyView
from .admin_v import AdminView
from .order_view_v import OrdersView
from .reservations_v import ReservationsView
from .inventory_modify_v import InventoryModifyView
from .inventory_v import InventoryView
from .account_v import AccountView
from .menu_edit_v import MenuEdit
from .reports_v import ReportView
from .discount_v import DiscountView


class Frames(TypedDict):
    signin: LoginView
    home: HomeView
    admin: AdminView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(LoginView, "login")
        self._add_frame(HomeView, "home")
        self._add_frame(ReservationsView, "reservations")
        self._add_frame(OrdersView, "orderView")
        self._add_frame(OrderCreate, "order")
        self._add_frame(OrderModifyView, "order-modify")
        self._add_frame(AdminView, "admin")
        self._add_frame(InventoryModifyView, "inventory-modify")
        self._add_frame(InventoryView, "inventory")
        self._add_frame(AccountView, "account")
        self._add_frame(MenuEdit, "menu-edit")
        self._add_frame(ReportView, "reports")
        self._add_frame(DiscountView, "discount")
        

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str, data=None) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()