from Models.main_m import Model
from Views.main_v import View
from tkinter import messagebox


class OrderViewController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["orderView"]
        self._bind()
        self.updateOrders()
        self.frame.setOrderCompleteCallback(self.orderComplete)

    def _bind(self) -> None:
        # Binds controller functions with respective buttons in the view
        self.frame.homeButton.config(command=self.home)
        self.frame.refresh_button.config(command=self.updateOrders)
        self.frame.doneButton.config(command=self.orderComplete)
        
    def update_view(self)-> None:
        self.updateOrders()
        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f" User: {current_user.getName()} ")
            self.frame.user_id.config(text=f" ID: {current_user.getStaffId()} ")
        else:
            self.frame.staff_name.config(text=f"Hey, Name ")
            self.frame.staff_id.config(text=f"ID: 12345678 ")
            
    def updateOrders(self):
        current_user = self.model.auth.current_user
        if current_user:
            tableOrders = self.model.orderView.getTableOrders(self.model.auth.current_user.getRestrantID()) 
            self.frame.create_main_frame(tableOrders)



    def home(self) -> None:
        self.view.switch("home")
    
    
    def orderComplete(self, table_number):
        current_user = self.model.auth.current_user
        if current_user:
            confirmation=messagebox.askquestion('Log off', 'Are you sure, you want to mark this order as complete?')
            if confirmation == 'yes':
                self.model.orderView.completeOrder(current_user.getRestrantID(),table_number.strip("Table")[1])
                self.updateOrders()
                print("SELECTED ORDER ID: ", table_number)

        


