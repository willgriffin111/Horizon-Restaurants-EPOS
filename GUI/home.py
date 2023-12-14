'''
Auther Jevhan Seechurn, Will Griffin
Date: 13/12/2023 3am lmao
Version: 1.0
'''

import tkinter as tk
from tkinter import PhotoImage

userName = "Will Griffin"
userId = "193812"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('Horizon Restaurant')
        self.configure(bg='#1A58B5')
        self.topbar(userName=userName, userID=userId)
        self.main_menu()
        self.bottombar()

    def topbar(self, userName, userID):
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
        username = tk.Label(topFrame, text=f" User: {userName} ", fg='white', bg='#2976E9', font=('Arial', 14))
        username.pack(side=tk.RIGHT, anchor='e')
        username.place(relx=1.0, rely=0.5, anchor='e', x=-350, y=4)

        # User ID
        user_id = tk.Label(topFrame, text=f"ID: {userId}", fg='white', bg='#2976E9', font=('Arial', 14))
        user_id.pack(side=tk.RIGHT, anchor='e')
        user_id.place(relx=1.0, rely=0.5, anchor='e', x=-260, y=4)
    
    def createReservation(self):
        print("Reservation button clicked")
    def createOrder(self):    
        print("Take Order button clicked")
    def viewOrders(self):
        print("View Orders button clicked")
    def modifyOrders(self):
        print("Modify Orders button clicked")
    def adminFeatures(self):
        print("Admin Features button clicked")
    def reports(self):
        print("Reports button clicked")
        
    

    def main_menu(self):
        # Frame for the main menu buttons
        menuFrame = tk.Frame(self, bg='#1A58B5')
        menuFrame.place(relx=0.5, rely=0.5, anchor='center')
        
        buttonHeight = 10
        buttonWidth = 25
        backgorundColor = "#B0B0B0"
        # backgorundColor = "black"
        fontColor = "white"
        fontDetails = ('Arial', 14)
        
        createReservation = tk.Button(menuFrame, text='Create reservation', command=self.createReservation ,bd=0, bg=backgorundColor, fg=fontColor, font=fontDetails, width=buttonWidth, height=buttonHeight)
        createReservation.grid(row=0, column=0, padx=10, pady=10)

        createOrder = tk.Button(menuFrame, text='Take Orders',command=self.createOrder, bd=0, bg=backgorundColor, fg=fontColor, font=fontDetails, width=buttonWidth, height=buttonHeight)
        createOrder.grid(row=0, column=1, padx=10, pady=10)

        viewOrders = tk.Button(menuFrame, text='View Orders',command=self.viewOrders, bd=0, bg=backgorundColor, fg=fontColor, font=fontDetails, width=buttonWidth, height=buttonHeight)
        viewOrders.grid(row=0, column=2, padx=10, pady=10)
        
        modifyOrders = tk.Button(menuFrame, text='Modify Orders',command=self.modifyOrders, bd=0, bg=backgorundColor, fg=fontColor, font=fontDetails, width=buttonWidth, height=buttonHeight)
        modifyOrders.grid(row=1, column=0, padx=10, pady=10)

        adminFeatures = tk.Button(menuFrame, text='Admin Features',command=self.adminFeatures, bd=0, bg=backgorundColor, fg=fontColor, font=fontDetails, width=buttonWidth, height=buttonHeight)
        adminFeatures.grid(row=1, column=1, padx=10, pady=10)

        reports = tk.Button(menuFrame, text='Reports', bd=0,command=self.reports, bg=backgorundColor, fg=fontColor, font=fontDetails, width=buttonWidth, height=buttonHeight)
        reports.grid(row=1, column=2, padx=10, pady=10)

    # Bottom bar 
    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='#2976E9')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#2976E9')
        bottom_label.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()