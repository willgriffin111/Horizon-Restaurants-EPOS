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
        self.title('Order Page')
        self.configure(bg='#1A58B5')
        self.Sidebar()
        self.topbar(userName=userName, userID=userId)
        self.bottombar()

    # button funtion
    def home_action(self):
        print("Option button clicked")

    def Log_out_button(self):
        print("Logged off")

    def table_button(self):
        print("Table button clicked")



    def topbar(self, userName, userID):
        topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#2976E9')
        topFrame.pack(fill=tk.X)

        label = tk.Label(topFrame, text="Horizon Restaurant", fg='white', bg='#2976E9', anchor='w', font=('Arial', 16), underline=True)
        label.pack(fill=tk.BOTH, expand=True)

        top_underline = tk.Canvas(topFrame, height=2, bg='#2976E9', highlightthickness=0)
        top_underline.create_line(4, 2, 143, 2, width=2, fill='white')
        top_underline.pack(fill=tk.X)

        username = tk.Label(topFrame, text=f" User: {userName}", fg='white', bg='#2976E9', font=('Arial', 12))
        username.pack(side=tk.RIGHT, anchor='e')
        username.place(relx=1.0, rely=0.5, anchor='e', x=-170, y=4)

        user_id = tk.Label(topFrame, text=f"ID: {userID}", fg='white', bg='#2976E9', font=('Arial', 12))
        user_id.pack(side=tk.RIGHT, anchor='e')
        user_id.place(relx=1.0, rely=0.5, anchor='e', x=-90, y=4)

        # Home Button
        refresh_button = tk.Button(topFrame, text='Home', command=self.home_action, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        refresh_button.place(relx=1.0, rely=0.5, anchor='e', x=3, y=4)


    def Sidebar(self):
        Sidebar = tk.Frame(self, width=300, height=478, bg='#F0FFFF')
        Sidebar.pack(fill=tk.Y, side=tk.LEFT)

        top_box = tk.Frame(Sidebar, bg='grey')
        top_box.pack(anchor='nw', padx=10, pady=10)

        Log_out_button = tk.Button(top_box, command=self.Log_out_button, text="Log Out", bg='white', padx=10, pady=0, borderwidth=0, highlightthickness=0,height=4,width=10)
        Log_out_button.pack(side=tk.LEFT)  # Aligns the Log Out button to the left

        table_button = tk.Button(top_box, command=self.table_button, text="Table", bg='white', padx=10, pady=0, borderwidth=0, highlightthickness=0,height=4,width=10)
        table_button.pack(side=tk.LEFT)  # Aligns the Table button to the left next to Log Out button

# To do list 

        product_label = tk.Label

        qty_label = tk.Label

        total = tk.Label

        Line_split1 = tk.Canvas

        item = tk.Label

        discount_dp = tk.Label

        Line_split2 = tk.Canvas

        total_dp = tk.Label

        due_dpl = tk.Label

        Line_split3 = tk.Canvas

        reciept_btn = tk.Button

        discount_btn = tk.Button

        delete_btn = tk.Button

        mod_btn = tk.Button

        pay_btn = tk.Button


    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='#2976E9')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#2976E9')
        bottom_label.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
