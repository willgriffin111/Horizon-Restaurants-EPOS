import tkinter as tk
from tkinter import ttk, Frame
from tkinter import Toplevel
from datetime import datetime, timedelta

# List of times in "HH:MM AM/PM" format
times_str = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM"]

# Convert to datetime.timedelta
times = []
for time_str in times_str:
    time_obj = datetime.strptime(time_str, "%I:%M %p")
    timedelta_since_midnight = timedelta(hours=time_obj.hour, minutes=time_obj.minute)
    times.append(timedelta_since_midnight)

class ReservationsView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("800x600")
        # self.title('Horizon Restaurant')
        self.configure(bg='#1A58B5')
        self.reservations = {}  # Stores reservation status
        self.buttons = {}  # Stores button references
        self.topbar()
        self.bottomBar()
        self.resvationDetailsUI()
        self.createReservationTable()



    def topbar(self):
        self.topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#2976E9')
        self.topFrame.pack(fill=tk.X)
        label = tk.Label(self.topFrame, text="Horizon Restaurant", fg='white', bg='#2976E9', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(self.topFrame, height=2, bg='#2976E9', highlightthickness=0)
        canvas.create_line(4, 2, 218, 2, width=2, fill='white')
        canvas.pack(fill=tk.X)
        self.username = tk.Label(self.topFrame, fg='white', bg='#2976E9', font=('Arial', 14))
        self.username.pack(side=tk.RIGHT, anchor='e')
        self.username.place(relx=1.0, rely=0.5, anchor='e', x=-350, y=4)
        self.userIDLabel = tk.Label(self.topFrame, fg='white', bg='#2976E9', font=('Arial', 14))
        self.userIDLabel.pack(side=tk.RIGHT, anchor='e')
        self.userIDLabel.place(relx=1.0, rely=0.5, anchor='e', x=-260, y=4)
        
        self.homeButton = tk.Button(self.topFrame, text="Home", bd=0, highlightthickness=0, highlightbackground="#2976E9", pady=10, border=None)
        self.homeButton.place(relx=1.0, rely=0.5, anchor="e", x=3, y=4)
        
        self.refreshButton = tk.Button(self.topFrame, text='Refresh', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.refreshButton.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

    def bottomBar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='#2976E9')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottomLabel = tk.Label(bottomFrame, text="", bg='#2976E9')
        bottomLabel.pack()

    def createReservationsManager(self):
        
        self.reservationsPopUp = Toplevel(self)
        self.reservationsPopUp.title("Create reservations")
        self.reservationsPopUp.geometry("400x550")  
        self.reservationsPopUp.resizable(False,False)
        self.reservationsPopUp.configure(bg="#FFFFFF")  
        
        tk.Label(self.reservationsPopUp, text="Restaurant name", bg="white").pack(pady=(20, 5))
        self.restaurantNameDropDown = ttk.Combobox(self.reservationsPopUp)
        self.restaurantNameDropDown.pack(pady=(0, 20), padx=20)


        tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Customer name").pack(pady=(10, 0))
        self.customerNameUI = tk.Entry(self.reservationsPopUp,bg='white',fg='black')
        self.customerNameUI.pack(pady=(0, 10))

        tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Customer number").pack(pady=(10, 0))
        self.customerNumberUI = tk.Entry(self.reservationsPopUp,bg='white',fg='black')
        self.customerNumberUI.pack(pady=(0, 10))
        
        tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Table number").pack(pady=(10, 0))
        self.tableNumUI = tk.Entry(self.reservationsPopUp,bg='white',fg='black')
        self.tableNumUI.pack(pady=(0, 10))

        tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Party size").pack(pady=(10, 0))
        self.partySizeUI = tk.Entry(self.reservationsPopUp,bg='white',fg='black')
        self.partySizeUI.pack(pady=(0, 10))

        self.datetimeFrame = tk.Frame(self.reservationsPopUp, bg="white")
        self.datetimeFrame.pack(fill=tk.X, pady=20)

        self.dateFrame = tk.Frame(self.datetimeFrame, bg="white")
        self.dateFrame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Label(self.dateFrame,bg='white',fg='black', text="Date YYYY-MM-DD").pack()
        self.dateUI = tk.Entry(self.dateFrame,bg='white',fg='black')
        self.dateUI.pack()

        self.timeFrame = tk.Frame(self.datetimeFrame, bg="white" , width=5)
        self.timeFrame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Label(self.timeFrame,bg='white',fg='black', text="Time HH:MM:SS").pack()
        self.timeUI = tk.Entry(self.timeFrame,bg='white',fg='black')
        self.timeUI.pack(expand=True)

        # Submit Button
        self.submitButtonFrame = tk.Frame(self.reservationsPopUp, bg="white")
        self.submitButtonFrame.pack(pady=10)

        self.submitUIBtn = tk.Button(self.submitButtonFrame, text="Submit", bg="white",width=10,height=10)
        self.submitUIBtn.pack()
        
    def createReservationsOther(self):
        
        self.reservationsPopUp = Toplevel(self)
        self.reservationsPopUp.title("Create reservations")
        self.reservationsPopUp.geometry("300x550")  
        self.reservationsPopUp.resizable(False,False)
        self.reservationsPopUp.configure(bg="#FFFFFF")  

        tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Customer name").pack(pady=(10, 0))
        self.customerNameUI = tk.Entry(self.reservationsPopUp)
        self.customerNameUI.pack(pady=(0, 10))

        tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Customer number").pack(pady=(10, 0))
        self.customerNumberUI = tk.Entry(self.reservationsPopUp)
        self.customerNumberUI.pack(pady=(0, 10))
        
        tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Table number").pack(pady=(10, 0))
        self.tableNumUI = tk.Entry(self.reservationsPopUp)
        self.tableNumUI.pack(pady=(0, 10))

        tk.Label(self.reservationsPopUp,bg='white',fg='black', text="Party size").pack(pady=(10, 0))
        self.partySizeUI = tk.Entry(self.reservationsPopUp)
        self.partySizeUI.pack(pady=(0, 10))

        self.datetimeFrame = tk.Frame(self.reservationsPopUp, bg="white")
        self.datetimeFrame.pack(fill=tk.X, pady=20)

        self.dateFrame = tk.Frame(self.datetimeFrame, bg="white")
        self.dateFrame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Label(self.dateFrame,bg='white',fg='black', text="Date YYYY-MM-DD", width=5).pack()
        self.dateUI = tk.Entry(self.dateFrame)
        self.dateUI.pack()

        self.timeFrame = tk.Frame(self.datetimeFrame, bg="white" , width=5)
        self.timeFrame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Label(self.timeFrame,bg='white',fg='black', text="Time HH:MM:SS").pack()
        self.timeUI = tk.Entry(self.timeFrame)
        self.timeUI.pack(expand=True)

        # Submit Button
        self.submitButtonFrame = tk.Frame(self.reservationsPopUp, bg="white")
        self.submitButtonFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)
        self.submitUIBtn = tk.Button(self.submitButtonFrame, text="Submit")
        self.submitUIBtn.pack()
    
    def viewReservation(self):

        self.modifyOrderWindow = tk.Toplevel(self)
        self.modifyOrderWindow.title("Reservation Details")
        self.modifyOrderWindow.geometry("500x500")
        self.modifyOrderWindow.resizable(False, False)
        self.modifyOrderWindow.configure(bg="#FFFFFF")  

        self.reservationId = tk.Label(self.modifyOrderWindow, text="Reservation ID: ", bg="white")
        self.reservationId.pack(pady=(20, 5))
        
        self.restaurantId = tk.Label(self.modifyOrderWindow, text="Restaurant ID: ", bg="white")
        self.restaurantId.pack(pady=(20, 5))
        
        self.customerName = tk.Label(self.modifyOrderWindow, text="Customer Name: ", bg="white")
        self.customerName.pack(pady=(20, 5))
        
        self.customerNumber = tk.Label(self.modifyOrderWindow, text="Customer Number: ", bg="white")
        self.customerNumber.pack(pady=(20, 5))
        
        self.partySize = tk.Label(self.modifyOrderWindow, text="Party Size: ", bg="white")
        self.partySize.pack(pady=(20, 5))
        
        self.date = tk.Label(self.modifyOrderWindow, text="Date: ", bg="white")
        self.date.pack(pady=(20, 5))
        
        self.time = tk.Label(self.modifyOrderWindow, text="Time: ", bg="white")
        self.time.pack(pady=(20, 5))
        
        self.cancelButton = tk.Button(self.modifyOrderWindow, text="Cancel", bg="white" , padx=10, pady=5)
        self.cancelButton.pack(pady=(20, 5))
        

    def resvationDetailsUI(self):
        self.inputFrame = tk.Frame(self, bg="white")
        self.inputFrame.pack(pady=0)  

        self.dateLabel = tk.Label(self.inputFrame, text="Date:")
        self.dateLabel.pack(side=tk.LEFT, pady=0)  

        self.dateEntry = tk.Entry(self.inputFrame, bg="white", width=10)
        self.dateEntry.pack(side=tk.LEFT, padx=(10, 0), pady=0) 

        self.restaurantNameLabel = tk.Label(self.inputFrame, text="Restaurant name: ", bg="white")
        self.restaurantNameLabel.pack(side=tk.LEFT, pady=0, padx=20)  

        self.restaurantNameDropDown = ttk.Combobox(self.inputFrame)
        self.restaurantNameDropDown.pack(side=tk.LEFT, pady=0, padx=(0, 20))  
        
        self.submitButton = tk.Button(self.inputFrame, text="Submit", bg="white", padx=10, pady=5)
        self.submitButton.pack(side=tk.LEFT, pady=0, padx=(0, 20))

    
    def createReservationTable(self):
        if hasattr(self, 'tableFrame'):
            self.tableFrame.destroy()

        self.tableFrame = tk.Frame(self, bg='#1A58B5')
        self.tableFrame.pack(fill=tk.BOTH, expand=True, padx=75, pady=10)

        tableNumbers = [1, 2, 3, 4, 5, 6]

        for i, tableNum in enumerate(tableNumbers):
            tk.Label(self.tableFrame, text=f"Table {tableNum}", borderwidth=2, relief="groove").grid(row=0, column=i+1, sticky='nsew')

        for j, time in enumerate(times):
            tk.Label(self.tableFrame, text=str(time), borderwidth=2, relief="groove").grid(row=j+1, column=0, sticky='nsew')

            for i, tableNum in enumerate(tableNumbers):
                key = (tableNum, time)
                self.button = tk.Button(self.tableFrame, padx=10, pady=5, bg='green', text="Available", borderwidth=2, relief="groove")
                self.button.grid(row=j+1, column=i+1, sticky='nsew')
                self.buttons[key] = self.button

                
    def insertData(self, reservations):
        print(reservations)

        for key, button in self.buttons.items():
            button.config(bg='green', text='Available')

        for reservationTime, tableId, count in reservations:
            key = (tableId, reservationTime)

            if key in self.buttons:
                if count > 0: 
                    self.buttons[key].config(bg='red', text='Reserved')
