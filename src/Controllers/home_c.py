'''
Author: Alex Rogers
Date: 18/12/2023
Version: 1.0
'''

from Models.main_m import Model
from Views.main_v import View


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
        self.frame.inventory_modify_btn.config(command=self.inventory_modify)
        self.frame.inventory_btn.config(command=self.inventory)
        self.frame.adminFeatures_btn.config(command=self.adminFeatures)
        self.frame.reports_btn.config(command=self.reports)
        self.frame.Acc_btn.config(command=self.account)
        self.frame.menu_edit_btn.config(command=self.menu_edit)
        self.frame.discount_btn.config(command=self.discount)

    #button functions
    def createReservation(self) -> None:
        print("Reservation button clicked")
        self.view.switch("reservations")
        
    def createOrder(self) -> None:   
        print("Take Order button clicked")
        self.view.switch("order")
        
    def viewOrders(self) -> None:
        print("View Orders button clicked")
        self.view.switch("orderView")
        
    def inventory_modify(self) -> None:
        print("Inventory modify button clicked")
        self.view.switch("inventory-modify")
    
    def inventory(self):
        print("inventory button clicked")
        self.view.switch("inventory")
        
    def adminFeatures(self) -> None:
        print("Admin Features button clicked")
        self.view.switch("admin")
        
    def reports(self) -> None:
        print("Reports button clicked")
        self.view.switch("reports")
        
    def account(self)  -> None:
        print("Account button clicked")
        self.view.switch("account")
    
    def menu_edit(self):
        print("Menu Management button clicekd")
        self.view.switch("menu-edit")
    
    def discount(self):
        print("Discount Management button clicked")
        self.view.switch("discount")

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
                self.frame.inventory_modify_btn.grid(row=1, column=0, padx=10, pady=10)
                self.frame.inventory_btn.grid_forget()
                self.frame.adminFeatures_btn.grid(row=1, column=1, padx=10, pady=10)
                self.frame.reports_btn.grid(row=1, column=2, padx=10, pady=10)
                self.frame.discount_btn.grid(row=2, column=0, padx=10, pady=10)
                self.frame.menu_edit_btn.grid(row=2, column=1, padx=10, pady=10)
            elif(userType == 'DIRECTOR'):
                #displaying director buttons
                self.frame.createReservation_btn.grid_forget()
                self.frame.createOrder_btn.grid_forget()
                self.frame.viewOrders_btn.grid_forget()
                self.frame.inventory_modify_btn.grid_forget()
                self.frame.inventory_btn.grid_forget()
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.reports_btn.grid(row=1, column=2, padx=10, pady=10)
                self.frame.menu_edit_btn.grid_forget()
                self.frame.discount_btn.grid_forget()
            elif(userType == 'MANAGER'):
                #displaying manager buttons
                self.frame.createReservation_btn.grid(row=0, column=0, padx=10, pady=10)
                self.frame.createOrder_btn.grid(row=0, column=1, padx=10, pady=10)
                self.frame.viewOrders_btn.grid(row=0, column=2, padx=10, pady=10)
                self.frame.inventory_modify_btn.grid(row=1, column=0, padx=10, pady=10)
                self.frame.inventory_btn.grid_forget()
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.reports_btn.grid(row=1, column=1, padx=10, pady=10)
                self.frame.discount_btn.grid(row=1, column=2, padx=10, pady=10)
                self.frame.menu_edit_btn.grid_forget()
            elif(userType == 'CHEF'):
                #displaying chef buttons (temp)
                self.frame.createReservation_btn.grid_forget()
                self.frame.createOrder_btn.grid_forget()
                self.frame.viewOrders_btn.grid_forget()
                self.frame.inventory_modify_btn.grid_forget()
                self.frame.inventory_btn.grid_forget()
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.menu_edit_btn.grid(row=0, column=1, padx=10, pady=10)
                self.frame.discount_btn.grid_forget()
                self.frame.reports_btn.grid_forget()
            elif(userType == 'KITCHEN'):
                #displaying kitchen staff buttons
                self.frame.createReservation_btn.grid_forget()
                self.frame.createOrder_btn.grid_forget()
                self.frame.viewOrders_btn.grid(row=0, column=0, padx=10, pady=10)
                self.frame.inventory_modify_btn.grid_forget()
                self.frame.inventory_btn.grid(row=0, column=1, padx=10, pady=10)
                self.frame.menu_edit_btn.grid_forget()
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.discount_btn.grid_forget()
                self.frame.reports_btn.grid_forget()
            elif(userType == 'FRONT'):
                #displaying front buttons
                self.frame.createReservation_btn.grid(row=0, column=0, padx=10, pady=10)
                self.frame.createOrder_btn.grid(row=0, column=1, padx=10, pady=10)
                self.frame.inventory_btn.grid(row=0, column=2, padx=10, pady=10)
                self.frame.menu_edit_btn.grid_forget()
                self.frame.viewOrders_btn.grid_forget()
                self.frame.inventory_modify_btn.grid_forget()
                self.frame.adminFeatures_btn.grid_forget()
                self.frame.discount_btn.grid_forget()
                self.frame.reports_btn.grid_forget()
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
            self.frame.createReservation_btn.grid_forget()
            self.frame.createOrder_btn.grid_forget()
            self.frame.viewOrders_btn.grid_forget()
            self.frame.inventory_modify_btn.grid_forget()
            self.frame.inventory_btn.grid_forget()
            self.frame.adminFeatures_btn.grid_forget()
            self.frame.reports_btn.grid_forget()
            self.frame.menu_edit_btn.grid_forget()
            self.frame.discount_btn.grid_forget()

            
