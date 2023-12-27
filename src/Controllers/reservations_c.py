from Models.main_m import Model
from Views.main_v import View
from tkinter import messagebox
import random

class ReservationsController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["reservations"]
        self._bind()
    
    def _bind(self) -> None:
        self.frame.homeButton.config(command=self.home)
        self.frame.create_btn.config(command=self.createReservations)
        self.frame.delete_button.config(command=self.deleteReservation)
        self.frame.tree.bind("<Double-1>", self.onDoubleClick)

        
        
    def createReservations(self): 
        self.frame.createReservations()
        self.frame.submitUI_btn.config(command=self.createReservationSubmit)   
        
    def createReservationSubmit(self) -> None:
        print("createing reservation")
        self.model.reservation.createReservation(self.frame.restaurantNameDropDown.get(),self.frame.customerNameUI.get(), 
                                                 self.frame.customerNumberUI.get(),self.frame.partySizeUI.get(),self.frame.dateUI.get(),self.frame.timeUI.get())

        if not all([self.restaurantName, self.customerName, self.customerNumber, self.partySize, self.date, self.time]):
            messagebox.showerror("Error", "All fields are required")
            return

        
                    
        self.frame.booking = (self.reservationId, self.customerName, self.customerNumber, self.restaurantName, self.date, self.time)
        self.frame.bookings.append(self.booking)

        self.frame.tree.insert('', 'end', values=self.booking)
        self.frame.showBookings()

        print("Reservation added:", self.booking)

        self.reservationsPopUp.destroy()
        
    #delete reservation    
    def deleteReservation(self):
        self.selectedItem = self.frame.tree.selection() 
        if self.selectedItem:
            self.selectedReservationId = self.frame.tree.item(self.selectedItem)['values'][0]  
            for i, booking in enumerate(self.bookings):
                if booking[0] == self.selectedReservationId:
                    del self.bookings[i]
                    break
            self.tree.delete(self.selectedItem)  
            print(f"Reservation {self.selectedReservationId} deleted")
        else:
            messagebox.showerror("Error", "No item selected")
    
    

    #edit in collems
    def onDoubleClick(self, event):
        self.rowId = self.frame.tree.identify_row(event.y)
        self.columnId = self.frame.tree.identify_column(event.x)
        if self.rowId and self.columnId:
            self.frame.editWindowPopup(self.rowId, self.columnId)
            self.frame.saveEditButton.config(command=self.saveNewValue)
    
    def saveNewValue(self):
        self.column_index = int(self.columnId[1:]) - 1
        self.curentValues = list(self.frame.tree.item(self.rowId, 'values'))
        self.curentValues[self.column_index] = self.frame.newValueUI.get()
        self.frame.tree.item(self.rowId, values=self.curentValues)
        self.frame.editWindow.destroy()
            
    def home(self) -> None:
        self.view.switch("home")