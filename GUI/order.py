import tkinter as Tk

userName = "Will Griffin"
userId = "193812"

menuItems = {
    "Starters": ["Starter1", "Starter2", "Starter3", "Starter4"],
    "Mains": ["Main1", "Main2", "Main3", "Main4"],
    "Desserts": ["Dessert1", "Dessert2", "Dessert3", "Dessert4"],
    "Drinks": ["Drink1", "Drink2", "Drink3", "Drink4"]
}

class App(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Order Page")
        self.configure(bg="#1A58B5")
        self.sidebar()
        self.topbar(userName=userName, userID=userId)
        self.createMenuCategories()
        # self.bottombar()

    # Button function
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

        tableButton = Tk.Button(topBox, command=self.tableButton, text="Table", bg="white", padx=10, pady=0, borderwidth=0, highlightthickness=0, height=4, width=10)
        tableButton.pack(side=Tk.LEFT)  # Aligns the Table button to the left next to Log Out button
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
        print(options)

        for index, option in enumerate(options):
            row = index // 2  # Calculate the row number
            col = index % 2  # Calculate the column number

            optionButton = Tk.Button(self.optionsFrame, text=option, width=26, height=4)
            optionButton.grid(row=row, column=col, padx=10, pady=5)

        # Configure column weights to ensure buttons expand to fill the frame
        for i in range(2):
            self.optionsFrame.grid_columnconfigure(i, weight=1)

    def bottombar(self):
        bottomFrame = Tk.Frame(self, borderwidth=7, relief=Tk.FLAT, bg="#2976E9")
        bottomFrame.pack(fill=Tk.X, side=Tk.BOTTOM)
        bottomLabel = Tk.Label(bottomFrame, text="", bg="#2976E9")
        bottomLabel.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
