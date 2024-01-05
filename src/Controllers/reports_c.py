'''
Author: Alex Rogers
Date: 18/12/2023
Version: 1.0
'''

from Models.main_m import Model
from Views.main_v import View
import re

class ReportController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["reports"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.homeBtn.config(command=self.home_btn)
        self.frame.salesReportsBtn.config(command=self.salesreport)
        self.frame.staffReportsBtn.config(command=self.staffreport)
        
        
    def salesreport(self):
        self.RestaurantOptions = ["Show All Restaurants"]
        for Names in self.model.reservation.getRestaurantNames():
            self.RestaurantOptions.append(Names)
        self.frame.showSalesReports(self.RestaurantOptions)
        self.frame.updateGraphButton.config(command=self.update_graph) 
        if(self.current_user.getAccountType() == "MANAGER"):
            self.frame.restaurantDropdown.forget()
        
    def update_graph(self):
        
        if(self.current_user.getAccountType() == "MANAGER"):
            self.restaurantID = self.current_user.getRestrantID()
        else:
            #gets the restaurantID  and formats it
            self.restaurantID = self.frame.selectedRestaurnant.get()
            if(self.restaurantID != "Show All Restaurants"):
                self.restaurantID = re.search('\(([^)]+)\)', self.restaurantID)
                self.restaurantID = self.restaurantID.group(1)
         
    
        #gets the order totals for each day the total dates and the total for all days to be placed in graph
        self.orderstotals,self.ordersdates, self.fullTotalRev = self.model.reports.getGraphData(self.frame.startDateEnrty.get(),self.frame.endDateEntry.get(),self.restaurantID)
        
        self.frame.totalSalesLabel.config(text=f"Total revenue: £{self.fullTotalRev}")
        #puts data in graph
        self.frame.update_graph(self.ordersdates, self.orderstotals, self.restaurantID)
    
    def staffreport(self):
        self.frame.showStaffReports()
        
        if(self.current_user.getAccountType() == "MANAGER"):
            self.frame.insertIntoStaffProfit(self.model.reports.getStaffProfit(self.current_user.getRestrantID()))
            self.frame.insertIntoStaffOrder(self.model.reports.getStaffOrders(self.current_user.getRestrantID()))
        else:
            self.frame.insertIntoStaffProfit(self.model.reports.getStaffProfit())
            self.frame.insertIntoStaffOrder(self.model.reports.getStaffOrders())
        
    #home tab
    def home_btn(self) -> None:
        self.frame.cleargraph()
        self.view.switch("home")
        
     #update view
    def update_view(self) -> None:
        self.current_user = self.model.auth.current_user
        if self.current_user:
            self.frame.usernameLabel.config(text=f"User: {self.current_user.getName()} ")
            self.frame.userIdLabel.config(text=f"ID: {self.current_user.getStaffId()} ")
            self.salesreport()
        else:
            self.frame.staff_name.config(text=f"User: Name ")
            self.frame.staff_id.config(text=f"ID: 12345678 ")

    
