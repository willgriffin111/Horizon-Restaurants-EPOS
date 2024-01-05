from Models.main_m import Model
from Views.main_v import View



class OrderViewController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["orderView"]
        self._bind()
        self.updateOrders()

    def _bind(self) -> None:
        # Binds controller functions with respective buttons in the view
        self.frame.homeButton.config(command=self.home)
        self.frame.refresh_button.config(command=self.updateOrders)
        self.frame.doneButton.config(command=self.orderComplete)
        
    def updateOrders(self):
        current_user = self.model.auth.current_user
        if current_user:
            tableOrders = self.model.orderView.getTableOrders(self.model.auth.current_user.getRestrantID()) 
            self.frame.create_main_frame(tableOrders)



    def home(self) -> None:
        self.view.switch("home")
    
    def orderComplete(self):
        self.frame.removeOrder()
        


