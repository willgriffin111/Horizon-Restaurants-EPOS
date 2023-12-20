import tkinter as Tk
from tkinter import Toplevel


userName = "Will Griffin"
userId = "193812"
totalDiscount = 0
menuItems = {
    "Starters": ["Starter1", "Starter2", "Starter3", "Starter4"],
    "Mains": ["Main1", "Main2", "Main3", "Main4"],
    "Desserts": ["Dessert1", "Dessert2", "Dessert3", "Dessert4"],
    "Drinks": ["Drink1", "Drink2", "Drink3", "Drink4", "Drink5", "Drink6"]
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
        #self.resizable(False, False)
        self.sidebar()
        self.topbar(userName=userName, userID=userId)
        self.bottombar()
        self.createMenuCategories()
        self.discount_window = None

    # Jevs Button function -----------------------------------------------------------------------------------------------------------------------------------|

    def homeAction(self):
        print("Home button clicked")

    def logOutButton(self):
        print("Logged off")

    def tableButton(self):
        print("Table button clicked")

    # Discount window created (topwindow) ----------------------------------------------------------------------------------------------------------------------|

    def create_discount_window(self):
        self.discount_window = Toplevel(self)
        self.discount_window.title("Discounts")
        self.discount_window.geometry('400x400')
        self.discount_window.configure(bg='#1A58B5')
        self.discount_window.resizable(False, False)
        
        # Frame to hold the buttons
        discountButtonContainer = Tk.Frame(self.discount_window, bg='#1A58B5')

        discountButtonContainer.place(relx=0.5, rely=0.5, anchor='center')

        # Staff discount button
        staff_discount = Tk.Button(discountButtonContainer, text='Staff discount', bg='white', fg='black', padx=10, pady=25, command=self.staff_disc, borderwidth=0, width=12)
        staff_discount.pack(side='top', pady=10)  

        # Seasonal discount button
        # THE IDEA IS TO ONLY SHOW THIS BUTOTN IN THE MONTH OF DECEMBER (SAME FUNCTIONALY AS HOME PAGE BUTTONS, WHERE BUTTONS ONLY SHOW IF AVAILABLE TO USER)
        christmass_discount = Tk.Button(discountButtonContainer, text='Christams discount', bg='white', fg='black', padx=10, pady=25, command=self.christmass_disc, borderwidth=0, width=12)
        christmass_discount.pack(side='top', pady=10)  
        
        '''
        MAYBE ADD DISCOUNT FOR DAY OF THE WEEK
        EG. 10% OFF ON MONDAYS
        '''
        
        # Remove discount button
        remove_discount = Tk.Button(discountButtonContainer, text='Remove discount', bg='white', fg='black', padx=10, pady=25, command=self.remove_disc, borderwidth=0, width=12)
        remove_discount.pack(side='top', pady=10)  
        
       
        

    def discount_btn(self):
        if self.discount_window and self.discount_window.winfo_exists(): 
            self.discount_window.destroy()  
        else:
            self.create_discount_window()
    
    
    def staff_disc(self):
        global totalDiscount
        print('Staff discount applied')
        totalDiscount = 25
        self.updateOrderSummary()
        self.discount_window.destroy()
        
    def christmass_disc(self):
        global totalDiscount
        print('Christmas discount applied')
        totalDiscount = 10
        self.updateOrderSummary()
        self.discount_window.destroy()

    def remove_disc(self):
        global totalDiscount
        print('Discount removed')
        totalDiscount = 0
        self.updateOrderSummary()
        self.discount_window.destroy()


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
        homeButton = Tk.Button(topFrame, text="Home", command=self.homeAction, bd=0, highlightthickness=0, highlightbackground="#2976E9", pady=10, border=None)
        homeButton.place(relx=1.0, rely=0.5, anchor="e", x=3, y=4)

    # Side bar update for discount ----------------------------------------------------------------------------------------------------------------------------------------|
    def updateOrderSummary(self):
        global totalDiscount
        totalItems = 0
        totalPrice = 0.0

        # Calculate total items and price
        for item, details in order.items():
            quantity, pricePerItem = details
            totalItems += quantity
            totalPrice += quantity * pricePerItem

        # Apply discount
        totalPrice *= (1 - totalDiscount / 100)

        # Update the itemList and Summary in the sidebar
        self.itemList.delete(0, Tk.END)
        for item, (quantity, price) in order.items():
            entry = f"{item} x {quantity} - £{price * quantity}"
            self.itemList.insert(Tk.END, entry)

        # Clear and update the Summary Frame
        for widget in self.summaryFrame.winfo_children():
            widget.destroy()

        Tk.Label(self.summaryFrame, text=f"Items: {totalItems}", fg='black', bg="#F0FFFF").pack(side=Tk.LEFT)
        Tk.Label(self.summaryFrame, text=f"Total: £{totalPrice:.2f}", fg='black', bg="#F0FFFF").pack(side=Tk.RIGHT)

    # Window Side bar ----------------------------------------------------------------------------------------------------------------------------------------|
    def sidebar(self):
        self.sidebar = Tk.Frame(self, width=300, height=478, bg="#F0FFFF")
        self.sidebar.pack(fill=Tk.Y, side=Tk.LEFT)

        topBox = Tk.Frame(self.sidebar, bg="#F0FFFF")
        topBox.pack(anchor="nw", padx=10, pady=10)

        logOutButton = Tk.Button(topBox, command=self.logOutButton, text="Log Out", bg="white", padx=10, pady=0, borderwidth=0, highlightthickness=0, height=4, width=10)
        logOutButton.pack(side=Tk.LEFT)

        tableMenu = Tk.OptionMenu(topBox, self.selected_table, *tables, command=self.selectedTableChanged)
        tableMenu.config(bg="#F0FFFF", padx=10, pady=0, borderwidth=0, highlightthickness=0, height=0, width=0, fg='black')
        tableMenu["menu"].config(bg="#F0FFFF")
        tableMenu.pack(side=Tk.LEFT)

        posFrame = Tk.Frame(self.sidebar, bg="#F0FFFF", borderwidth=0, highlightthickness=0)
        posFrame.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)

        self.itemList = Tk.Listbox(posFrame, bg="#F0FFFF", fg='black')
        self.itemList.pack(fill=Tk.BOTH, expand=True)

        self.summaryFrame = Tk.Frame(posFrame, bg="#F0FFFF")
        self.summaryFrame.pack(fill=Tk.BOTH, expand=True)

        self.updateOrderSummary()

        payButton = Tk.Button(self.sidebar, text="Pay", bg="#F0FFFF", fg="black", borderwidth=0, width=4, height=3)
        payButton.place(x=4, y=535)

        discount = Tk.Button(self.sidebar, text="Discount", bg="#F0FFFF", fg="black", borderwidth=0, width=4, height=3, command=self.discount_btn)
        discount.place(x=84, y=535)

        modify = Tk.Button(self.sidebar, text="Modify", bg="#F0FFFF", fg="black", borderwidth=0, width=4, height=3)
        modify.place(x=164, y=535)
    
    def selectedTableChanged(self, selectedValue):
        '''
        THE updateOrderSummary FUNCTION WILL NEED TO BE CALLED HERE TO UPDATE THE ORDER LIST FOR THE NEW TABLE
        '''
        print(selectedValue)

        
    def createMenuCategories(self):
        self.menuFrame = Tk.Frame(self, bg="#1A58B5")
        self.menuFrame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=True)

        # Grid layout for category buttons
        gridFrame = Tk.Frame(self.menuFrame, bg="#1A58B5")
        gridFrame.pack(pady=10)

        self.categoryButtons = {}

