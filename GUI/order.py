import tkinter as Tk

userName = "Will Griffin"
userId = "193812"

menuItems = {
    "Starters": ["Starter1", "Starter2", "Starter3", "Starter4"],
    "Mains": ["Main1", "Main2", "Main3", "Main4"],
    "Desserts": ["Dessert1", "Dessert2", "Dessert3", "Dessert4"],
    "Drinks": ["Drink1", "Drink2", "Drink3", "Drink4"]
}

tables = ["Table 1", "Table 2", "Table 3"]  

# FIRST ITEM IS THE ITEM NAME, SECOND IS THE QUANTITY, THIRD IS PRICE
order = {
            "Starter 1": (1, 6.50),
            "Main 3": (2, 10.00),
            "Dessert 5": (1, 4.50)
        }
'''
Example of implentaion

menuItems = {
    "SELECT category FROM MENU": ["SELECT menuItem FROM MENU WHERE category IS 'Starters'"],
    "SELECT category FROM MENU": ["SELECT menuItem FROM MENU WHERE category IS 'Mains'"],
    "SELECT category FROM MENU": ["SELECT menuItem FROM MENU WHERE category IS 'Desserts'"],
    "SELECT category FROM MENU": ["SELECT menuItem FROM MENU WHERE category IS 'Drinks'"]
}

tables = ["SELECT tableNumber FROM TABLE"] 

order = {
    "SELECT menuItem FROM ORDER WHERE tableNumber FROM Tabel IS 1": (SELECT , 6.50),
    "SELECT menuItem FROM ORDER WHERE tableNumber FROM Tabel IS 2": (2, 10.00),
    "SELECT menuItem FROM ORDER WHERE tableNumber FROM Tabel IS 3": (1, 4.50)
}
    
'''

