'''
Author: Jevhan Seechurn, Will Griffin, Alex Rogers, Shahbaz Bokhari
Date: 13/12/2023
Version: 1.1
'''

import tkinter as tk
from tkinter import PhotoImage
from sys import platform


class HomeView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='#1A58B5')
        self.topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#2976E9')
        self.topFrame.pack(fill=tk.X)

        # The Label 'Horizon Restaurant'
        self.label = tk.Label(self.topFrame, text="Horizon Restaurant", fg='white', bg='#2976E9', anchor='w', font=('Arial', 25), underline=True)
        self.label.pack(fill=tk.BOTH, expand=True)

        # Underlines the Label 
        self.canvas = tk.Canvas(self.topFrame, height=2, bg='#2976E9', highlightthickness=0)
        self.canvas.create_line(4, 2, 218, 2, width=2, fill='white')
        self.canvas.pack(fill=tk.X)
        
        self.Acc_btn = tk.Button(self.topFrame, text='Account', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.Acc_btn.pack(side=tk.RIGHT, anchor='e')
        self.Acc_btn.place(relx=1.0, rely=0.5, anchor='e', x=-300, y=4)

        # Username
        self.username = tk.Label(self.topFrame, text=f"", fg='white', bg='#2976E9', font=('Arial', 14))
        self.username.pack(side=tk.RIGHT, anchor='e')
        self.username.place(relx=1.0, rely=0.5, anchor='e', x=-120, y=4)

        # User ID
        self.user_id = tk.Label(self.topFrame, text=f"", fg='white', bg='#2976E9', font=('Arial', 14))
        self.user_id.pack(side=tk.RIGHT, anchor='e')
        self.user_id.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

        # Frame for the main menu buttons
        self.menuFrame = tk.Frame(self, bg='#1A58B5')
        self.menuFrame.place(relx=0.5, rely=0.5, anchor='center')
        
        #changes button size based off of platform
        if platform == "win32":
            # Windows
            self.buttonHeight = 7
            self.buttonWidth = 15
        elif platform == "darwin":
            self.buttonHeight = 7
            self.buttonWidth = 25
        else:
            self.buttonHeight = 10
            self.buttonWidth = 25
            
        self.backgorundColor = "#B0B0B0"
        # backgorundColor = "black"
        self.fontColor = "black"
        self.fontDetails = ('Arial', 14)
        
        self.createReservation_btn = tk.Button(self.menuFrame, text='Create reservation',bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.createReservation_btn.grid(row=0, column=0, padx=10, pady=10)

        self.createOrder_btn = tk.Button(self.menuFrame, text='Take Orders', bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.createOrder_btn.grid(row=0, column=1, padx=10, pady=10)

        self.viewOrders_btn = tk.Button(self.menuFrame, text='View Orders', bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.viewOrders_btn.grid(row=0, column=2, padx=10, pady=10)
        
        self.inventory_modify_btn = tk.Button(self.menuFrame, text='Manage Inventory', bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.inventory_modify_btn.grid(row=1, column=0, padx=10, pady=10)

        self.inventory_btn = tk.Button(self.menuFrame, text='View Inventory', bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.inventory_btn.grid(row=1, column=1, padx=10, pady=10)

        self.adminFeatures_btn = tk.Button(self.menuFrame, text='Admin Features', bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.adminFeatures_btn.grid(row=1, column=2, padx=10, pady=10)

        self.reports_btn = tk.Button(self.menuFrame, text='Reports', bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.reports_btn.grid(row=1, column=3, padx=10, pady=10)

        self.menu_edit_btn = tk.Button(self.menuFrame, text='Menu Management', bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.menu_edit_btn.grid(row=1, column=4, padx=10, pady=10)

        self.discount_btn = tk.Button(self.menuFrame, text='Discount Management', bd=0, bg=self.backgorundColor, fg=self.fontColor, font=self.fontDetails, width=self.buttonWidth, height=self.buttonHeight)
        self.discount_btn.grid(row=1, column=4, padx=10, pady=10)

    # Bottom bar 
        self.bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='#2976E9')
        self.bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        self.bottom_label = tk.Label(self.bottomFrame, text="", bg='#2976E9')
        self.bottom_label.pack()

