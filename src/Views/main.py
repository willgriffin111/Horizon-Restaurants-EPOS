from typing import TypedDict

from .root import Root
from .home import HomeView
from .login import LoginView
from .order import OrderView



class Frames(TypedDict):
    signin: LoginView
    home: HomeView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(LoginView, "login")
        self._add_frame(HomeView, "home")
        self._add_frame(OrderView, "order")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()