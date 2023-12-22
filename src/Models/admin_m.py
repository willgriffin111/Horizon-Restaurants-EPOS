'''
Author: Alex Rogers
Date: 18/12/2023
Version: 1.1
'''

from typing import TypedDict, Union
from .base_m import ObservableModel
from database import dbfunc




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
        