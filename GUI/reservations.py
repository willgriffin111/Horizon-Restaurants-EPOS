import tkinter as Tk
from tkinter import Toplevel, ttk, messagebox
import random


userName = "Will Griffin"
userId = "193812"

bookings = [
            ("1231481", "Alex Rogers", "123", "Bristol 1", "1/1/2024", "12:00"),
            ("4310832", "James Beal", "123", "Nottingham 1", "2/1/2024", "12:00"),
        ]
'''
Impentation example:

index = "SELECT reservationID FROM RESERVATION"

for i in index:
    booking = (SELECT reservationID FROM RESERVATION", "SELECT customerName FROM RESERVATION", "SELECT customerNumber FROM RESERVATION", \
        "SELECT restaurantName FROM RESERVATION", "SELECT date FROM RESERVATION", "SELECT time FROM RESERVATION")
    bookings.append(booking)

'''


class App(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Reservations Page")
        self.configure(bg="#1A58B5")
        self.resizable(False, False)
        self.sidebar()
        self.topbar(userName=userName, userID=userId)
        self.showBookings()
        self.bottombar()

    # Top bar of window --------------------------------------------------------------------------------------------------------------------------------------|
    
    def topbar(self, userName, userID):
        topFrame = Tk.Frame(self, borderwidth=25, relief=Tk.FLAT, bg="#2976E9")
        topFrame.pack(fill=Tk.X)

        label = Tk.Label(topFrame, text="Horizon Restaurant", fg="white", bg="#2976E9", anchor="w", font=("Arial", 16), underline=True)
        label.pack(fill=Tk.BOTH, expand=True)

        topUnderline = Tk.Canvas(topFrame, height=2, bg="#2976E9", highlightthickness=0)
        topUnderline.create_line(4, 2, 143, 2, width=2, fill="white")
        topUnderline.pack(fill=Tk.X)

        username = Tk.Label(topFrame, text=f"User: {userName}", fg="white", bg="#2976E9", font=("Arial", 12))
        username.pack(side=Tk.RIGHT, anchor="e")
        username.place(relx=1.0, rely=0.5, anchor="e", x=-170, y=4)

        userIDLabel = Tk.Label(topFrame, text=f"ID: {userID}", fg="white", bg="#2976E9", font=("Arial", 12))
        userIDLabel.pack(side=Tk.RIGHT, anchor="e")
        userIDLabel.place(relx=1.0, rely=0.5, anchor="e", x=-90, y=4)

        # Home Button
        homeButton = Tk.Button(topFrame, text="Home", command=self.home_btn, bd=0, highlightthickness=0, highlightbackground="#2976E9", pady=10, border=None)
        homeButton.place(relx=1.0, rely=0.5, anchor="e", x=3, y=4)

    
    def sidebar(self):
        self.sidebar = Tk.Frame(self, width=300, height=478, bg="#F0FFFF")
        self.sidebar.pack(fill=Tk.Y, side=Tk.LEFT)

        create_button = Tk.Button(self.sidebar, text="Create reservation", command=self.createReservations, bg="white", width=25, height=5)
        create_button.pack(pady=(75,30))

        delete_button = Tk.Button(self.sidebar, text="Delete reservation", command=self.deleteReservation, bg="white", width=25, height=5)
        delete_button.pack(pady=30)

    def createReservations(self):
        
        self.reservationsPopUp = Toplevel(self)
        self.reservationsPopUp.title("Create reservations")
        self.reservationsPopUp.geometry("300x500")  
        self.reservationsPopUp.configure(bg="#FFFFFF")  


        # List of restaurant names for the dropdown
        restaurantNames = ("Birmingham 1", "Birmingham 2", "Bristol 1","Bristol 2", "Cardiff 1", "Cardiff 2", "Glasgow 1", "Glasgow 2" , "Manchester 1", "Manchester 2", "Nottingham 1", "Nottingham 2", "London 1", "London 2")  # Add your restaurant names here

        # This will dynamicaly load from db
        Tk.Label(self.reservationsPopUp, text="Restaurant name", bg="white").pack(pady=(20, 5))
        self.restaurantNameDropDown = ttk.Combobox(self.reservationsPopUp, values=restaurantNames)
        self.restaurantNameDropDown.pack(pady=(0, 20), padx=20)


        Tk.Label(self.reservationsPopUp, text="Customer name").pack(pady=(10, 0))
        self.customerNameUI = Tk.Entry(self.reservationsPopUp)
        self.customerNameUI.pack(pady=(0, 10))

        Tk.Label(self.reservationsPopUp, text="Customer number").pack(pady=(10, 0))
        self.customerNumberUI = Tk.Entry(self.reservationsPopUp)
        self.customerNumberUI.pack(pady=(0, 10))

        Tk.Label(self.reservationsPopUp, text="Party size").pack(pady=(10, 0))
        self.partySizeUI = Tk.Entry(self.reservationsPopUp)
        self.partySizeUI.pack(pady=(0, 10))

        # Frame for date and time entries
        datetimeframe = Tk.Frame(self.reservationsPopUp, bg="white")
        datetimeframe.pack(fill=Tk.X, pady=20)

        # Date Entry
        dateFrame = Tk.Frame(datetimeframe, bg="white")
        dateFrame.pack(side=Tk.LEFT, fill=Tk.X, expand=True)

        Tk.Label(dateFrame, text="Date", width=5).pack()
        self.dateUI = Tk.Entry(dateFrame)
        self.dateUI.pack()

        # Time Entry
        timeframe = Tk.Frame(datetimeframe, bg="white" , width=5)
        timeframe.pack(side=Tk.LEFT, fill=Tk.X, expand=True)

        Tk.Label(timeframe, text="Time").pack()
        self.timeUI = Tk.Entry(timeframe)
        self.timeUI.pack(expand=True)

        # Submit Button
        submitButtonFrame = Tk.Frame(self.reservationsPopUp, bg="white")
        submitButtonFrame.pack(side=Tk.BOTTOM, fill=Tk.X, pady=20)
        submitUI = Tk.Button(submitButtonFrame, text="Submit", command=self.createReservationSubmit, bg="#4CAF50")
        submitUI.pack()
        
        
    def createReservationSubmit(self):
        restaurantName = self.restaurantNameDropDown.get()
        customerName = self.customerNameUI.get()
        customerNumber = self.customerNumberUI.get()
        partySize = self.partySizeUI.get()
        date = self.dateUI.get()
        time = self.timeUI.get()


        if not all([restaurantName, customerName, customerNumber, partySize, date, time]):
            messagebox.showerror("Error", "All fields are required")
            return

        reservationId = random.randint(1000000, 9999999)
                    
        booking = (reservationId, customerName, customerNumber, restaurantName, date, time)
        bookings.append(booking)

        self.tree.insert('', 'end', values=booking)
        self.showBookings()

        print("Reservation added:", booking)

        self.reservationsPopUp.destroy()



    def onDoubleClick(self, event):
        row_id = self.tree.identify_row(event.y)
        column_id = self.tree.identify_column(event.x)
        if row_id and column_id:
            self.editWindowPopup(row_id, column_id)

    def editWindowPopup(self, row_id, column_id):
        editWindow = Toplevel(self)
        editWindow.title("Edit Cell Value")
        editWindow.geometry("300x100")

        # Calculate column index
        column_index = int(column_id[1:]) - 1
        current_value = self.tree.item(row_id, 'values')[column_index]

        # Entry widget for new value
        newValueUI = Tk.Entry(editWindow)
        newValueUI.pack(pady=10)
        newValueUI.insert(0, current_value)

        # Save button
        saveButton = Tk.Button(editWindow, text="Save", command=lambda: self.saveNewValue(row_id, column_index, newValueUI.get(), editWindow))
        saveButton.pack()

    def saveNewValue(self, row_id, column_index, new_value, edit_window):

        curentValues = list(self.tree.item(row_id, 'values'))
        curentValues[column_index] = new_value
        self.tree.item(row_id, values=curentValues)
        edit_window.destroy()

    def modifyReservations(self):
        updated_bookings = [self.tree.item(child, 'values') for child in self.tree.get_children()]
        bookings = updated_bookings
        print("Reservations updated:", bookings)
        

    def showBookings(self):
        
        columns = ("Reservation ID", "Customer name", "Customer number", "Restaurant name", "Date", "Time")
        self.tree = ttk.Treeview(self, columns=columns, show='headings', selectmode='browse')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")


        for row in bookings:
            self.tree.insert('', 'end', values=row)

        self.tree.pack(side='right', fill='both', expand=True)

        self.tree.bind("<Double-1>", self.onDoubleClick)
         
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        
    def deleteReservation(self):
        selectedItem = self.tree.selection() 
        if selectedItem:
            selectedReservationId = self.tree.item(selectedItem)['values'][0]  # Assuming reservation ID is the first value
            for i, booking in enumerate(bookings):
                if booking[0] == selectedReservationId:
                    del bookings[i]
                    break
            self.tree.delete(selectedItem)  
            print(f"Reservation {selectedReservationId} deleted")
        else:
            messagebox.showerror("Error", "No item selected")

    def bottombar(self):
        bottomFrame = Tk.Frame(self, borderwidth=7, relief=Tk.FLAT, bg='#2976E9')
        bottomFrame.pack(fill=Tk.X, side=Tk.BOTTOM)
        bottom_label = Tk.Label(bottomFrame, text="", bg='#2976E9')
        bottom_label.pack()

    def home_btn(self):
        print("home button clicked")
        
 

if __name__ == "__main__":
    app = App()
    app.mainloop()