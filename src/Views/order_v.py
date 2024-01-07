import tkinter as Tk
from tkinter import Toplevel, Frame, ttk
import copy


userName = "Will Griffin"
userId = "193812"
totalDiscount = 0
menuItems = {
    "Starters": ["Starter1", "Starter2", "Starter3", "Starter4"],
    "Mains": ["Main1", "Main2", "Main3", "Main4"],
    "Desserts": ["Dessert1", "Dessert2", "Dessert3", "Dessert4"],
    "Drinks": ["Drink1", "Drink2", "Drink3", "Drink4", "Drink5"],
    "LOLOLOL": ["asodasda", "sadasdas"]
}

tables = ["Select Table", "Table 1", "Table 2", "Table 3"]  

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

class OrderCreate(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.geometry("800x600")
        #self.title("Order Page")
        self.configure(bg="#1A58B5")
        self.menu = {}
        self.order = {}
        self.categoryButtons = {}
        self.total_discount = 0
        self.selected_table = Tk.StringVar()
        self.selected_table.set(tables[0])  # Set the default value
        self.sidebar()
        self.topbar()
        self.bottombar()
        self.discount_window = None
        self.create_menu_categories()

    def setOrder(self, order):
        self.order = order
        

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
        
        self.discount_window.rowconfigure((0, 1), weight=1)
        self.discount_window.columnconfigure(0, weight=1)

        self.top_frame = Frame(self.discount_window, borderwidth=25, relief=Tk.FLAT, bg='#2976E9')
        self.top_frame.pack(side="top", fill="both")

        self.apply_discount_button = Tk.Button(self.top_frame, text='Apply', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None)
        self.apply_discount_button.pack(side="left", fill="both", expand=True, padx=2)

        self.apply_staff_discount_button = Tk.Button(self.top_frame, text='Staff', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None)
        self.apply_staff_discount_button.pack(side="left", fill="both", expand=True, padx=2)

        self.remove_discount_button = Tk.Button(self.top_frame, text='Remove', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, command=self.remove_discount)
        self.remove_discount_button.pack(side="left", fill="both", expand=True, padx=2)

        self.view_discounts_tree_view()
    
    def view_discounts_tree_view(self):
        self.discount_table_frame = Frame(self.discount_window, borderwidth=25, relief=Tk.FLAT, bg='#1A58B5', height=300, width=480)
        self.discount_table_frame.pack(side="bottom", fill="both", expand=True)
        
        self.view_discount_tree = ttk.Treeview(self.discount_table_frame,height=15)
        self.view_discount_tree['columns'] = ("name", "value")
        column_width = 120

        # Formatting columns
        self.view_discount_tree.column("#0", width=0, minwidth=0)
        self.view_discount_tree.column("name", anchor='w', width=column_width, minwidth=column_width)
        self.view_discount_tree.column("value", anchor='w', width=column_width, minwidth=column_width)

        # Formatting Headers 
        self.view_discount_tree.heading("name", text="Discount Name",anchor='center')
        self.view_discount_tree.heading("value", text="Value (%)",anchor='center')

        # Add tag configurations for odd and even rows
        self.view_discount_tree.tag_configure('oddrow', background='white', foreground='black')
        self.view_discount_tree.tag_configure('evenrow', background='lightgray', foreground='black')

        self.view_discount_tree.pack(side='left', expand=True)
    
    def clear_view_discounts_tree_view(self):
        # Clear existing rows in the treeview
        for row in self.view_discount_tree.get_children():
            self.discount_tree.delete(row)
    
    def insert_tree_view(self, data):
        # Populate treeview with updated data
        count = 0
        for record in data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'  # Give alternating colors to rows

            self.view_discount_tree.insert(parent='', index='end', iid=count, text="", values=record, tags=(tag,))
            count += 1

    def remove_discount(self):
        print('Discount removed')
        self.total_discount = 0
        self.updateOrderSummary()
        self.discount_window.destroy()
    
    def enter_staff_ID_popup(self):
        self.enter_staff_ID_window = Toplevel(self)
        self.enter_staff_ID_window.title("Staff Discount")
        self.enter_staff_ID_window.geometry("300x100")

        self.staff_ID_entry = Tk.Entry(self.enter_staff_ID_window)
        self.staff_ID_entry.pack(pady=10)
        
        self.submit_staff_ID_button = Tk.Button(self.enter_staff_ID_window, text="Submit")
        self.submit_staff_ID_button.pack()

    def create_discount_popup(self):
        if self.discount_window and self.discount_window.winfo_exists(): 
            self.discount_window.destroy()  
        else:
            self.create_discount_window()      

    # Top bar of window --------------------------------------------------------------------------------------------------------------------------------------|
    
    def topbar(self):
        self.topFrame = Tk.Frame(self, borderwidth=25, relief=Tk.FLAT, bg="#2976E9")
        self.topFrame.pack(fill=Tk.X)

        self.label = Tk.Label(self.topFrame, text="Horizon Restaurant", fg="white", bg="#2976E9", anchor="w", font=("Arial", 16), underline=True)
        self.label.pack(fill=Tk.BOTH, expand=True)

        self.topUnderline = Tk.Canvas(self.topFrame, height=2, bg="#2976E9", highlightthickness=0)
        self.topUnderline.create_line(4, 2, 143, 2, width=2, fill="white")
        self.topUnderline.pack(fill=Tk.X)

        self.username = Tk.Label(self.topFrame, fg="white", bg="#2976E9", font=("Arial", 12))
        self.username.pack(side=Tk.RIGHT, anchor="e")
        self.username.place(relx=1.0, rely=0.5, anchor="e", x=-170, y=4)

        self.user_id = Tk.Label(self.topFrame, fg="white", bg="#2976E9", font=("Arial", 12))
        self.user_id.pack(side=Tk.RIGHT, anchor="e")
        self.user_id.place(relx=1.0, rely=0.5, anchor="e", x=-90, y=4)

        # Home Button
        self.homeButton = Tk.Button(self.topFrame, text="Home", bd=0, highlightthickness=0, highlightbackground="#2976E9", pady=10, border=None)
        self.homeButton.place(relx=1.0, rely=0.5, anchor="e", x=3, y=4)

    # Side bar update for discount ----------------------------------------------------------------------------------------------------------------------------------------|
    def updateOrderSummary(self, category=None, menuItem=None, table=None):
        print("updated order summary")
        
        category = category or ""
        menuItem=menuItem or {}
        table = table or ""
        totalItems = 0
        totalPrice = 0.0
        defaultQuantity = 1

        
        if menuItem:
            menuItem['category'] = category
            key = menuItem.get('name', None)
            if key is not None:
                # If the menuItem is already in the order, update the quantity, otherwise just set the default quantity of 1
                if key in self.order:
                    self.order[key]['quantity'] += defaultQuantity
                else:
                    newMenuItem = copy.deepcopy(menuItem)
                    newMenuItem['quantity'] = defaultQuantity
                    self.order[key] = newMenuItem
        
        self.updateWidgets()
        print(f"Order Page, order = {self.order}\n")

    def updateWidgets(self):
        # Calculate total items and price
        totalItems = sum(item['quantity'] for item in self.order.values())
        self.total_price = sum(item['price'] * item['quantity'] for item in self.order.values())

        # Apply discount
        self.discount_amount = self.total_price * (self.total_discount / 100)
        self.discounted_price = self.total_price - self.discount_amount

        # Update the itemList and Summary in the sidebar
        self.itemList.delete(0, Tk.END)
        for item in self.order.values():
            if item['description'] is not None and item['description'] != '':
                entry = f"{item['name']} x {item['quantity']} - £{item['price'] * item['quantity']:.2f} <-desc"
                self.itemList.insert(Tk.END, entry)
            else:
                entry = f"{item['name']} x {item['quantity']} - £{item['price'] * item['quantity']:.2f}"
                self.itemList.insert(Tk.END, entry)

        # Clear and update the Summary Frame
        for widget in self.summaryFrame.winfo_children():
            widget.destroy()

        Tk.Label(self.summaryFrame, text=f"Items: {totalItems}", fg='black', bg="#F0FFFF").pack(padx=10, pady=5, anchor='w')
        Tk.Label(self.summaryFrame, text=f"Discounted: -£{self.discount_amount:.2f}", fg='black', bg="#F0FFFF").pack(padx=10, pady=5, anchor='w')
        Tk.Label(self.summaryFrame, text=f"Total: £{self.discounted_price:.2f}", fg='black', bg="#F0FFFF").pack(padx=10, pady=5, anchor='w')
    # Window Side bar ----------------------------------------------------------------------------------------------------------------------------------------|
    def sidebar(self):
        self.sidebar = Tk.Frame(self, width=300, height=478, bg="#F0FFFF")
        self.sidebar.pack(fill=Tk.Y, side=Tk.LEFT)

        self.sidebar.columnconfigure(0, weight=1)
        self.sidebar.rowconfigure((0, 2), weight=1)
        self.sidebar.rowconfigure(1, weight=50)

        topBox = Tk.Frame(self.sidebar, bg="#F0FFFF")
        topBox.columnconfigure((0,1), weight=1)
        topBox.rowconfigure(0, weight=1)
        topBox.grid(column=0, row=0, padx=10, pady=10)


        tableMenu = Tk.OptionMenu(topBox, self.selected_table, *tables, command=self.selectedTableChanged)
        tableMenu.config(bg="#F0FFFF", borderwidth=0, highlightthickness=0, fg='black')
        tableMenu["menu"].config(bg="#F0FFFF")
        tableMenu.grid(column=1,row=0, sticky='nswe')

        posFrame = Tk.Frame(self.sidebar, bg="#F0FFFF", borderwidth=0, highlightthickness=0)
        #posFrame.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)
        posFrame.grid(column=0, row=1, sticky='nsew', padx=10, pady=10)
        posFrame.columnconfigure(0, weight=1)
        posFrame.rowconfigure(0, weight=1)
        posFrame.rowconfigure(1, weight=1)

        self.itemList = Tk.Listbox(posFrame, bg="#F0FFFF", fg='black')
        #self.itemList.pack(fill=Tk.BOTH, expand=True)
        self.itemList.grid(column=0, row=0, sticky='nsew')

        self.summaryFrame = Tk.Frame(posFrame, bg="#F0FFFF")
        self.summaryFrame.grid(column=0, row=1, sticky='nswe')
        self.summaryFrame.columnconfigure((0, 1), weight=1)
        self.summaryFrame.rowconfigure(0, weight=1)

        self.updateOrderSummary()


        self.buttonFrame = Tk.Frame(self.sidebar, bg="#F0FFFF")
        self.buttonFrame.grid(column=0, row=2, sticky='new')
        self.buttonFrame.columnconfigure((0,1,2), weight=1)
        self.buttonFrame.rowconfigure(0, weight=1)

        self.pay_button = Tk.Button(self.buttonFrame, text="Pay", bg="#F0FFFF", fg="black", borderwidth=0, width=4, height=3)
        self.pay_button.grid(row=0, column=0,sticky='new')

        self.view_discount_button = Tk.Button(self.buttonFrame, text="Discount", bg="#F0FFFF", fg="black", borderwidth=0, width=4, height=3)
        self.view_discount_button.grid(row=0, column=1,sticky='new')

        self.modify = Tk.Button(self.buttonFrame, text="Modify", bg="#F0FFFF", fg="black", borderwidth=0, width=4, height=3)
        self.modify.grid(row=0, column=2,sticky='new')
    
    def selectedTableChanged(self, selectedValue):
        '''
        THE updateOrderSummary FUNCTION WILL NEED TO BE CALLED HERE TO UPDATE THE ORDER LIST FOR THE NEW TABLE
        '''
        self.updateOrderSummary(table=selectedValue) # thank you Will that comment is a life saver

        
    def create_menu_categories(self, menu=None):
        self.menu = menu or {}
        self.menuFrame = Tk.Frame(self, bg="#1A58B5")
        self.menuFrame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=True)

        # Grid layout for category buttons
        self.gridFrame = Tk.Frame(self.menuFrame, bg="#1A58B5")
        self.gridFrame.pack(pady=10)


