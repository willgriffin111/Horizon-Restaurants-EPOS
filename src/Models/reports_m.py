'''
Author: Niel Paraggua
Date: 18/12/2023
Version: 1.0
'''

from typing import TypedDict, Union
from .base_m import ObservableModel
from passlib.hash import sha256_crypt
from Class.EmployeeClass import EmployeeAccount
from database import dbfunc
from tkinter import messagebox
import datetime



class Reports(ObservableModel):
    def __init__(self):
        super().__init__()
        
    def getGraphData(self, dateStart, dateEnd, SelectedRest):
        print("getting graph data")
        self.totalRev = 0
        self.orderstotals = []
        self.ordersdates = []
        dateStart = self.formatdate(dateStart)
        dateEnd = self.formatdate(dateEnd)
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established   
                while dateStart < dateEnd: 
                    dbcursor = conn.cursor() #Creating cursor object 
                    totalforday = 0 
                    
                    if (SelectedRest != "Show All Restaurants"):
                        dbcursor.execute("SELECT order_menu_item_qty, order_price FROM orders WHERE restaurant_id = %s \
                        AND order_time_created BETWEEN (%s) AND (%s);", (SelectedRest,dateStart,dateStart + datetime.timedelta(days=1)))
                        
                    else:  
                        dbcursor.execute("SELECT order_menu_item_qty, order_price FROM orders WHERE \
                        order_time_created BETWEEN (%s) AND (%s);", (dateStart,dateStart + datetime.timedelta(days=1)))   
                                                         
                    self.orderList = dbcursor.fetchall()
                    
                    for order in self.orderList:
                        totalforday += float(order[1]) * float(order[0])
                        
                    self.totalRev += totalforday 
                    self.orderstotals.append(totalforday)
                    self.ordersdates.append(dateStart)
                    dateStart += datetime.timedelta(days=1)
                    
                    dbcursor.close()
                conn.close() 
                
                return(self.orderstotals,self.ordersdates,self.totalRev)
            
    def formatdate(self,date):
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            return(date)
        except:
            messagebox.showerror("Error", "Date should be in format Year-Month-Day e.g. 2024-12-12")
            
    def getStaffProfit(self, SelectedRest = None):
        print("getting staff sales")
        self.stafflist = []
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established
                dbcursor = conn.cursor() #Creating cursor object   
                if (SelectedRest != None):
                    dbcursor.execute(f"SELECT * FROM employee WHERE restaurant_id = {SelectedRest};")
                else:  
                    dbcursor.execute("SELECT * FROM employee;")  
                                                        
                self.employeeList = dbcursor.fetchall()
                
                for employee in self.employeeList:
                    totalforstaff = 0 
                    dbcursor.execute(f"SELECT order_menu_item_qty, order_price FROM orders WHERE order_author = {employee[0]};")  
                    
                    self.orderList = dbcursor.fetchall()
                    
                    for order in self.orderList:
                        totalforstaff += float(order[1]) * float(order[0])
                        
                    self.stafflist.append([str(employee[0]),str(employee[2]),str(employee[3]),str(totalforstaff)])
                    
                dbcursor.close()
                conn.close() 
                
                return(self.stafflist)
    
    def getStaffOrders(self, SelectedRest = None):
        print("getting staff orders")
        self.stafflist = []
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established
                dbcursor = conn.cursor() #Creating cursor object   
                if (SelectedRest != None):
                    dbcursor.execute(f"SELECT * FROM employee WHERE restaurant_id = {SelectedRest};")
                else:  
                    dbcursor.execute("SELECT * FROM employee;")  
                                                        
                self.employeeList = dbcursor.fetchall()
                
                for employee in self.employeeList:
                    totalforstaff = 0 
                    dbcursor.execute(f"SELECT order_menu_item_qty, order_price FROM orders WHERE order_author = {employee[0]};")  
        
                    dbcursor.fetchall()
                        
                    self.stafflist.append([str(employee[0]),str(employee[2]),str(employee[3]),str(dbcursor.rowcount)])
                    
                dbcursor.close()
                conn.close() 
                
                return(self.stafflist)
            
    def getRestName(self,SelectedRest):
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established
                dbcursor = conn.cursor() #Creating cursor object   
                dbcursor.execute(f"SELECT * FROM restaurant WHERE restaurant_id = {SelectedRest};")
                self.restaurant_data = dbcursor.fetchone()
                return self.restaurant_data[2]
                