# Inside the createMenuCategories method --------------------------------------------------------------------------------------------------------------------------|

        categories = ["Starters", "Mains", "Desserts", "Drinks"]
        # Starters Button


        startersButton = Tk.Button(gridFrame, text="Starters", command=lambda: self.displayCategoryOptions("Starters"), width=10, height=5,borderwidth=0)
        startersButton.grid(row=0, column=0, padx=5, pady=5)
        self.categoryButtons["Starters"] = startersButton

        # Mains Button
        mainsButton = Tk.Button(gridFrame, text="Mains", command=lambda: self.displayCategoryOptions("Mains"), width=10, height=5,borderwidth=0, background="white")
        mainsButton.grid(row=0, column=1, padx=5, pady=5)
        self.categoryButtons["Mains"] = mainsButton

        # Desserts Button
        dessertsButton = Tk.Button(gridFrame, text="Desserts", command=lambda: self.displayCategoryOptions("Desserts"), width=10, height=5,borderwidth=0)
        dessertsButton.grid(row=0, column=2, padx=5, pady=5)
        self.categoryButtons["Desserts"] = dessertsButton

        # Drinks Button
        drinksButton = Tk.Button(gridFrame, text="Drinks", command=lambda: self.displayCategoryOptions("Drinks"), width=10, height=5,borderwidth=0)
        drinksButton.grid(row=0, column=3, padx=5, pady=5)
        self.categoryButtons["Drinks"] = drinksButton 


        self.optionsFrame = Tk.Frame(self.menuFrame, bg="#1A58B5")
        self.optionsFrame.pack(fill=Tk.BOTH, expand=True)

    def displayCategoryOptions(self, category):
        # Clear previous options
        for widget in self.optionsFrame.winfo_children():
            widget.destroy()

        # Fetch options for the selected category
        options = menuItems.get(category, [])

        for index, option in enumerate(options):
            row = index // 3  # Calculate the row number
            col = index % 3  # Calculate the column number

            optionButton = Tk.Button(self.optionsFrame, text=option, width=26, height=7, command=self.selectedCategoryOptions(category,option),borderwidth=0)
            optionButton.grid(row=row, column=col, padx=10, pady=5)

        # Configure column weights to ensure buttons expand to fill the frame
        for i in range(3):
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
    
        # Bottom bar -----------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        bottomFrame = Tk.Frame(self, borderwidth=7, relief=Tk.FLAT, bg='#2976E9')
        bottomFrame.pack(fill=Tk.X, side=Tk.BOTTOM)
        bottom_label = Tk.Label(bottomFrame, text="", bg='#2976E9')
        bottom_label.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()