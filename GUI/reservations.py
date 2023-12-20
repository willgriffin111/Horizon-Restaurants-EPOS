import tkinter as Tk
from tkinter import Toplevel, ttk

userName = "Will Griffin"
userId = "193812"


class App(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Reservations Page")
        self.configure(bg="#1A58B5")
        self.resizable(False, False)
        self.sidebar()
        self.topbar(userName=userName, userID=userId)
        self.bottombar()
        self.discount_window = None




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


        create_button = Tk.Button(self.sidebar, text="Create reservation", command=self.create_reservation, bg="white", width=25)
        create_button.pack(pady=10)


        modify_button = Tk.Button(self.sidebar, text="Modify reservation", command=self.modify_reservation, bg="white", width=25)
        modify_button.pack(pady=10)


        delete_button = Tk.Button(self.sidebar, text="Delete reservation", command=self.delete_reservation, bg="white", width=25)
        delete_button.pack(pady=10)

    def create_reservation(self):
        reservation_window = Toplevel(self)
        reservation_window.title("Create reservations")
        reservation_window.geometry("300x500")  
        reservation_window.configure(bg="#FFFFFF")  

        # List of restaurant names for the dropdown
        restaurant_names = ("Birmingham 1", "Birmingham 2", "Bristol 1","Bristol 2", "Cardiff 1", "Cardiff 2", "Glasgow 1", "Glasgow 2" , "Manchester 1", "Manchester 2", "Nottingham 1", "Nottingham 2", "London 1", "London 2")  # Add your restaurant names here

        # This will dynamicaly load from db
        Tk.Label(reservation_window, text="Restaurant name", bg="white").pack(pady=(20, 5))
        restaurant_name_combobox = ttk.Combobox(reservation_window, values=restaurant_names)
        restaurant_name_combobox.pack(pady=(0, 20), padx=20)


        Tk.Label(reservation_window, text="Customer name").pack(pady=(10, 0))
        customer_name_entry = Tk.Entry(reservation_window)
        customer_name_entry.pack(pady=(0, 10))

        Tk.Label(reservation_window, text="Customer number").pack(pady=(10, 0))
        customer_number_entry = Tk.Entry(reservation_window)
        customer_number_entry.pack(pady=(0, 10))

        Tk.Label(reservation_window, text="Party size").pack(pady=(10, 0))
        party_size_entry = Tk.Entry(reservation_window)
        party_size_entry.pack(pady=(0, 10))

        # Frame for date and time entries
        datetime_frame = Tk.Frame(reservation_window, bg="white")
        datetime_frame.pack(fill=Tk.X, pady=20)

        # Date Entry
        date_frame = Tk.Frame(datetime_frame, bg="white")
        date_frame.pack(side=Tk.LEFT, fill=Tk.X, expand=True)

        Tk.Label(date_frame, text="Date", width=5).pack()
        date_entry = Tk.Entry(date_frame)
        date_entry.pack()

        # Time Entry
        time_frame = Tk.Frame(datetime_frame, bg="white" , width=5)
        time_frame.pack(side=Tk.LEFT, fill=Tk.X, expand=True)

        Tk.Label(time_frame, text="Time").pack()
        time_entry = Tk.Entry(time_frame)
        time_entry.pack(expand=True)

        # Submit Button
        submit_button_frame = Tk.Frame(reservation_window, bg="white")
        submit_button_frame.pack(side=Tk.BOTTOM, fill=Tk.X, pady=20)
        submit_button = Tk.Button(submit_button_frame, text="Submit", command=self.submit_reservation, bg="#4CAF50")
        submit_button.pack()
    def submit_reservation(self):
        # Placeholder for submit reservation logic
        print("Reservation submitted")


    def modify_reservation(self):
        print("Modify reservation clicked")

    def delete_reservation(self):
        print("Delete reservation clicked")

        
    
   
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