from .base_m import ObservableModel
from datetime import datetime
from database import dbfunc




class ReservationManager(ObservableModel):

    #creates the reservation with inserted data
    def createReservation(self,restaurantID,customerName,customerNumber,partySize,date,time,employeeID):
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("INSERT INTO reservation (restaurant_id, reservation_customer_name, reservation_customer_phone, \
                                 reservation_party_size, reservation_author, reservation_creation_time, reservation_date,\
                                     reservation_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (restaurantID, customerName, customerNumber,
                                                                                                  partySize, employeeID,datetime.now(), datetime.strptime(date, '%d/%m/%Y'), datetime.strptime(time, "%H:%M"))) 
                conn.commit()
                dbcursor.close()
                conn.close() 
                print("reservation created")
            
    def updateReservation(self, column_index, newValue, reservationID): #updates the data from the reservations table
        #finding out what data type needs to be updated
        if column_index == 1:
            self.columnName = 'reservation_customer_name'
        elif column_index == 2:
            self.columnName = 'reservation_customer_phone'
        elif column_index == 4:
            self.columnName = 'reservation_date'
        elif column_index == 5:
            self.columnName = 'reservation_time'
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object  
                #updates data
                #finding out what data type needs to be updated
                if column_index == 1:
                    dbcursor.execute('UPDATE reservation SET reservation_customer_name = %s WHERE reservation_id = %s;', (newValue,reservationID)) 
                elif column_index == 2:
                    dbcursor.execute('UPDATE reservation SET reservation_customer_phone = %s WHERE reservation_id = %s;', (newValue,reservationID))
                elif column_index == 4:
                    dbcursor.execute('UPDATE reservation SET reservation_date = %s WHERE reservation_id = %s;', (datetime.strptime(newValue, '%d/%m/%Y'),reservationID))
                elif column_index == 5:
                    dbcursor.execute('UPDATE reservation SET reservation_time = %s WHERE reservation_id = %s;', (datetime.strptime(newValue, "%H:%M"),reservationID))                                               
                
                conn.commit()
                dbcursor.close()
                conn.close() 
    
    def cancelReservation(self, reservationID):
        #cancels a specific reservation by its ID number
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()
                dbcursor.execute('DELETE FROM reservation WHERE reservation_id = '+str(reservationID)+';')
                conn.commit()
                dbcursor.close()
                conn.close() 
            
            
    def getReservations(self, restaurantID = None): #gets the reservations made and formats them for the reservations table
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object 
                if restaurantID == None:                                            
                    dbcursor.execute("SELECT reservation_id, reservation_customer_name, reservation_customer_phone, restaurant_id, reservation_date, reservation_time FROM reservation;")    
                else:
                    dbcursor.execute("SELECT reservation_id, reservation_customer_name, reservation_customer_phone, restaurant_id, reservation_date, reservation_time FROM reservation WHERE reservation_id = "+str(restaurantID)+";")                                       
                self.reservationlist = dbcursor.fetchall()
                dbcursor.close()
                conn.close() 
        return(self.reservationlist)
    
    def getRestaurantNames(self):
        self.restaurantNames = []
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("SELECT restaurant_id, restaurant_name FROM restaurant;")                                           
                self.restaurantList = dbcursor.fetchall()
                for restaurant in self.restaurantList:
                    self.tempRestaurantName = str(restaurant[1]) + "("+ str(restaurant[0]) +")"
                    self.restaurantNames.append(self.tempRestaurantName)
                dbcursor.close()
                conn.close() 
        return(self.restaurantNames)
            
            
        
    # def checkAvailability(self,reservationDate,reservationTime):
    #     # Calculate the start and end times
    #     self.beforeReservationTime = reservationTime - datetime.timedelta(hours=1)
    #     self.afterReservationTime = reservationTime + datetime.timedelta(hours=1)

    #     # Format the times as strings in the format MySQL expects
    #     self.beforeReservationTime = self.beforeReservationTime.strftime("%H:%M:%S")
    #     self.afterReservationTime = self.afterReservationTime.strftime("%H:%M:%S")
    #     conn = dbfunc.getConnection() 
    #     if conn != None:    #Checking if connection is None                    
    #         if conn.is_connected(): #Checking if connection is established  
    #             dbcursor = conn.cursor()    #Creating cursor object                                                 
    #             dbcursor.execute("SELECT * FROM reservation WHERE reservation_date = %s \
    #             AND reservation_time BETWEEN (%s) AND (%s);", (reservationDate,self.beforeReservationTime,self.afterReservationTime))
    #             if(dbcursor.rowcount > 0): # this means there is reservations takeing those time slots and so the table is not avalible
    #                 dbcursor.close()
    #                 conn.close() 
    #                 return False
    #             else:
    #                 dbcursor.close()
    #                 conn.close() 
    #                 return True
    
            
  
                
        

