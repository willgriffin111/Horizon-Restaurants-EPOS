from .base_m import ObservableModel
from datetime import datetime, timedelta
from database import dbfunc
from tkinter import messagebox
import datetime as dt




class ReservationModel(ObservableModel):

    def getDailyReservations(self, date, restaurantID):
        reservations = []
        try:
            conn = dbfunc.getConnection()
            if conn is not None and conn.is_connected():
                dbcursor = conn.cursor()
                query = """
                SELECT reservation_time, table_id, COUNT(*)
                FROM reservation
                WHERE restaurant_id = %s
                AND reservation_date = %s
                GROUP BY reservation_time, table_id
                ORDER BY reservation_time, table_id;
                """
                dbcursor.execute(query, (restaurantID, date))
                reservations = dbcursor.fetchall()
                dbcursor.close()
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()
        return reservations

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
            
    
    

    # creates the reservation with inserted data
    def createReservation(self,restaurantID,customerName, customerEmail,customerNumber,partySize,date,time,employeeID,tableNum):
        self.tableID = self.getTableID(tableNum, restaurantID)
        if self.tableID != None:
            date = self.formatdate(date)
            time = self.formattime(time)
            if(self.checkAvailability(date,time,self.tableID,restaurantID,partySize)):
                conn = dbfunc.getConnection() 
                if conn != None:    #Checking if connection is None                    
                    if conn.is_connected(): #Checking if connection is established  
                        dbcursor = conn.cursor()    #Creating cursor object                                                 
                        dbcursor.execute("INSERT INTO reservation (restaurant_id, reservation_customer_name, reservation_customer_email, reservation_customer_phone, \
                                        table_id, reservation_party_size, reservation_author, reservation_creation_time, reservation_date,\
                                            reservation_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (restaurantID, customerName, customerEmail, customerNumber, self.tableID,
                                                                                                        partySize, employeeID,datetime.now(), date, time)) 
                        conn.commit()
                        dbcursor.close()
                        conn.close() 
                        messagebox.showinfo("Sucsess", "Reservation created sucsessfully")
            else:
                messagebox.showerror("Error", "Table not available at that time.")
                
            
    def updateReservation(self, column_index, newValue, reservationID): #updates the data from the reservations table
        #finding out what data type needs to be updated
            
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object  
                #updates data
                #finding out what data type needs to be updated
                    
                if column_index == 2:
                    dbcursor.execute('UPDATE reservation SET reservation_customer_name = %s WHERE reservation_id = %s;', (newValue,reservationID))
                    messagebox.showinfo("Sucsess", "Name has been updated")
                elif column_index == 3:
                    dbcursor.execute('UPDATE reservation SET reservation_customer_email = %s WHERE reservation_id = %s;', (newValue,reservationID))
                    messagebox.showinfo("Sucsess", "Email has been updated")
                    
                elif column_index == 4:
                    dbcursor.execute('UPDATE reservation SET reservation_customer_phone = %s WHERE reservation_id = %s;', (newValue,reservationID))
                    messagebox.showinfo("Sucsess", "Phone number has been updated")
                    
                elif column_index == 5:
                    dbcursor.execute('UPDATE reservation SET reservation_party_size = %s WHERE reservation_id = %s;', (newValue, reservationID))
                    messagebox.showinfo("Success", "Party size has been updated")
                    
                elif column_index == 6:
                    dbcursor.execute("SELECT restaurant_id, table_id, reservation_time, reservation_party_size FROM reservation WHERE reservation_id = "+str(reservationID)+";")
                    reservation = dbcursor.fetchone()  
                    date = self.formatdate(newValue)
                    time = self.formattime(reservation[2])
                    if (self.checkAvailability(date, time,reservation[1],reservation[0],reservation[3])):
                        dbcursor.execute('UPDATE reservation SET reservation_date = %s WHERE reservation_id = %s;', (date,reservationID))
                        messagebox.showinfo("Sucsess", "Date has been updated")
                    else:
                        messagebox.showerror("Error", "Table not available at that time.")
                        
                elif column_index == 7:
                    dbcursor.execute("SELECT restaurant_id, table_id, reservation_date, reservation_party_size FROM reservation WHERE reservation_id = "+str(reservationID)+";")
                    reservation = dbcursor.fetchone() 
                    date = self.formatdate(reservation[2])
                    time = self.formattime(newValue) 
                    if (self.checkAvailability(date, time,reservation[1],reservation[0],reservation[3])):
                        dbcursor.execute('UPDATE reservation SET reservation_time = %s WHERE reservation_id = %s;', (time,reservationID)) 
                        messagebox.showinfo("Sucsess", "Time has been updated")
                    else:
                        messagebox.showerror("Error", "Table not available at that time.")                                              
                
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
            
            
            
        
    def checkAvailability(self,reservationDate,reservationTime,tableid,restaurantID, partySize):
        # Calculate the start and end times  
        self.beforeReservationTime = reservationTime 
        self.afterReservationTime = reservationTime  + timedelta(hours=1)
        
        print(f"Befor: {self.beforeReservationTime}")
        print(f"After: {self.afterReservationTime}")

        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("SELECT * FROM reservation WHERE restaurant_id = %s AND table_id = %s AND reservation_date = %s \
                AND reservation_time BETWEEN (%s) AND (%s);", (restaurantID,tableid,reservationDate,self.beforeReservationTime,self.afterReservationTime))
                dbcursor.fetchall()
                if(dbcursor.rowcount > 0): # this means there is reservations takeing those time slots and so the table is not avalible
                    dbcursor.close()
                    conn.close() 
                    messagebox.showerror("Error", "Table already reserved.")   
                    return False
                else:
                    dbcursor.close()
                    dbcursor = conn.cursor()
                    dbcursor.execute("SELECT * FROM tables WHERE table_id = "+str(tableid)+" ;")
                    self.capacity = dbcursor.fetchone()
                    if (int(self.capacity[2]) < int(partySize)):
                        dbcursor.close()
                        conn.close()
                        messagebox.showerror("Error", f"This table has a capacity of {self.capacity[2]}.")   
                        return False
                    else:
                        dbcursor.close()
                        conn.close() 
                        return True
                    
    def getTableID(self, tablenum, restaurantID):
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object                                                 
                dbcursor.execute("SELECT * FROM tables WHERE restaurant_id = %s AND table_number = %s ;", (restaurantID,tablenum))
                tableID = dbcursor.fetchone()
                if(dbcursor.rowcount > 0): # finding if table exsits
                    dbcursor.close()
                    conn.close() 
                    return tableID[0]
                else:
                    messagebox.showerror("Error", "Table does not exsit")
                    return None   
                
                
    def formatdate(self,date):
        try:
            if isinstance(date, dt.date) != True:
                date = datetime.strptime(date, '%Y-%m-%d') 
            return(date)
        except:
            messagebox.showerror("Error", "Date should be in format Year-Month-Day e.g. 2024-12-12")
    
    def formattime(self,time):
        try:
            if isinstance(time, dt.timedelta) != True:
                time = datetime.strptime(time, "%H:%M:%S")
            return(time)
        except:
            messagebox.showerror("Error", "Time should be in format Hour:Minuite:Seccond e.g. 12:00:00")
    
    def getReservationDetails(self, tableNum, timeSlot):
        conn = dbfunc.getConnection() 
        if conn != None:    #Checking if connection is None                    
            if conn.is_connected(): #Checking if connection is established  
                dbcursor = conn.cursor()    #Creating cursor object 
                dbcursor.execute("SELECT reservation_id, restaurant_id, reservation_customer_name, reservation_customer_email, reservation_customer_phone, reservation_party_size, reservation_date, reservation_time \
                    FROM reservation WHERE table_id = %s AND reservation_time = %s;", (tableNum, timeSlot))
                reservationDetails = dbcursor.fetchall()
                dbcursor.close()
                conn.close() 
                return tuple(reservationDetails)
    
    def cancelReservation(self, reservationID):
        conn = dbfunc.getConnection()
        if conn is not None:
            try:
                dbcursor = conn.cursor()
                dbcursor.execute("DELETE FROM reservation WHERE reservation_id = %s;", (reservationID,))
                conn.commit()
                messagebox.showinfo("Success", "Reservation has been canceled")
            except Exception as e:
                print(e)
                messagebox.showerror("Error", "Failed to cancel the reservation.")
            finally:
                if dbcursor: dbcursor.close()
                if conn: conn.close()

                    
        

