'''
Author: Will Griffin, Jevhan Seechurn, Alex Rogers
Date: 12/12/2023
Version: 1.1
'''
import tkinter as tk
from tkinter import ttk, Frame, Toplevel
from .order_v import OrderCreate


# tableOrders = {
#     "Table 1": [("Starter 1", 1), ("Main 3", 2), ("Desert 2", 2)],
#     "Table 2": [("Starter 1", 1), ("Main 6", 1, "No egg"), ("Main 2", 1), ("Main 10", 1, "Medium Spice", "No salt")],
#     "Table 3": [("Main 6", 1), ("Main 2", 1, "No tomatoes"), ("Desert 8", 1), ("Desert 4", 1)],
#     "Table 4": [("Main 6", 1), ("Main 2", 1, "No tomatoes"), ("Desert 8", 1), ("Desert 4", 1)],
#     "Table 5": [("Starter 3", 2), ("Main 5", 1), ("Desert 1", 1)],
#     "Table 6": [("Starter 2", 1), ("Main 1", 2, "Extra cheese"), ("Main 4", 1, "Less spice"), ("Desert 3", 2)],
#     "Table 7": [("Main 7", 1), ("Main 8", 2, "Gluten-free"), ("Desert 5", 1)],
#     "Table 8": [("Starter 4", 1, "Vegan"), ("Main 9", 1), ("Main 11", 1, "No onion"), ("Desert 6", 1, "Sugar-free")]
# }

# EXAMPLE OF IMPLEMENTATION
'''
tableOrders = {
     "SELECT tableNumber FROM TABLE": [("SELECT menuItem FROM ORDER WHERE tableNumber FROM Tabel IS 1", 1)],   
}
'''

