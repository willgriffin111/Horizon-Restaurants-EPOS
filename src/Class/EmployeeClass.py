#employee class ill put this somewhere later
import mysql.connector 
from database import dbfunc

class EmployeeAccount:
    def __init__(self, id, restrant, name, type):
        self.__name = name
        self.__staffId = id
        self.__accountType = type
        self.__restrantID = restrant
    
    #Getters
    def getStaffId(self):
        return self.__staffId
    
    def getName(self):
        return self.__name
    
    def getAccountType(self):
        return self.__accountType
    
    def getRestrantID(self):
        return self.__restrantID
    
    #update functions
    def updatePassword(self,newpass):
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("UPDATE employee SET employee_password = %s WHERE employee_id = %s;", (newpass,self.getStaffId())) 
                conn.commit()
                dbcursor.close()
                conn.close() 
    
    def updateAccountType(self,acctype):
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("UPDATE employee SET employee_account_type = %s WHERE employee_id = %s;", (acctype,self.getStaffId())) 
                conn.commit()
                dbcursor.close()
                conn.close()
    
    def updateName(self,name):
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("UPDATE employee SET employee_name = %s WHERE employee_id = %s;", (name,self.getStaffId())) 
                conn.commit()
                dbcursor.close()
                conn.close()
                self.__name = name
        