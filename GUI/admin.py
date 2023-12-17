'''
Auther Jevhan Seechurn,
Date: 13/12/2023 3am lmao
Version: 1.0
'''

import tkinter as tk
from tkinter import PhotoImage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('Admin Feature')
        self.configure(bg='#F0FFFF')
        self.topbar()
        self.bottombar()
        self.Sidebar()

    # button functions
    def staff_edit(self):
        print("staff edit button clicked")

    def menu_edit(self):
        print("menu edit button clicked")

    def home_btn(self):
        print("home button clicked")

    def topbar(self):
        topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        topFrame.pack(fill=tk.X)

        label = tk.Label(topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)

        top_underline = tk.Canvas(topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        top_underline.create_line(4, 2, 218, 2, width=2, fill='white')
        top_underline.pack(fill=tk.X)

        username = tk.Label(topFrame, text=" Admin: Alex Rogers ", fg='white', bg='#1A1A1A', font=('Arial', 14))
        username.pack(side=tk.RIGHT, anchor='e')
        username.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        user_id = tk.Label(topFrame, text="ID: 193812", fg='white', bg='#1A1A1A', font=('Arial', 14))
        user_id.pack(side=tk.RIGHT, anchor='e')
        user_id.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

    def Sidebar(self):
        Sidebar = tk.Frame(self, height=478, bg='#474747')
        Sidebar.pack(fill=tk.Y, side=tk.LEFT)

        side_label = tk.Label(Sidebar,text="Admin Features",fg='white', bg='#474747', anchor='w', font=('Arial', 18),width=13)
        side_label.pack(padx=45,pady=15)


        staff_edit = tk.Button(Sidebar, text='Staff Edit', command=self.staff_edit, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        staff_edit.pack(pady=30)

        menu_edit = tk.Button(Sidebar, text='Menu Edit', command=self.menu_edit, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        menu_edit.pack(pady=30)

        home_btn = tk.Button(Sidebar, text='Home', command=self.home_btn, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        home_btn.pack(pady=30)


    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#1A1A1A')
        bottom_label.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()