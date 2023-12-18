from typing import TypedDict

from .root_v import Root
from .home_v import HomeView
from .login_v import LoginView
from .order import OrderView
from .admin_v import AdminView



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
        self._add_frame(OrderView, "order")
        self._add_frame(AdminView, "admin")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()