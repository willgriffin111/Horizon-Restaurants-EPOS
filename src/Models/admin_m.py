'''
Author: Alex Rogers
Date: 18/12/2023
Version: 1.1
'''

from typing import TypedDict, Union
from .base_m import ObservableModel




class Admin(ObservableModel):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.current_user = None

    def login(self, staffId, password) -> None:  
        print('login start 1.1')
        


    def logout(self) -> None:
        self.is_logged_in = False
        self.current_user = None
        self.trigger_event("auth_changed")