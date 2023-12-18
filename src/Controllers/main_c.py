from Models.main_m import Model
from Models.auth_m import Auth
from Views.main_v import View

from .home_c import HomeController
from .login_c import LoginController
from .order import OrderController
from .admin_c import AdminController



class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.signin_controller = LoginController(model, view)
        self.home_controller = HomeController(model, view)
        self.order_controller = OrderController(model, view)
        self.admin_controller = AdminController(model, view)

        self.model.auth.add_event_listener("auth_changed", self.auth_state_listener)

    def auth_state_listener(self, data: Auth) -> None:
        if data.is_logged_in:
            self.home_controller.update_view()
            self.admin_controller.update_view()
            self.view.switch("home")
        else:
            self.view.switch("login")

    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        if self.model.auth.is_logged_in:
            self.view.switch("home")
        else:
            self.view.switch("login")

        self.view.start_mainloop()