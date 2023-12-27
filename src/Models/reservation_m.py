from .base_m import ObservableModel
from .restaurant import Reservation
import datetime
from database import dbfunc


# Mock data


class ReservationManager(ObservableModel):
    
    def createReservation(self,restaurantName,customerName,customerNumber,partySize,date,time,employeeID):
        if(self.checkAvailability(date,time)):
            self.reservationID = self.getReservationID()
            self.CreateReservationArray
            self.reservationsManager.append(Reservation(self.reservationID, restaurantName,customerName,customerNumber,partySize
                                                        ,1,employeeID,datetime.now(),date,time))
            
            
            
        
    def checkAvailability(self,reservationDate,reservationTime):
        # Calculate the start and end times
        self.beforeReservationTime = reservationTime - datetime.timedelta(hours=1)
        self.afterReservationTime = reservationTime + datetime.timedelta(hours=1)

        # Format the times as strings in the format MySQL expects
        self.beforeReservationTime = self.beforeReservationTime.strftime("%H:%M:%S")
        self.afterReservationTime = self.afterReservationTime.strftime("%H:%M:%S")
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("SELECT * FROM reservation WHERE reservation_date = %s \
                AND reservation_time BETWEEN (%s) AND (%s);", (reservationDate,self.beforeReservationTime,self.afterReservationTime))
                if(dbcursor.rowcount > 0): # this means there is reservations takeing those time slots and so the table is not avalible
                    dbcursor.close()
                    conn.close() 
                    return False
                else:
                    dbcursor.close()
                    conn.close() 
                    return True
    
    def getReservationID(self):
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("SELECT * FROM reservation ORDER BY reservation_id;")
                self.highestID = dbcursor.fetchone # grabs the highest id number or most resent reservation
                dbcursor.close()
                conn.close()
                return(self.highestID[0] + 1) #adds one to id as this is how it will be store in database
            
    def CreateReservationArray(self):
        self.reservationsManager = []
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("SELECT * FROM reservation")
                self.reservationsList = dbcursor.fetchall # grabs the all reservations
                if(dbcursor.rowcount > 0):
                     for reservation in self.reservationList:
                        self.reservationsManager.append(Reservation(reservation[0],reservation[1],reservation[2], reservation[3], reservation[4], 
                                                                    reservation[5], reservation[6], reservation[7], reservation[8], reservation[9],reservation[10]))
                dbcursor.close()
                conn.close()
                
        

