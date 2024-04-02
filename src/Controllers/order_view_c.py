
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
        self.frame.setOrderCancelCallback(self.cancelOrder)
        self.frame.setOrderModifyCallback(self.modifyOrder)
       
        
        

    def _bind(self) -> None:
        # Binds controller functions with respective buttons in the view
        self.frame.homeButton.config(command=self.home)
        self.frame.refresh_button.config(command=self.updateOrders)
        self.frame.doneButton.config(command=self.orderComplete)
        self.frame.cancelButton.config(command=self.cancelOrder)
        self.frame.modifyButton.config(command=self.modifyOrder)
        
        

        
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
    
    def cancelOrder(self, table_number):
        current_user = self.model.auth.current_user
        if current_user:
            confirmation=messagebox.askquestion('Log off', 'Are you sure, you want to cancel this order?')
            if confirmation == 'yes':
                self.model.orderView.cancelOrder(current_user.getRestrantID(),table_number.strip("Table")[1])
                self.updateOrders()
                print("SELECTED ORDER ID: ", table_number)
                
    def modifyOrder(self, table_number):
        if table_number.startswith("Table "):
            self.table_num = table_number[len("Table "):].strip()  # Store table_num
        else:
            self.table_num = table_number.strip()

        order_details = self.model.orderView.getSingleOrder(self.model.auth.current_user.getRestrantID(), self.table_num)

        data_to_insert = []
        for orderID, details in order_details.items():
            item = details[0]  
            quantity = details[1] 
            description = details[2] if len(details) > 2 else ""  
            data_to_insert.append((orderID, item, quantity, description))

        self.frame.modifyOrderPopUp(data_to_insert)
        self.frame.tree.bind("<Double-1>", self.onDoubleClick)

        
    def onDoubleClick(self, event):
        self.rowId = self.frame.tree.identify_row(event.y)
        self.columnId = self.frame.tree.identify_column(event.x)

        if self.rowId and self.columnId:
            self.column_index = int(self.columnId[1:]) - 1
            if self.column_index == 0 or self.column_index == 1:
                messagebox.showinfo("Error", "You cannot edit this column.")
            else:
                self.currentValues = list(self.frame.tree.item(self.rowId, 'values'))
                self.orderID = self.currentValues[0]  
                self.frame.editWindowPopup(self.rowId, self.columnId)
                self.frame.saveEditButton.config(command=lambda: self.saveNewValue(self.orderID))

    def saveNewValue(self, orderID):
        newValue = self.frame.newValueUI.get()
        self.model.orderView.updateOrder(self.column_index, newValue, self.model.auth.current_user.getRestrantID(), self.table_num, orderID)
        self.frame.editWindow.destroy()
        self.frame.modifyOrderWindow.destroy()
        self.updateOrders()
        self.modifyOrder(self.table_num)


        
        
