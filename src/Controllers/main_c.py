from Models.main_m import Model
from Models.auth_m import Auth
from Models.order_m import Order
from Views.main_v import View

from .home_c import HomeController
from .login_c import LoginController
from .order_c import OrderController
from .order_modify_c import OrderModifyController
from .admin_c import AdminController
from .order_view_c import OrderViewController
from .reservations_c import ReservationsController
from .inventory_modify_c import InventoryModifyController
from .inventory_c import InventoryController


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.signin_controller = LoginController(model, view)
        self.home_controller = HomeController(model, view)
        self.order_controller = OrderController(model, view)
        self.order_modify_controller = OrderModifyController(model, view)
        self.admin_controller = AdminController(model, view)
        self.order_view_controller = OrderViewController(model, view)
        self.reservation_controller = ReservationsController(model,view)
        self.inventory_modify_controller = InventoryModifyController(model, view)
        self.inventory_controller = InventoryController(model, view)

        self.model.auth.add_event_listener("auth_changed", self.auth_state_listener)
        self.model.order.add_event_listener("order_saved", self.update_order_in_modify_page)

    def auth_state_listener(self, data: Auth) -> None:
        if data.is_logged_in:
            self.home_controller.update_view()
            self.admin_controller.update_view()
            self.reservation_controller.update_view()
            self.inventory_modify_controller.update_view()
            self.inventory_controller.update_view()
            self.view.switch("home")
        else:
            self.view.switch("login")
    
    def update_order_in_modify_page(self, data: Order):
        self.order_modify_controller.updateOrder()
        self.order_controller.updateOrder()

    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        if self.model.auth.is_logged_in:
            self.view.switch("home")
        else:
            self.view.switch("login")

        self.view.start_mainloop()