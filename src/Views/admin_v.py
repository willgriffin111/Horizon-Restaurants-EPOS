'''
Author: Jevhan Seechurn, Alex Rogers
Date: 18/12/2023
Version: 1.1
'''

import tkinter as tk
from tkinter import PhotoImage

class AdminView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='#F0FFFF')


        #top bar
        self.topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        self.topFrame.pack(fill=tk.X)

        self.label = tk.Label(self.topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        self.label.pack(fill=tk.BOTH, expand=True)

        self.top_underline = tk.Canvas(self.topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        self.top_underline.create_line(4, 2, 218, 2, width=2, fill='white')
        self.top_underline.pack(fill=tk.X)

        self.username = tk.Label(self.topFrame, text="hi", fg='white', bg='#1A1A1A', font=('Arial', 14))
        self.username.pack(side=tk.RIGHT, anchor='e')
        self.username.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        self.user_id = tk.Label(self.topFrame, text="hi", fg='white', bg='#1A1A1A', font=('Arial', 14))
        self.user_id.pack(side=tk.RIGHT, anchor='e')
        self.user_id.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

        #side bar
        self.Sidebar = tk.Frame(self, height=478, bg='#474747')
        self.Sidebar.pack(fill=tk.Y, side=tk.LEFT)

        self.side_label = tk.Label(self.Sidebar,text="Admin Features",fg='white', bg='#474747', anchor='w', font=('Arial', 18),width=13)
        self.side_label.pack(padx=45,pady=15)


        self.staff_edit_btn = tk.Button(self.Sidebar, text='Staff Edit', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.staff_edit_btn.pack(pady=30)

        self.menu_edit_btn = tk.Button(self.Sidebar, text='Menu Edit', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.menu_edit_btn.pack(pady=30)

        self.home_btn = tk.Button(self.Sidebar, text='Home', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.home_btn.pack(pady=30)

        #bottom bar
        self.bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        self.bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        self.bottom_label = tk.Label(self.bottomFrame, text="", bg='#1A1A1A')
        self.bottom_label.pack()

