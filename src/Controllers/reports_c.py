'''
Author: Niel Paraggua
Date: 18/12/2023
Version: 1.0
'''

from Models.main_m import Model
from Views.main_v import View
import re
from Class.profit_reports import PDFProfit
from datetime import datetime
from tkinter import messagebox


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
                self.restName = f"Restaurant: {self.model.reports.getRestName(self.current_user.getRestrantID())}"
            else:
                self.restName = "Restaurant: All"
         
    
        #gets the order totals for each day the total dates and the total for all days to be placed in graph
        self.orderstotals,self.ordersdates, self.fullTotalRev = self.model.reports.getGraphData(self.frame.startDateEnrty.get(),self.frame.endDateEntry.get(),self.restaurantID)
        
        self.frame.totalSalesLabel.config(text=f"Total revenue: £{self.fullTotalRev}")
        #puts data in graph
        try:
            self.frame.dowloadReport_btn.forget()
            self.frame.update_graph(self.ordersdates, self.orderstotals, self.restaurantID)
            self.frame.dowloadReport_btn.config(command=self.generateRestaurantReport)
        except AttributeError:
            self.frame.update_graph(self.ordersdates, self.orderstotals, self.restaurantID)
            self.frame.dowloadReport_btn.config(command=self.generateRestaurantReport)
        
    def generateRestaurantReport(self):
        pdf = PDFProfit()
        self.title = 'Restaurant Preformace Report'
        self.date = f'Date: {datetime.today().strftime("%Y-%m-%d")}'
        self.name = f'User: {self.current_user.getName()}'
        pdf.add_page()
        pdf.subHeader(self.title,self.date,self.name)
        pdf.add_line_graph_to_pdf(self.ordersdates,self.orderstotals)
        pdf.sales_record(self.ordersdates,self.orderstotals)
        pdf.output(f'Restaurant-Report-{datetime.today().strftime("%Y-%m-%d")}.pdf', 'F')
        messagebox.showinfo("Sucsess", f"Restaurant-Report-{datetime.today().strftime('Y-%m-%d')}.pdf has been sucsessfully generated")
    
    def staffreport(self):
        self.frame.showStaffReports()
        self.frame.dowloadReport_btn.config(command=self.generateStaffReport)
        #gets all staff reports data and put it in correct tables
        if(self.current_user.getAccountType() == "MANAGER"):
            self.staffProfits = self.model.reports.getStaffProfit(self.current_user.getRestrantID())
            self.staffOrders = self.model.reports.getStaffOrders(self.current_user.getRestrantID())
            self.frame.insertIntoStaffProfit(self.staffProfits)
            self.frame.insertIntoStaffOrder(self.staffOrders)
            self.restName = f"Restaurant: {self.model.reports.getRestName(self.current_user.getRestrantID())}"
        else:
            self.staffProfits = self.model.reports.getStaffProfit()
            self.staffOrders = self.model.reports.getStaffOrders()
            self.frame.insertIntoStaffProfit(self.staffProfits)
            self.frame.insertIntoStaffOrder(self.staffOrders)
            self.restName = "Restaurant: All"
            
    def generateStaffReport(self):
        pdf = PDFProfit()
        self.title = 'Staff Preformace Report'
        self.date = f'Date: {datetime.today().strftime("%Y-%m-%d")}'
        self.name = f'User: {self.current_user.getName()}'
        pdf.add_page()
        pdf.subHeader(self.title,self.date,self.name)
        pdf.profit_title()
        pdf.profit_record(self.staffProfits,self.restName)
        pdf.order_title()
        pdf.order_record(self.staffOrders, self.restName)
        pdf.output(f'Staff-Report-{datetime.today().strftime("%Y-%m-%d")}.pdf', 'F')
        messagebox.showinfo("Sucsess", f"Staff-Report-{datetime.today().strftime('%Y-%m-%d')}.pdf has been sucsessfully generated")
        
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

    
