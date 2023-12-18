'''
Author: Alex Rogers
Date: 18/12/2023
Version: 1.0
'''

from Models.main_m import Model
from Views.main_v import View

class LoginController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["login"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.login_btn.config(command=self.login)

    def login(self) -> None:
        staffId = self.frame.staffId_entry.get() #getting staffID
        password = self.frame.password_entry.get() # getting Password
        self.frame.password_entry.delete(0, last=len(password))
        self.model.auth.login(staffId,password)