class App(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Order Page")
        self.configure(bg="#1A58B5")

        self.selected_table = Tk.StringVar()
        self.selected_table.set(tables[0])  # Set the default value
        self.resizable(False, False)
        self.sidebar()
        self.topbar(userName=userName, userID=userId)
        self.createMenuCategories()

    # Jevs Button function
    def homeAction(self):
        print("Home button clicked")

    def logOutButton(self):
        print("Logged off")

    def tableButton(self):
        print("Table button clicked")

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
        homeButton = Tk.Button(topFrame, text="Home", command=self.homeAction, bd=0, highlightthickness=0, highlightbackground="#2976E9", pady=10, border=None)
        homeButton.place(relx=1.0, rely=0.5, anchor="e", x=3, y=4)

    def sidebar(self):
        sidebar = Tk.Frame(self, width=300, height=478, bg="#F0FFFF")
        sidebar.pack(fill=Tk.Y, side=Tk.LEFT)

        topBox = Tk.Frame(sidebar, bg="grey")
        topBox.pack(anchor="nw", padx=10, pady=10)

        logOutButton = Tk.Button(topBox, command=self.logOutButton, text="Log Out", bg="white", padx=10, pady=0, borderwidth=0, highlightthickness=0, height=4, width=10)
        logOutButton.pack(side=Tk.LEFT)  # Aligns the Log Out button to the left

        # tableButton = Tk.Button(topBox, command=self.tableButton, text="Table", bg="white", padx=10, pady=0, borderwidth=0, highlightthickness=0, height=4, width=10)
        # tableButton.pack(side=Tk.LEFT)  # Aligns the Table button to the left next to Log Out button
        # Dropdown menu for tables
        
        tableMenu = Tk.OptionMenu(topBox, self.selected_table, *tables, command=self.getSelectedTable)
        tableMenu.config(bg="white", padx=10, pady=0, borderwidth=0, highlightthickness=0, height=4, width=5)
        tableMenu["menu"].config(bg="black")
        tableMenu.pack(side=Tk.LEFT)  
        
        # Add a frame for the POS system interface
        posFrame = Tk.Frame(sidebar, bg="white")
        posFrame.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)

        # Add a label and entry for item listing, quantity, and price
        self.itemList = Tk.Listbox(posFrame)
        self.itemList.pack(fill=Tk.BOTH, expand=True)

        for item, (quantity, price) in order.items():
            entry = f"{item} x {quantity} - £{price * quantity}"
            self.itemList.insert(Tk.END, entry)

        # Summary of the order
        summaryFrame = Tk.Frame(posFrame, bg="#E8E8E8")
        summaryFrame.pack(fill=Tk.BOTH, expand=True)

        totalItems = 0
        totalPrice = 0.0

        # Loop through each order item to calculate the total items and total price
        for item, details in order.items():
            quantity, pricePerItem = details
            totalItems += quantity
            totalPrice += quantity * pricePerItem

        Tk.Label(summaryFrame, text=f"Items: {totalItems}", bg="#E8E8E8").pack(side=Tk.LEFT)
        Tk.Label(summaryFrame, text=f"Total: £{totalPrice}", bg="#E8E8E8").pack(side=Tk.RIGHT)

        # Add buttons for actions
        buttonsFrame = Tk.Frame(posFrame, bg="#E8E8E8")
        buttonsFrame.pack(fill=Tk.BOTH, expand=True, pady=5)

        # deleteButton = Tk.Button(buttonsFrame, text="Delete", bg="red", fg="white")
        # deleteButton.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=True)

        # modifyButton = Tk.Button(buttonsFrame, text="Modify", bg="gray", fg="white")
        # modifyButton.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=True)

        payButton = Tk.Button(buttonsFrame, text="Pay", bg="green", fg="black")
        payButton.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=True)

    
    def getSelectedTable(self, selectedValue):
        print(selectedValue)

        
    def createMenuCategories(self):
        self.menuFrame = Tk.Frame(self, bg="#1A58B5")
        self.menuFrame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=True)

        # Grid layout for category buttons
        gridFrame = Tk.Frame(self.menuFrame, bg="#1A58B5")
        gridFrame.pack(pady=10)

        self.categoryButtons = {}

        # Starters Button
        startersButton = Tk.Button(gridFrame, text="Starters", command=lambda: self.displayCategoryOptions("Starters"), width=13, height=5)
        startersButton.grid(row=0, column=0, padx=5, pady=5)
        self.categoryButtons["Starters"] = startersButton

        # Mains Button
        mainsButton = Tk.Button(gridFrame, text="Mains", command=lambda: self.displayCategoryOptions("Mains"), width=13, height=5)
        mainsButton.grid(row=0, column=1, padx=5, pady=5)
        self.categoryButtons["Mains"] = mainsButton

        # Desserts Button
        dessertsButton = Tk.Button(gridFrame, text="Desserts", command=lambda: self.displayCategoryOptions("Desserts"), width=13, height=5)
        dessertsButton.grid(row=0, column=2, padx=5, pady=5)
        self.categoryButtons["Desserts"] = dessertsButton

        # Drinks Button
        drinksButton = Tk.Button(gridFrame, text="Drinks", command=lambda: self.displayCategoryOptions("Drinks"), width=13, height=5)
        drinksButton.grid(row=0, column=3, padx=5, pady=5)
        self.categoryButtons["Drinks"] = drinksButton

        self.optionsFrame = Tk.Frame(self.menuFrame, bg="systemTransparent")
        self.optionsFrame.pack(fill=Tk.BOTH, expand=True)

    def displayCategoryOptions(self, category):
        # Clear previous options
        for widget in self.optionsFrame.winfo_children():
            widget.destroy()

        # Fetch options for the selected category
        options = menuItems.get(category, [])

        for index, option in enumerate(options):
            row = index // 2  # Calculate the row number
            col = index % 2  # Calculate the column number

            optionButton = Tk.Button(self.optionsFrame, text=option, width=26, height=4, command=self.selectedCategoryOptions(category,option))
            optionButton.grid(row=row, column=col, padx=10, pady=5)

        # Configure column weights to ensure buttons expand to fill the frame
        for i in range(2):
            self.optionsFrame.grid_columnconfigure(i, weight=1)

    def selectedCategoryOptions(self, category, item):
        def inner():  
            print(f"Selected Item: {item} in Category: {category} for Table: {self.selected_table.get()}")
            ''' 
            HERE IS WHERE WE WILL ADD THE ITEM TO THE ORDER IN THE DATABASE
            WE ENTER TABLE NUMBER, ITEM, QUANTITY
            USING THE VARIABLES
            
            self.selected_table.get() = TABLE NUMBER
            item = ITEM
            quantity = 1, as pressed once. If pressed twise the item will be added again under the same table number and will be shown the left x2
            
            WILL ALSO NEED A AUTO REFRESH FUNCTION TO UPDATE THE ORDER LIST
            '''
        return inner



if __name__ == "__main__":
    app = App()
    app.mainloop()

