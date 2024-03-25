import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel

userName = "Will Griffin"
userId = "193812"

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
times = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM"]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('Horizon Restaurant')
        self.configure(bg='#1A58B5')
        self.reservations = {}  # Stores reservation status
        self.buttons = {}  # Stores button references
        self.topbar(userName=userName, userID=userId)
        self.bottombar()
        self.create_reservation_table()


    def topbar(self, userName, userID):
        self.topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#2976E9')
        self.topFrame.pack(fill=tk.X)
        label = tk.Label(self.topFrame, text="Horizon Restaurant", fg='white', bg='#2976E9', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(self.topFrame, height=2, bg='#2976E9', highlightthickness=0)
        canvas.create_line(4, 2, 218, 2, width=2, fill='white')
        canvas.pack(fill=tk.X)
        username = tk.Label(self.topFrame, text=f" User: {userName} ", fg='white', bg='#2976E9', font=('Arial', 14))
        username.pack(side=tk.RIGHT, anchor='e')
        username.place(relx=1.0, rely=0.5, anchor='e', x=-350, y=4)
        user_id = tk.Label(self.topFrame, text=f"ID: {userID}", fg='white', bg='#2976E9', font=('Arial', 14))
        user_id.pack(side=tk.RIGHT, anchor='e')
        user_id.place(relx=1.0, rely=0.5, anchor='e', x=-260, y=4)
        
        self.homeButton = tk.Button(self.topFrame, text="Home", bd=0, highlightthickness=0, highlightbackground="#2976E9", pady=10, border=None)
        self.homeButton.place(relx=1.0, rely=0.5, anchor="e", x=3, y=4)

    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='#2976E9')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#2976E9')
        bottom_label.pack()

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

        self.datetimeframe = tk.Frame(self.reservationsPopUp, bg="white")
        self.datetimeframe.pack(fill=tk.X, pady=20)

        self.dateFrame = tk.Frame(self.datetimeframe, bg="white")
        self.dateFrame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Label(self.dateFrame,bg='white',fg='black', text="Date YYYY-MM-DD").pack()
        self.dateUI = tk.Entry(self.dateFrame,bg='white',fg='black')
        self.dateUI.pack()

        self.timeframe = tk.Frame(self.datetimeframe, bg="white" , width=5)
        self.timeframe.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Label(self.timeframe,bg='white',fg='black', text="Time HH:MM:SS").pack()
        self.timeUI = tk.Entry(self.timeframe,bg='white',fg='black')
        self.timeUI.pack(expand=True)

        # Submit Button
        self.submitButtonFrame = tk.Frame(self.reservationsPopUp, bg="white")
        self.submitButtonFrame.pack(pady=10)

        self.submitUI_btn = tk.Button(self.submitButtonFrame, text="Submit", bg="white",width=10,height=10)
        self.submitUI_btn.pack()
        
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

        self.datetimeframe = tk.Frame(self.reservationsPopUp, bg="white")
        self.datetimeframe.pack(fill=tk.X, pady=20)

        self.dateFrame = tk.Frame(self.datetimeframe, bg="white")
        self.dateFrame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Label(self.dateFrame,bg='white',fg='black', text="Date YYYY-MM-DD", width=5).pack()
        self.dateUI = tk.Entry(self.dateFrame)
        self.dateUI.pack()

        self.timeframe = tk.Frame(self.datetimeframe, bg="white" , width=5)
        self.timeframe.pack(side=tk.LEFT, fill=tk.X, expand=True)

        tk.Label(self.timeframe,bg='white',fg='black', text="Time HH:MM:SS").pack()
        self.timeUI = tk.Entry(self.timeframe)
        self.timeUI.pack(expand=True)

        # Submit Button
        self.submitButtonFrame = tk.Frame(self.reservationsPopUp, bg="white")
        self.submitButtonFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)
        self.submitUI_btn = tk.Button(self.submitButtonFrame, text="Submit")
        self.submitUI_btn.pack()
    
    def viewReservation(self):

        self.modifyOrderWindow = tk.Toplevel(self)
        self.modifyOrderWindow.title("Modify Order")
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
        
        


    def create_reservation_table(self):
        tableFrame = tk.Frame(self, bg='#1A58B5')
        tableFrame.pack(fill=tk.BOTH, expand=True, padx=75, pady=20)

        for i, day in enumerate(days):
            tk.Label(tableFrame, text=day, borderwidth=2, relief="groove").grid(row=0, column=i+1, sticky='nsew')

        for j, time in enumerate(times):
            tk.Label(tableFrame, text=time, borderwidth=2, relief="groove").grid(row=j+1, column=0, sticky='nsew')

            for i, day in enumerate(days):
                key = (day, time)
                self.reservations[key] = False 
                button = tk.Button(tableFrame, padx = 10, pady= 5,bg = 'green',text="Available", borderwidth=2, relief="groove")
                button.grid(row=j+1, column=i+1, sticky='nsew')
                self.buttons[key] = button
    
    def saveReservation(self, day, time):

        self.reservations[(day, time)] = True
        self.buttons[(day, time)].config(text="Booked\nClick to see details")
        self.reservationsPopUp.destroy()  
if __name__ == "__main__":
    app = App()
    app.mainloop()
