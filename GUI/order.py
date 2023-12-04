""" 
AUTHOR : WILL GRIFFIN
DATE : 29/11/2023
VERSION : 1.0
"""
import tkinter as tk



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('Horizon Restaurant')
        self.configure(bg='#2976E9')
        self.create_widgets()

    def create_widgets(self):
        # Creating frames with proper assignment
        leftContainer = tk.Frame(self, bg="white")
        rightContainer = tk.Frame(self, bg='#1A58B5')

        # Positioning frames
        leftContainer.grid(row=0, column=0, sticky='nsew')
        rightContainer.grid(row=0, column=1, sticky='nsew')

        # Configuring grid layout to expand containers
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        #  LEFT CONTAINER
        # Configure the column weights for leftContainer
        leftContainer.grid_columnconfigure(0, weight=1)
        leftContainer.grid_columnconfigure(1, weight=1)

        # Creating buttons
        leftContainerButtonLogOut = tk.Button(leftContainer, text="Log out", fg='black', font=('inter', 15), height=4, width=10)
        leftContainerButtonTables = tk.Button(leftContainer, text="Tables", fg='black', font=('inter', 15), height=4, width=10)
        
        # leftContainerTest = tk.Label(leftContainer, text="Test", fg='black', font=('inter', 15), height=3, width=10)
        # leftContainerTest.pack(fill='x', pady=5)

        # Positioning buttons at the top
        leftContainerButtonLogOut.grid(row=0, column=0, sticky='nsew')
        leftContainerButtonTables.grid(row=0, column=1, sticky='nsew')
        
        # RIGHT CONTAINER
        rightContainerTitle = tk.Label(rightContainer, text="Horizon Restaurant", fg='white', bg="#2976E9", font=('inter', 20), height=2)
        rightContainerUserDetails = tk.Label(rightContainer, text="User details", fg='white', bg="#2976E9", font=('inter', 15))
        rightContainerSearch = tk.Entry(rightContainer, width=30, font=('inter', 15))
        
        rightContainerTitle.grid(row=0, column=0, sticky='nsew')
        rightContainerUserDetails.grid(row=1, column=0, sticky='nsew')
        rightContainerSearch.grid(row=0, column=1, rowspan=2, sticky='nsew')

    def logout(self):
        print("Logged out")
    
    def tables(self):
        print("Tables")

if __name__ == "__main__":
    app = App()
    app.mainloop()
