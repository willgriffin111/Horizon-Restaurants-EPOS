from Models.main_m import Model
from Views.main_v import View
from tkinter import messagebox
from datetime import datetime
import re, time

class ReservationsController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["reservations"]
        
       
        self.frame.register_available_slot_callback(self.available_slot_clicked)
        self.frame.register_reserved_slot_callback(self.reserved_slot_clicked)
        self.frame.bind_slot_callbacks()
        
        self.displayUI()
        self.loadTable()
        


        self._bind() 
                    
    def _bind(self) -> None:
        self.frame.homeButton.config(command=self.home)
        self.frame.refreshButton.config(command=self.displayUI)
        
        

    
    def displayUI(self):
        current_user = self.model.auth.current_user
        if current_user:
            if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
                self.frame.resvationDetailsUIManger()
                self.frame.createReservationTable()
                self.frame.restaurantNameDropDown.config(values=self.model.reservation.getRestaurantNames())
                self.frame.restaurantNameDropDown.current(0)
                self.frame.dateEntry.insert(0, datetime.now().strftime('%Y-%m-%d'))  
                self.frame.submitButton.config(command=self.loadTable)
            else:
                self.frame.resvationDetailsUIother()
                self.frame.createReservationTable()
                self.frame.dateEntry.insert(0, datetime.now().strftime('%Y-%m-%d'))
                self.frame.submitButton.config(command=self.loadTable)
        

    def available_slot_clicked(self, table_number, time_slot):
        
        time_slot_datetime = (datetime.min + time_slot).time()
        
        
        if self.frame.dateEntry.get() < datetime.now().strftime('%Y-%m-%d') or time_slot_datetime < datetime.now().time():
            messagebox.showerror("Error", "You cannot book a table for a past date")
        else:
            print(f"Available slot clicked: Table {table_number}, Time Slot {time_slot}")
            self.tableNum = table_number
            self.time = time_slot
            self.date = self.frame.dateEntry.get()
            
            # current_user = self.model.auth.current_user
            if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
                self.frame.createReservationsManager()
                self.frame.restaurantNameDropDown.config(values=self.model.reservation.getRestaurantNames())
                self.frame.submitUIBtn.config(command=self.createReservationSubmit)
            else:
                self.frame.createReservationsOther()
                self.frame.submitUIBtn.config(command=self.createReservationSubmit)
        

    def reserved_slot_clicked(self, table_number, time_slot):
        print(f"Reserved slot clicked: Table {table_number}, Time Slot {time_slot}")
        
        self.frame.viewReservation(table_number, time_slot)

        reservationDetails = self.model.reservation.getReservationDetails(table_number, time_slot)
        
        if reservationDetails:
            details = reservationDetails[0]  
            resID, restID, custName, custNum, partySize, date, time_delta = details

            hours, remainder = divmod(time_delta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            formatted_time = f"{hours:02d}:{minutes:02d}"

            self.frame.tree.insert("", "end", values=(resID, restID, custName, custNum, partySize, date, formatted_time))
            
           
            self.frame.cancel_button.config(command=lambda resID=resID: self.cancelReservation(resID))
            
            self.frame.tree.bind("<Double-1>", self.onDoubleClick)
        else:
            messagebox.showinfo("Info", "No reservation details found for this slot.")

    
    def cancelReservation(self, resID):
        confirmation = messagebox.askquestion('Delete Reservation', 'Do you want to cancel this reservation?')
        if confirmation == 'yes':
            self.model.reservation.cancelReservation(resID)
            self.frame.reservationsPopUp.destroy()  # Close the details window
        time.sleep(0.5)
        
        self.displayUI()  # Refresh the reservations UI
        # self.loadTable()  # Refresh the reservations table

        
        
        
        
        
              

    #edit reservation
    def onDoubleClick(self, event):
        self.rowId = self.frame.tree.identify_row(event.y) #finds out what coloum and row have been selected
        self.columnId = self.frame.tree.identify_column(event.x)
        if self.rowId and self.columnId:
            self.column_index = int(self.columnId[1:]) - 1
            if self.column_index != 0 and self.column_index != 1:
                #creates pop up window
                self.frame.editWindowPopup(self.rowId, self.columnId)
                #binds buttons
                self.frame.saveEditButton.config(command=self.saveNewValue)
            else:
                messagebox.showerror("Error", "You cannot edit this value")
    
    def saveNewValue(self):
        print(self.column_index)
        #formats index
        self.column_index = int(self.columnId[1:]) - 1
        #gets all values from
        self.curentValues = list(self.frame.tree.item(self.rowId, 'values'))
        self.model.reservation.updateReservation(self.column_index, self.frame.newValueUI.get(), self.curentValues[0])
        
        self.loadTable()
        # self.frame.reservationsPopUp.destroy()
        self.reserved_slot_clicked(time_slot=self.curentValues[6], table_number=self.curentValues[1])
        self.frame.editWindow.destroy()
    
        
    def createReservationSubmit(self) -> None:
        print("createing reservation")
        #gets the required varrables
        if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
            self.restaurantName = self.frame.restaurantNameDropDown.get()
        self.customerName = self.frame.customerNameUI.get()
        self.customerNumber = self.frame.customerNumberUI.get()
        self.partySize = self.frame.partySizeUI.get()
        
        if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
            #checks to see if all boxes have entered data for manager create reservation
            if not all([self.restaurantName, self.customerName, self.customerNumber, self.partySize, self.date, self.time, self.tableNum]):
                messagebox.showerror("Error", "All fields are required")
                return
        else:
            #checks to see if all boxes have entered data for other create reservation
            if not all([self.customerName, self.customerNumber, self.partySize, self.date, self.time, self.tableNum]):
                messagebox.showerror("Error", "All fields are required")
                return
            
        if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
            #convert restrant format e.g. bristol 1(1) to 1 to get id
            self.restaurantID = re.search('\(([^)]+)\)', self.restaurantName)
            self.restaurantID = self.restaurantID.group(1)
        else:
            #defults to current users asigned restrant
            self.restaurantID = self.model.auth.current_user.getRestrantID()
            print(self.restaurantID)
            
        #creates reservation in database table
        self.model.reservation.createReservation(self.restaurantID, self.customerName, 
                                                self.customerNumber , self.partySize ,self.date,
                                                self.time,self.model.auth.current_user.getStaffId(), self.tableNum)
        
        self.loadTable()
        self.frame.reservationsPopUp.destroy()
        
    
    def is_valid_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def loadTable(self):

        # self.displayUI()
        current_user = self.model.auth.current_user
        if current_user:
            
            date_str = self.frame.dateEntry.get()  # YYYY-MM-DD

            if not self.is_valid_date(date_str):
                print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                messagebox.showerror("Error", "Invalid date format. Please enter a date in YYYY-MM-DD format.")
                return
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
                restaurant_name_and_id = self.frame.restaurantNameDropDown.get() 
                restaurant_id = restaurant_name_and_id.split("(")[-1].rstrip(")")
            else:
                restaurant_id = self.model.auth.current_user.getRestrantID()

            reservations = self.model.reservation.getDailyReservations(date, restaurant_id)
            self.frame.insertData(reservations)

            



    def home(self) -> None:
        self.view.switch("home")
        
        
    #update upon login
    def update_view(self) -> None:

        current_user = self.model.auth.current_user
        if current_user:
            self.frame.username.config(text=f"User: {current_user.getName()}")
            self.frame.userIDLabel.config(text=f"ID: {current_user.getStaffId()}")
            self.displayUI()
 
        else:
            self.frame.username.config(text=f" User: Name ")
            self.frame.user_id.config(text=f" ID: 12345678 ")
            
  
            

    # OLD ALEX CODE BELOW
        # #create reservation  
    # def createReservations(self): 
    #     if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
    #         self.frame.createReservationsManager()
    #         self.frame.restaurantNameDropDown.config(values=self.model.reservation.getRestaurantNames()) 
    #     else:
    #         self.frame.createReservationsOther()
            
    #     self.frame.submitUI_btn.config(command=self.createReservationSubmit) 
        
        
    # def createReservationSubmit(self) -> None:
    #     print("createing reservation")
    #     #gets the required varrables
    #     if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
    #         self.restaurantName = self.frame.restaurantNameDropDown.get()
    #     self.customerName = self.frame.customerNameUI.get()
    #     self.customerNumber = self.frame.customerNumberUI.get()
    #     self.partySize = self.frame.partySizeUI.get()
    #     self.date = self.frame.dateUI.get()
    #     self.time = self.frame.timeUI.get()
    #     self.tableNum = self.frame.tableNumUI.get()
        
    #     if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
    #         #checks to see if all boxes have entered data for manager create reservation
    #         if not all([self.restaurantName, self.customerName, self.customerNumber, self.partySize, self.date, self.time, self.tableNum]):
    #             messagebox.showerror("Error", "All fields are required")
    #             return
    #     else:
    #         #checks to see if all boxes have entered data for other create reservation
    #         if not all([self.customerName, self.customerNumber, self.partySize, self.date, self.time, self.tableNum]):
    #             messagebox.showerror("Error", "All fields are required")
    #             return
            
    #     if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
    #         #convert restrant format e.g. bristol 1(1) to 1 to get id
    #         self.restaurantID = re.search('\(([^)]+)\)', self.restaurantName)
    #         self.restaurantID = self.restaurantID.group(1)
    #     else:
    #         #defults to current users asigned restrant
    #         self.restaurantID = self.model.auth.current_user.getRestrantID()
    #         print(self.restaurantID)
            
    #     #creates reservation in database table
    #     self.model.reservation.createReservation(self.restaurantID, self.customerName, 
    #                                             self.customerNumber , self.partySize ,self.date,
    #                                             self.time,self.model.auth.current_user.getStaffId(), self.tableNum)
        
    #     self.refreshTable()
    #     self.frame.reservationsPopUp.destroy()
        
    # #delete reservation    
    # def deleteReservation(self):
    #     self.selectedItem = self.frame.tree.selection() 
    #     if self.selectedItem:
    #         confirmation=messagebox.askquestion('Delete reservation', 'Do you want to remove this reservation?')
    #         if confirmation == 'yes':
    #             self.selectedReservationId = self.frame.tree.item(self.selectedItem)['values'][0]  
    #             self.model.reservation.cancelReservation(self.selectedReservationId)
    #         self.refreshTable()
    #     else:
    #         messagebox.showerror("Error", "No item selected")
    
    
        
    # def refreshTable(self):
    #     #updates the table by getting new bookings data from the database
    #     self.frame.clear_table()
    #     if self.model.auth.current_user.getAccountType() == "ADMIN" or self.model.auth.current_user.getAccountType() == "MANAGER":
    #         self.bookings = self.model.reservation.getReservations()
    #     else:
    #         self.bookings = self.model.reservation.getReservations(restaurantID = self.model.auth.current_user.getRestrantID())
    #     self.frame.insert_data(self.bookings)
    #     self.frame.tree.bind("<Double-1>", self.onDoubleClick) #rebinds buttons
            