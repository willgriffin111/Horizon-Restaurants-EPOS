'''
Author: Alex Rogers
Date: 22/12/2023
Version: 1.1
'''

from typing import TypedDict, Union
from .base_m import ObservableModel
from database import dbfunc
from passlib.hash import sha256_crypt



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
            print(error)
            return(employeeData)
        
    def add_new_staff(self,staffName,staffType,staffPass) -> None:
        staffPass = sha256_crypt.hash(staffPass)
        print('Adding New Staff')          
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                  
            if conn.is_connected(): #Checking if connection is established                        
                print('MySQL Connection is established')                          
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("INSERT INTO employee (employee_name, employee_account_type, \
                                 employee_password) VALUES (%s, %s, %s)", (staffName, staffType, staffPass))                                        
                conn.commit() 
                print("User created sucsesfully")
                dbcursor.close()       
                conn.close()
                
    def remove_staff(self,staffId) -> None:
        print('Removeing Staff')          
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                  
            if conn.is_connected(): #Checking if connection is established                        
                print('MySQL Connection is established')                          
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("DELETE FROM employee WHERE employee_id = "+str(staffId)+";")                                        
                conn.commit() 
                print("User removed sucsesfully")
                dbcursor.close()       
                conn.close()
        