from Models.main import Model
from Views.main import View


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self) -> None:
        #Binds controller functions with respective buttons in the view
        self.frame.createReservation_btn.config(command=self.createReservation)
        self.frame.createOrder_btn.config(command=self.createOrder)
        self.frame.viewOrders_btn.config(command=self.viewOrders)
        self.frame.modifyOrders_btn.config(command=self.modifyOrders)
        self.frame.adminFeatures_btn.config(command=self.adminFeatures)
        self.frame.reports_btn.config(command=self.reports)

    #button functions
    def createReservation(self) -> None:
        print("Reservation button clicked")#
        
    def createOrder(self) -> None:   
        print("Take Order button clicked")
        
    def viewOrders(self) -> None:
        print("View Orders button clicked")
        
    def modifyOrders(self) -> None:
        print("Modify Orders button clicked")
        
    def adminFeatures(self) -> None:
        print("Admin Features button clicked")
        
    def reports(self) -> None:
        print("Reports button clicked")

    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f" User: {current_user.getName()} ")
            self.frame.user_id.config(text=f" ID: {current_user.getStaffId()} ")
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
            
