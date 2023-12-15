'''
Auther Will Griffin
Date: 12/12/2023
Version: 1.0
'''
import tkinter as tk
from tkinter import ttk



tableOrders = {
    "Table 1": [("Starter 1", 1), ("Main 3", 2), ("Desert 2", 2)],
    "Table 2": [("Starter 1", 1), ("Main 6", 1, "No egg"), ("Main 2", 1), ("Main 10", 1, "Medium Spice", "No salt")],
    "Table 3": [("Main 6", 1), ("Main 2", 1, "No tomatoes"), ("Desert 8", 1), ("Desert 4", 1)],
    "Table 4": [("Main 6", 1), ("Main 2", 1, "No tomatoes"), ("Desert 8", 1), ("Desert 4", 1)],
    "Table 5": [("Starter 3", 2), ("Main 5", 1), ("Desert 1", 1)],
    "Table 6": [("Starter 2", 1), ("Main 1", 2, "Extra cheese"), ("Main 4", 1, "Less spice"), ("Desert 3", 2)],
    "Table 7": [("Main 7", 1), ("Main 8", 2, "Gluten-free"), ("Desert 5", 1)],
    "Table 8": [("Starter 4", 1, "Vegan"), ("Main 9", 1), ("Main 11", 1, "No onion"), ("Desert 6", 1, "Sugar-free")]
}

# EXAMPLE OF IMPLEMENTATION
'''
tableOrders = {
     "SELECT tableNumber FROM TABLE": [("SELECT menuItem FROM ORDER WHERE tableNumber FROM Tabel IS 1", 1)],   
}
'''



class KitchenFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='#FFA500')
        self.create_widgets()

    def create_widgets(self):

        # Header frame
        topFrame = tk.Frame(self, bg='#2976E9', height=100)  
        topFrame.pack(fill=tk.X, side=tk.TOP)

        # User details frame within the header frame
        userIdFrame = tk.Frame(topFrame, bg='#2976E9')
        userIdFrame.pack(side=tk.LEFT, padx=10, pady=(10, 0))  

        titleLabel = tk.Label(userIdFrame, text="Horizon Restaurant", font=("inter", 20), bg='#2976E9', fg='white')
        titleLabel.pack()
        
        userNameLabel = tk.Label(userIdFrame, text="Gordon Ramsay", font=("inter", 12), bg='#2976E9', fg='white')
        userNameLabel.pack(side=tk.TOP)

        userIdLabel = tk.Label(userIdFrame, text="ID: 01928312", font=("inter", 12), bg='#2976E9', fg='white')
        userIdLabel.pack(side=tk.BOTTOM)
        
        homeButtonIcon = tk.Button(topFrame, text="⌂", bg='#2976E9', fg='black', font=("inter", 50),command=lambda: self.home())
        homeButtonIcon.pack(side=tk.RIGHT, padx=(0, 10), pady=(10, 0))  
        
        orderTotal = tk.Label(topFrame, text=f"Total open orders:{len(tableOrders)}", font=("inter", 15), bg='#2976E9', fg='white')
        orderTotal.pack(side=tk.LEFT, padx=(50, 0), pady=(10, 0))
        
        # Create the main frame for the table orders
        mainFrame = tk.Frame(self,bg='#1A58B5')
        mainFrame.pack(fill=tk.BOTH, expand=True)

        for tableNumber, orders in self.tableOrders.items():
            self.createTableFrame(mainFrame, orders, tableNumber)

    def createTableFrame(self, parentFrame, orders, tableNumber):
        
        tableFrame = tk.Frame(parentFrame, borderwidth=2, relief=tk.GROOVE)
        tableFrame.pack(side=tk.LEFT, expand=True, padx=10, pady=10)

        tableNumberTitle = tk.Label(tableFrame, text=tableNumber, font=("inter", 12), bg="lightgrey")
        tableNumberTitle.pack(fill=tk.X)
        
        for order in orders:
            orderText = f"{order[1]} x {order[0]}"
            if len(order) > 2:  # Special instructions
                orderText += " (" + ", ".join(order[2:]) + ")"
            orderLabel = tk.Label(tableFrame, text=orderText)
            orderLabel.pack(anchor=tk.W, padx=5)
        
        doneButton = tk.Button(tableFrame, text="Done", command=lambda: self.doneButton(tableNumber))
        doneButton.pack(anchor=tk.S, padx=5)
        
    def test(self):
        
        topFrame = tk.Frame(self, bg='#2976E9', height=100)  
        topFrame.pack(fill=tk.X, side=tk.TOP)


    def doneButton(self, tableNumber):
        tableOrders.pop(tableNumber)
        self.refreshGUI()

    def refreshGUI(self):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
        self.test()

    
    def home(self):
        print("Home")
        
    def perform_kitchen_actions(self):
        # Logic for kitchen actions
        print("Performing kitchen actions...")

        
        