# Inside the createMenuCategories method --------------------------------------------------------------------------------------------------------------------------|
                 # Loop through categories and create buttons
        for col, (category, menuItems) in enumerate(self.menu.items()):
            self.category_button = Tk.Button(self.gridFrame, text=category, width=10, height=5, borderwidth=0, command=lambda c=category, m=menuItems: self.displayCategoryOptions(c, m))
            self.category_button.grid(row=0, column=col, padx=5, pady=5, sticky='w')
            print(col)
            # self.categoryButtons[category] = category_button


        self.optionsFrame = Tk.Frame(self.menuFrame, bg="#1A58B5")
        self.optionsFrame.pack(fill=Tk.BOTH, expand=True)
    
    def clear_menu_categories(self):
        for widget in self.menuFrame.winfo_children():
            widget.destroy()
        
        self.menuFrame.destroy()

    def displayCategoryOptions(self, category, menuItems):
        # Clear previous options
        print(f"\nDisplaying options for category: {category}")
        print("Menu items:", menuItems)

        for widget in self.optionsFrame.winfo_children():
            widget.destroy()
        for index, option in enumerate(menuItems):
            row = index // 3  # Calculate the row number
            col = index % 3  # Calculate the column number
            optionButton = Tk.Button(self.optionsFrame, text=option['name'], width=26, height=7,borderwidth=0, command=lambda c=category, o=option: self.updateOrderSummary(category=c, menuItem=o))
            optionButton.grid(row=row, column=col, padx=10, pady=5)


        # Configure column weights to ensure buttons expand to fill the frame
        for i in range(3):
            self.optionsFrame.grid_columnconfigure(i, weight=1)
    
    def optionSelected(self, category, option):
        print(f"Option selected: Category={category}, Option={option}")


    # def selectedCategoryOptions(self, category, item):
    #     def inner():  
    #         print(f"Selected Item: {item} in Category: {category} for Table: {self.selected_table.get()}")
    #         ''' 
    #         HERE IS WHERE WE WILL ADD THE ITEM TO THE ORDER IN THE DATABASE
    #         WE ENTER TABLE NUMBER, ITEM, QUANTITY
    #         USING THE VARIABLES
            
    #         self.selected_table.get() = TABLE NUMBER
    #         item = ITEM
    #         quantity = 1, as pressed once. If pressed twise the item will be added again under the same table number and will be shown the left x2
            
    #         WILL ALSO NEED A AUTO REFRESH FUNCTION TO UPDATE THE ORDER LIST
    #         '''
    #     return inner
    
        # Bottom bar -----------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        bottomFrame = Tk.Frame(self, borderwidth=7, relief=Tk.FLAT, bg='#2976E9')
        bottomFrame.pack(fill=Tk.X, side=Tk.BOTTOM)
        bottom_label = Tk.Label(bottomFrame, text="", bg='#2976E9')
        bottom_label.pack()


if __name__ == "__main__":
    app = OrderCreate()
    app.mainloop()
