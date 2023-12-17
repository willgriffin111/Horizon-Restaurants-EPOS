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
        self.view.switch("order")
        
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
            userType = current_user.getAccountType()
            if(userType == 'ADMIN'):
                #displaying admin buttons
                self.frame.createReservation_btn.grid(row=0, column=0, padx=10, pady=10)
                self.frame.createOrder_btn.grid(row=0, column=1, padx=10, pady=10)
                self.frame.viewOrders_btn.grid(row=0, column=2, padx=10, pady=10)
                self.frame.modifyOrders_btn.grid(row=1, column=0, padx=10, pady=10)
                self.frame.adminFeatures_btn.grid(row=1, column=1, padx=10, pady=10)
                self.frame.reports_btn.grid(row=1, column=2, padx=10, pady=10)
            elif(userType == 'DIRECTOR'):
                #displaying director buttons
                self.frame.createReservation_btn.grid_forget()
                self.frame.createOrder_btn.grid_forget()
                self.frame.viewOrders_btn.grid_forget()
                self.frame.modifyOrders_btn.grid_forget()
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.reports_btn.grid(row=1, column=2, padx=10, pady=10)
            elif(userType == 'MANAGER'):
                #displaying manager buttons
                self.frame.createReservation_btn.grid(row=0, column=0, padx=10, pady=10)
                self.frame.createOrder_btn.grid(row=0, column=1, padx=10, pady=10)
                self.frame.viewOrders_btn.grid(row=0, column=2, padx=10, pady=10)
                self.frame.modifyOrders_btn.grid(row=1, column=0, padx=10, pady=10)
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.reports_btn.grid(row=1, column=1, padx=10, pady=10)
            elif(userType == 'CHEF'):
                #displaying chef buttons (temp)
                self.frame.createReservation_btn.grid_forget()
                self.frame.createOrder_btn.grid_forget()
                self.frame.viewOrders_btn.grid_forget()
                self.frame.modifyOrders_btn.grid_forget()
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.reports_btn.grid(row=1, column=2, padx=10, pady=10)
            elif(userType == 'KITCHEN'):
                #displaying kitchen staff buttons
                self.frame.createReservation_btn.grid_forget()
                self.frame.createOrder_btn.grid_forget()
                self.frame.viewOrders_btn.grid(row=0, column=0, padx=10, pady=10)
                self.frame.modifyOrders_btn.grid(row=0, column=1, padx=10, pady=10)
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.reports_btn.grid_forget()
            elif(userType == 'FRONT'):
                #displaying front buttons
                self.frame.createReservation_btn.grid(row=0, column=0, padx=10, pady=10)
                self.frame.createOrder_btn.grid(row=0, column=1, padx=10, pady=10)
                self.frame.viewOrders_btn.grid_forget()
                self.frame.modifyOrders_btn.grid(row=0, column=2, padx=10, pady=10)
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.reports_btn.grid_forget()
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
            self.frame.createReservation_btn.grid_forget()
            self.frame.createOrder_btn.grid_forget()
            self.frame.viewOrders_btn.grid_forget()
            self.frame.modifyOrders_btn.grid_forget()
            self.frame.adminFeatures_btn.grid_forget()
            self.frame.reports_btn.grid_forget()
            