class OrdersView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.tableOrders = {}  
        self.doneButton = tk.Button(self, text="Done")
        self.cancelButton = tk.Button(self, text="Cancel")  
        self.modifyButton = tk.Button(self, text="Modify")


        self.create_top_frame()
    

    def create_top_frame(self):
        topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#2976E9')
        topFrame.pack(fill=tk.X)

        # The Label 'Horizon Restaurant'
        label = tk.Label(topFrame, text="Horizon Restaurant", fg='white', bg='#2976E9', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)

        # Underlines the Label 
        canvas = tk.Canvas(topFrame, height=2, bg='#2976E9', highlightthickness=0)
        canvas.create_line(4, 2, 218, 2, width=2, fill='white')
        canvas.pack(fill=tk.X)

        # Username
        self.username = tk.Label(topFrame, fg='white', bg='#2976E9', font=('Arial', 14))
        self.username.pack(side=tk.RIGHT, anchor='e')
        self.username.place(relx=1.0, rely=0.5, anchor='e', x=-350, y=4)

        # User ID
        self.user_id = tk.Label(topFrame,fg='white', bg='#2976E9', font=('Arial', 14))
        self.user_id.pack(side=tk.RIGHT, anchor='e')
        self.user_id.place(relx=1.0, rely=0.5, anchor='e', x=-260, y=4)

        # Refresh Button
        self.refresh_button = tk.Button(topFrame, text='Refresh', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.refresh_button.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        # Home Button
        self.homeButton = tk.Button(topFrame, text='Home', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.homeButton.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)
        
        # # Create the main frame for the table orders
        # mainFrame = tk.Frame(self,bg='#1A58B5')
        # mainFrame.pack(fill=tk.BOTH, expand=True)

        # for tableNumber, orders in self.tableOrders.items():
        #     self.createTableFrame(mainFrame, orders, tableNumber)
            
        # bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='#2976E9')
        # bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        # bottom_label = tk.Label(bottomFrame, text="", bg='#2976E9')
        # bottom_label.pack()
        
    def create_main_frame(self, tableOrders):
        self.tableOrders = tableOrders
        if hasattr(self, 'mainFrame'):  # Check if mainFrame already exists
            self.mainFrame.destroy()  # Destroy existing mainFrame
        self.mainFrame = tk.Frame(self, bg='#1A58B5')
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        # Grid configuration
        row, col = 0, 0
        for tableNumber, orders in self.tableOrders.items():
            if col == 4:  # Move to the next row after every 4 tables
                row += 1
                col = 0
            self.createTableFrame(self.mainFrame, orders, tableNumber, row, col)
            col += 1
        

    def createTableFrame(self, parentFrame, orders, tableNumber, row, col):
        
        tableFrame = tk.Frame(parentFrame, borderwidth=2, relief=tk.GROOVE)
        tableFrame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        # tableFrame = tk.Frame(parentFrame, borderwidth=2, relief=tk.GROOVE)
        # tableFrame.pack(side=tk.LEFT, expand=True, padx=10, pady=10)

        tableNumberTitle = tk.Label(tableFrame, text=tableNumber, font=("inter", 12), bg="lightgrey")
        tableNumberTitle.pack(fill=tk.X)

        for order in orders:
            
            orderText = f"{order[1]} x {order[0]}"
            if len(order) > 2:  # Special instructions
                orderText += " (" + ", ".join(order[2:]) + ")"
            orderLabel = tk.Label(tableFrame, text=orderText)
            orderLabel.pack(anchor=tk.W, padx=5)
            
        buttonFrame = tk.Frame(tableFrame)
        buttonFrame.pack(side=tk.BOTTOM, pady=5)

        doneButton = tk.Button(buttonFrame, text="Done",
                                command=lambda tn=tableNumber: self.orderCompleteCallback(tn))
        doneButton.pack(side=tk.LEFT, padx=5)
        
        modifyButton = tk.Button(buttonFrame, text="Modify",
                                command=lambda tn=tableNumber: self.orderModifyCallback(tn))
        modifyButton.pack(side=tk.LEFT, padx=5)
        
        cancelButton = tk.Button(buttonFrame, text="Cancel",
                                command=lambda tn=tableNumber: self.orderCancelCallback(tn))
        cancelButton.pack(side=tk.LEFT, padx=5)
        
    def setOrderCompleteCallback(self, callback):
        self.orderCompleteCallback = callback
        
    def setOrderCancelCallback(self, callback):
        self.orderCancelCallback = callback
    
    def setOrderModifyCallback(self, callback):
        self.orderModifyCallback = callback
        
    
    def modifyOrderPopUp(self, data):
        if not hasattr(self, 'modifyOrderWindow') or not self.modifyOrderWindow.winfo_exists():
            self.modifyOrderWindow = tk.Toplevel(self)
            self.modifyOrderWindow.title("Modify Order")
            self.modifyOrderWindow.geometry("500x500")
            self.modifyOrderWindow.resizable(False, False)
            self.modifyOrderWindow.configure(bg="#FFFFFF")  

            reserve_lbl = tk.Label(self.modifyOrderWindow, text='Order', fg='black', bg='white', font=("Arial", 18))
            reserve_lbl.pack(fill='x', pady=20)

            if hasattr(self, 'tree'):
                self.tree.destroy()

            columns = ("Quantity", "Item", "Notes")
            self.tree = ttk.Treeview(self.modifyOrderWindow, columns=columns, show='headings', selectmode='browse')

            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=80, anchor="center")

            self.tree.pack(side='right', fill='both', expand=True)
            self.insert_data(data)

            # self.scrollbar = ttk.Scrollbar(self.modifyOrderWindow, orient='vertical', command=self.tree.yview)
            # self.tree.configure(yscroll=self.scrollbar.set)
            # self.scrollbar.pack(side='right', fill='y')
            
    def clear_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    
    def insert_data(self, data):
        self.clear_table()  # Clears existing data
        for row in data:
            self.tree.insert('', 'end', values=row)  # Insert new data

    def editWindowPopup(self, row_id, column_id):
        self.editWindow = Toplevel(self)
        self.editWindow.title("Edit Cell Value")
        self.editWindow.geometry("300x100")

        # Calculate column index
        self.column_index = int(column_id[1:]) - 1
        self.current_value = self.tree.item(row_id, 'values')[self.column_index]

        self.newValueUI = tk.Entry(self.editWindow)
        self.newValueUI.pack(pady=10)
        self.newValueUI.insert(0, self.current_value)
        
        self.saveEditButton = tk.Button(self.editWindow, text="Save")
        self.saveEditButton.pack()

        
    # def cancelOrder(self, tableNumber):
    #     # if tableNumber in self.tableOrders:
    #     #     self.tableOrders.pop(tableNumber)
    #     #     self.refreshGUI()
    #      self.orderCancelCallback = tableNumber
        
    # def removeOrder(self, tableNumber):
    #     self.tableOrders.pop(tableNumber)
    #     self.refreshGUI()

    def refreshGUI(self):
        self.mainFrame.destroy()
        self.create_main_frame()


    
# if __name__ == "__main__":
#     app = OrdersView(tableOrders)
#     app.mainloop()
