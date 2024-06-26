'''
Author: Alex Rogers
Date: 22/12/2023
Version: 1.1
'''

from typing import TypedDict, Union
from .base_m import ObservableModel
from database import dbfunc
from passlib.hash import sha256_crypt
import re
from tkinter import messagebox



class Admin(ObservableModel):
    
    #gets list of all empoyees
    def get_employee_list(self) -> None:
        print('Getting Emyploee Data')
        error = "" #reseting error           
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                  
            if conn.is_connected(): #Checking if connection is established                        
                print('MySQL Connection is established')                          
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("SELECT * FROM employee;")                                             
                employeeData = dbcursor.fetchall()
                if dbcursor.rowcount < 1: #this means no staff exists                         
                    error = "No staff found"
                else:                            
                    dbcursor.close()
                    conn.close()
                    return(employeeData)
                
        if(error != ""):
            messagebox.showerror("Error", error)
            return(None)
        
    def add_new_staff(self,staffName,staffType,staffPass,restaurantID) -> None:
        staffPass = sha256_crypt.hash(staffPass)
        restaurantID = re.search('\(([^)]+)\)', restaurantID)
        restaurantID = restaurantID.group(1)
        if staffType == "ADMIN" or staffType == "DIRECTOR" or staffType == "CHEF" or staffType == "MANAGER" or staffType == "KITCHEN" or staffType == "FRONT":
            print('Adding New Staff')          
            conn = dbfunc.getConnection() 
            if conn != None:    #Checking if connection is None                  
                if conn.is_connected(): #Checking if connection is established                        
                    print('MySQL Connection is established')                          
                    dbcursor = conn.cursor()    #Creating cursor object                                                 
                    dbcursor.execute("INSERT INTO employee (employee_name, employee_account_type, \
                                    employee_password, restaurant_id) VALUES (%s, %s, %s, %s)", (staffName, staffType, staffPass, restaurantID))                                        
                    conn.commit() 
                    messagebox.showinfo("Sucsess", "User created sucsesfully.")
                    dbcursor.close()       
                    conn.close()
        else:
            messagebox.showerror("ERROR","User type must be one of the following; ADMIN,DIRECTOR,CHEF,MANAGER,KITCHEN or FRONT")
                
    def remove_staff(self,staffId) -> None:
        print('Removeing Staff')          
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                  
            if conn.is_connected(): #Checking if connection is established                        
                print('MySQL Connection is established')                          
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("DELETE FROM employee WHERE employee_id = "+str(staffId)+";")                                        
                conn.commit() 
                messagebox.showinfo("Sucsess", "User removed sucsesfully.")
                dbcursor.close()       
                conn.close()
                
    def updateStaff(self, column_index, newValue, staffID): #updates the data from the reservations table
        #finding out what data type needs to be updated
        
        if column_index == 3:
            newValue = sha256_crypt.hash(newValue)
    
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object  
                #updates data
                #finding out what data type needs to be updated
                if column_index == 1:
                    dbcursor.execute('UPDATE employee SET employee_name = %s WHERE employee_id = %s;', (newValue,staffID)) 
                    messagebox.showinfo("Sucsess", "User name updated.")
                elif column_index == 2:
                    dbcursor.execute('UPDATE employee SET employee_account_type = %s WHERE employee_id = %s;', (newValue,staffID))
                    messagebox.showinfo("Sucsess", "User type updated.")
                elif column_index == 3:
                    dbcursor.execute('UPDATE employee SET employee_password = %s WHERE employee_id = %s;', (newValue,staffID))
                    messagebox.showinfo("Sucsess", "User password updated.")
                elif column_index == 4:
                    dbcursor.execute('UPDATE employee SET restaurant_id = %s WHERE employee_id = %s;', (newValue,staffID))   
                    messagebox.showinfo("Sucsess", "Restaurant ID updated.")                                            
                
                conn.commit()
                dbcursor.close()
                conn.close() 
                
    
        