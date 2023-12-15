from typing import TypedDict, Union
from .base import ObservableModel



class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.current_user = None

    def login(self, employee) -> None:
        self.is_logged_in = True
        self.current_user = employee #takes employee class with all stored info 
        self.trigger_event("auth_changed")

    def logout(self) -> None:
        self.is_logged_in = False
        self.current_user = None
        self.trigger_event("auth_changed")
