'''
Author: Will Griffin
Date Created: 22/12/2023
'''

import tkinter as Tk
from tkinter import Toplevel, ttk, messagebox
import random




'''
Impentation example:

index = "SELECT reservationID FROM RESERVATION"

for i in index:
    booking = (SELECT reservationID FROM RESERVATION", "SELECT customerName FROM RESERVATION", "SELECT customerNumber FROM RESERVATION", \
        "SELECT restaurantName FROM RESERVATION", "SELECT date FROM RESERVATION", "SELECT time FROM RESERVATION")
    bookings.append(booking)

'''


class ReservationsView(Tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("800x600")
        # self.title("Reservations Page")
        self.configure(bg="white")
        # self.resizable(False, False)
        self.topbar()
        self.bottombar()
        self.sidebar()
        self.showBookings()


    # Top bar of window --------------------------------------------------------------------------------------------------------------------------------------|
    
    def topbar(self):
        self.topFrame = Tk.Frame(self, borderwidth=25, relief=Tk.FLAT, bg="#2976E9")
        self.topFrame.pack(fill=Tk.X)

        self.label = Tk.Label(self.topFrame, text="Horizon Restaurant", fg="white", bg="#2976E9", anchor="w", font=("Arial", 20), underline=True)
        self.label.pack(fill=Tk.BOTH, expand=True)

        self.topUnderline = Tk.Canvas(self.topFrame, height=2, bg="#2976E9", highlightthickness=0)
        self.topUnderline.create_line(4, 2, 175, 2, width=2, fill="white")
        self.topUnderline.pack(fill=Tk.X)

        self.username = Tk.Label(self.topFrame, text=f"", fg="white", bg="#2976E9", font=("Arial", 12))
        self.username.pack(side=Tk.RIGHT, anchor="e")
        self.username.place(relx=1.0, rely=0.5, anchor="e", x=-170, y=4)

        self.userIDLabel = Tk.Label(self.topFrame, text=f"", fg="white", bg="#2976E9", font=("Arial", 12))
        self.userIDLabel.pack(side=Tk.RIGHT, anchor="e")
        self.userIDLabel.place(relx=1.0, rely=0.5, anchor="e", x=-90, y=4)

        # Home Button
        self.homeButton = Tk.Button(self.topFrame, text="Home", bd=0, highlightthickness=0, highlightbackground="#2976E9", pady=10, border=None)
        self.homeButton.place(relx=1.0, rely=0.5, anchor="e", x=3, y=4)

    # Side bar  --------------------------------------------------------------------------------------------------------------------------------------|
    def sidebar(self):
        self.sidebar = Tk.Frame(self, bg="lightgrey")
        self.sidebar.pack(fill=Tk.Y, side=Tk.LEFT)

        self.create_btn = Tk.Button(self.sidebar, text="Create ", bg="white", width=10, height=5)
        self.create_btn.pack(pady=30,padx=35)

        self.delete_button = Tk.Button(self.sidebar, text="Delete ", bg="white", width=10, height=5)
        self.delete_button.pack(pady=30,padx=35)
        
    # Create window popup --------------------------------------------------------------------------------------------------------------------------------------|
    def createReservationsManager(self):
        
        self.reservationsPopUp = Toplevel(self)
        self.reservationsPopUp.title("Create reservations")
        self.reservationsPopUp.geometry("400x550")  
        self.reservationsPopUp.resizable(False,False)
        self.reservationsPopUp.configure(bg="#FFFFFF")  

        # List of restaurant names for the dropdown (this will dynamicaly load from db)
          # Add your restaurant names here

       
        Tk.Label(self.reservationsPopUp, text="Restaurant name", bg="white").pack(pady=(20, 5))
        self.restaurantNameDropDown = ttk.Combobox(self.reservationsPopUp)
        self.restaurantNameDropDown.pack(pady=(0, 20), padx=20)


        Tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Customer name").pack(pady=(10, 0))
        self.customerNameUI = Tk.Entry(self.reservationsPopUp,bg='white',fg='black')
        self.customerNameUI.pack(pady=(0, 10))

        Tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Customer number").pack(pady=(10, 0))
        self.customerNumberUI = Tk.Entry(self.reservationsPopUp,bg='white',fg='black')
        self.customerNumberUI.pack(pady=(0, 10))
        
        Tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Table number").pack(pady=(10, 0))
        self.tableNumUI = Tk.Entry(self.reservationsPopUp,bg='white',fg='black')
        self.tableNumUI.pack(pady=(0, 10))

        Tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Party size").pack(pady=(10, 0))
        self.partySizeUI = Tk.Entry(self.reservationsPopUp,bg='white',fg='black')
        self.partySizeUI.pack(pady=(0, 10))

        self.datetimeframe = Tk.Frame(self.reservationsPopUp, bg="white")
        self.datetimeframe.pack(fill=Tk.X, pady=20)

        self.dateFrame = Tk.Frame(self.datetimeframe, bg="white")
        self.dateFrame.pack(side=Tk.LEFT, fill=Tk.X, expand=True)

        Tk.Label(self.dateFrame,bg='white',fg='black', text="Date YYYY-MM-DD").pack()
        self.dateUI = Tk.Entry(self.dateFrame,bg='white',fg='black')
        self.dateUI.pack()

        self.timeframe = Tk.Frame(self.datetimeframe, bg="white" , width=5)
        self.timeframe.pack(side=Tk.LEFT, fill=Tk.X, expand=True)

        Tk.Label(self.timeframe,bg='white',fg='black', text="Time HH:MM:SS").pack()
        self.timeUI = Tk.Entry(self.timeframe,bg='white',fg='black')
        self.timeUI.pack(expand=True)

        # Submit Button
        self.submitButtonFrame = Tk.Frame(self.reservationsPopUp, bg="white")
        self.submitButtonFrame.pack(pady=10)

        self.submitUI_btn = Tk.Button(self.submitButtonFrame, text="Submit", bg="white",width=10,height=10)
        self.submitUI_btn.pack()
        
    def createReservationsOther(self):
        
        self.reservationsPopUp = Toplevel(self)
        self.reservationsPopUp.title("Create reservations")
        self.reservationsPopUp.geometry("300x550")  
        self.reservationsPopUp.resizable(False,False)
        self.reservationsPopUp.configure(bg="#FFFFFF")  

        Tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Customer name").pack(pady=(10, 0))
        self.customerNameUI = Tk.Entry(self.reservationsPopUp)
        self.customerNameUI.pack(pady=(0, 10))

        Tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Customer number").pack(pady=(10, 0))
        self.customerNumberUI = Tk.Entry(self.reservationsPopUp)
        self.customerNumberUI.pack(pady=(0, 10))
        
        Tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Table number").pack(pady=(10, 0))
        self.tableNumUI = Tk.Entry(self.reservationsPopUp)
        self.tableNumUI.pack(pady=(0, 10))

        Tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Party size").pack(pady=(10, 0))
        self.partySizeUI = Tk.Entry(self.reservationsPopUp)
        self.partySizeUI.pack(pady=(0, 10))

        self.datetimeframe = Tk.Frame(self.reservationsPopUp, bg="white")
        self.datetimeframe.pack(fill=Tk.X, pady=20)

        self.dateFrame = Tk.Frame(self.datetimeframe, bg="white")
        self.dateFrame.pack(side=Tk.LEFT, fill=Tk.X, expand=True)

        Tk.Label(self.dateFrame,bg='white',fg='black', text="Date YYYY-MM-DD", width=5).pack()
        self.dateUI = Tk.Entry(self.dateFrame)
        self.dateUI.pack()

        self.timeframe = Tk.Frame(self.datetimeframe, bg="white" , width=5)
        self.timeframe.pack(side=Tk.LEFT, fill=Tk.X, expand=True)

        Tk.Label(self.timeframe,bg='white',fg='black', text="Time HH:MM:SS").pack()
        self.timeUI = Tk.Entry(self.timeframe)
        self.timeUI.pack(expand=True)

        # Submit Button
        self.submitButtonFrame = Tk.Frame(self.reservationsPopUp, bg="white")
        self.submitButtonFrame.pack(side=Tk.BOTTOM, fill=Tk.X, pady=20)
        self.submitUI_btn = Tk.Button(self.submitButtonFrame, text="Submit")
        self.submitUI_btn.pack()
        
    

    # Modifying value in the table --------------------------------------------------------------------------------------------------------------------------------------|
        
    def editWindowPopup(self, row_id, column_id):
        self.editWindow = Toplevel(self)
        self.editWindow.title("Edit Cell Value")
        self.editWindow.geometry("300x100")

        # Calculate column index
        self.column_index = int(column_id[1:]) - 1
        self.current_value = self.tree.item(row_id, 'values')[self.column_index]

        self.newValueUI = Tk.Entry(self.editWindow)
        self.newValueUI.pack(pady=10)
        self.newValueUI.insert(0, self.current_value)
        
        self.saveEditButton = Tk.Button(self.editWindow, text="Save")
        self.saveEditButton.pack()

    def modifyReservations(self):
        self.updated_bookings = [self.tree.item(child, 'values') for child in self.tree.get_children()]
        self.bookings = self.updated_bookings
        print("Reservations updated:", self.bookings)
        

    # Displaying table  --------------------------------------------------------------------------------------------------------------------------------------|
    def showBookings(self):
        reserve_lbl = Tk.Label(self, text='Reservations',fg='black', bg='white', font=("Arial", 18))
        reserve_lbl.pack(fill='x',pady=20)
        
        if hasattr(self, 'tree'):
            self.tree.destroy()
        
        columns = ("Reservation ID", "Customer name", "Customer number", "Restaurant ID", "Table Number", "Date", "Time")
        self.tree = ttk.Treeview(self, columns=columns, show='headings', selectmode='browse')
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")


        self.insert_data()

        self.tree.pack(side='right', fill='both', expand=True)

         
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        
    def clear_table(self):
        for record in self.tree.get_children():
            self.tree.delete(record)
    
    def insert_data(self, data = None):
        # For loop to generate the values in the database 
        if data != None:
            for row in data:
                self.tree.insert('', 'end', values=row)
        
    # Deleting reservations --------------------------------------------------------------------------------------------------------------------------------------|
    
            
    # Bottom bar --------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        self.bottomFrame = Tk.Frame(self, borderwidth=7, relief=Tk.FLAT, bg='#2976E9')
        self.bottomFrame.pack(fill=Tk.X, side=Tk.BOTTOM)
        self.bottom_label = Tk.Label(self.bottomFrame, text="", bg='#2976E9')
        self.bottom_label.pack()

