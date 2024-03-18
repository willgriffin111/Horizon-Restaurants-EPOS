'''
Auther Jevhan Seechurn,
Date: 13/12/2023 3am lmao
Version: 1.0
'''

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title(' Staff Performance Page')
        self.configure(bg='white')
        self.topbar()
        self.bottombar()
        self.Sidebar()
        self.staff_perform_title_space()
        self.staff_perform_table_space()

# Button functions -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def Home_btn(self):
        print("Home button clicked")


    def topbar(self):
        topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        topFrame.pack(fill=tk.X)

        label = tk.Label(topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)

        top_underline = tk.Canvas(topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        top_underline.create_line(4, 2, 218, 2, width=2, fill='white')
        top_underline.pack(fill=tk.X)

        username = tk.Label(topFrame, text=" User: Jordon Brown ", fg='white', bg='#1A1A1A', font=('Arial', 14))
        username.pack(side=tk.RIGHT, anchor='e')
        username.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        user_id = tk.Label(topFrame, text="ID: 193812", fg='white', bg='#1A1A1A', font=('Arial', 14))
        user_id.pack(side=tk.RIGHT, anchor='e')
        user_id.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

# Side bar frame ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


    def Sidebar(self):
        Sidebar = tk.Frame(self, height=478, bg='#474747')
        Sidebar.pack(fill=tk.Y, side=tk.LEFT)

        side_label = tk.Label(Sidebar,text="Staff Performance",fg='white', bg='#474747', anchor='w', font=('Arial', 18),width=13)
        side_label.pack(padx=45,pady=15)

        home_btn = tk.Button(Sidebar, text='Home', command=self.Home_btn, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        home_btn.pack(pady=30)


# Staff performace tree view table ------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def staff_perform_title_space(self):
        top_frame = tk.Frame(self,bg='white')
        top_frame.pack(pady=20)

        frame_label = tk.Label(top_frame, text='Staff Performance Score', fg='black', bg='white', font=("Arial", 18))
        frame_label.pack()


    def staff_perform_table_space(self):
        mid_frame = tk.Frame(self, bg='white')
        mid_frame.pack(side='left',padx=10)

        mid_lbl_frame = tk.Frame(mid_frame, bg='white')
        mid_lbl_frame.pack()

        profit_label = tk.Label(mid_lbl_frame, text='Staff profit record', fg='black', bg='white', font=("Arial", 14))
        profit_label.pack(side='left',padx=70,pady=20)

        profit_label = tk.Label(mid_lbl_frame, text='Staff order record', fg='black', bg='white', font=("Arial", 14))
        profit_label.pack(side='left',padx=70,pady=20)
 
# Staff performance tree view (Profits made ) -------------------------------------------------------------------------------------------------------------------------------------------------------|

        tree_view_frame = tk.Frame(mid_frame, bg='white')
        tree_view_frame.pack(side='left',padx=10)

        staff_profit_tree = ttk.Treeview(tree_view_frame,height=14)
        staff_profit_tree['columns'] = ("ID", "Name", "role", "profit")
        column_width = 65

        # Formatting columns
        staff_profit_tree.column("#0", width=0, minwidth=0)
        staff_profit_tree.column("ID", anchor='center', width=50, minwidth=30)
        staff_profit_tree.column("Name", anchor='w', width=column_width, minwidth=column_width)
        staff_profit_tree.column("role",  anchor='w', width=column_width, minwidth=column_width)
        staff_profit_tree.column("profit", anchor='center', width=50, minwidth=50)


        # Formatting Headers 
        staff_profit_tree.heading("ID", text="Staff ID",anchor='center')
        staff_profit_tree.heading("Name", text="Name",anchor='center')
        staff_profit_tree.heading("role", text="Position",anchor='center')
        staff_profit_tree.heading("profit", text="Profit total",anchor='center')


        # Add tag configurations for odd and even rows
        staff_profit_tree.tag_configure('oddrow', background='white', foreground='black')
        staff_profit_tree.tag_configure('evenrow', background='lightgray', foreground='black')


        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 8)) 
        style.configure("Treeview.Heading", font=('Arial', 8, 'bold'))

        menu_data = [
            [1, 'James Beal', 'Front of house', 5],
            [2, 'Alice Smith', 'Chef', 4],
            [3, 'John Doe', 'Waiter', 3],
            [4, 'Emily Johnson', 'Manager', 5],
            [5, 'Michael Brown', 'Bartender', 4],
            [6, 'Sarah Wilson', 'Front of house', 4],
            [7, 'David Davis', 'Chef', 3],
            [8, 'Olivia Martinez', 'Waiter', 5],
            [9, 'Daniel Miller', 'Manager', 4],
            [10, 'Sophia Garcia', 'Bartender', 3],
            [11, 'Matthew Rodriguez', 'Front of house', 5],
            [12, 'Emma Lopez', 'Chef', 4],
            [13, 'Ethan Lee', 'Waiter', 3],
            [14, 'Ava Harris', 'Manager', 5],
            [15, 'Liam Clark', 'Bartender', 4],
            [16, 'Chloe Young', 'Front of house', 4],
            [17, 'Mason Allen', 'Chef', 3],
            [18, 'Isabella King', 'Waiter', 5],
            [19, 'Jacob Wright', 'Manager', 4],
            [20, 'Amelia Hill', 'Bartender', 3],
            [21, 'Sophie Turner', 'Front of house', 5],
            [22, 'Oliver White', 'Chef', 4],
            [23, 'Grace Brown', 'Waiter', 3],
            [24, 'William Scott', 'Manager', 5],
            [25, 'Natalie Adams', 'Bartender', 4],
            [26, 'Benjamin Carter', 'Front of house', 4],
            [27, 'Zoe Hall', 'Chef', 3],
            [28, 'Henry Reed', 'Waiter', 5],
            [29, 'Victoria Bell', 'Manager', 4],
            [30, 'Jack Wood', 'Bartender', 3]
        ]

        count = 0
        for record in menu_data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            staff_profit_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]), tags=(tag,))
            count += 1

        scrollbar = ttk.Scrollbar(tree_view_frame, orient='vertical', command=staff_profit_tree.yview)
        staff_profit_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        staff_profit_tree.pack(side='left')

        staff_profit_tree.pack(side='left')

# Staff performance tree view (Profits made ) -------------------------------------------------------------------------------------------------------------------------------------------------------|

        tree_view_frame = tk.Frame(mid_frame, bg='white')
        tree_view_frame.pack(side='left',padx=10)

        staff_order_tree = ttk.Treeview(tree_view_frame,height=14)
        staff_order_tree['columns'] = ("ID", "Name", "role", "order")

        # Formatting columns
        staff_order_tree.column("#0", width=0, minwidth=0)
        staff_order_tree.column("ID", anchor='center', width=50, minwidth=50)
        staff_order_tree.column("Name", anchor='w', width=column_width, minwidth=column_width)
        staff_order_tree.column("role",  anchor='w', width=column_width, minwidth=column_width)
        staff_order_tree.column("order", anchor='center', width=50, minwidth=50)


        # Formatting Headers 
        staff_order_tree.heading("ID", text="Staff ID",anchor='center')
        staff_order_tree.heading("Name", text="Name",anchor='center')
        staff_order_tree.heading("role", text="Position",anchor='center')
        staff_order_tree.heading("order", text="Order Total",anchor='center')


        # Add tag configurations for odd and even rows
        staff_order_tree.tag_configure('oddrow', background='white', foreground='black')
        staff_order_tree.tag_configure('evenrow', background='lightgray', foreground='black')


        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 8)) 
        style.configure("Treeview.Heading", font=('Arial', 8, 'bold'))

        menu_data = [
            [1, 'James Beal', 'Front of house', 5],
            [2, 'Alice Smith', 'Chef', 4],
            [3, 'John Doe', 'Waiter', 3],
            [4, 'Emily Johnson', 'Manager', 5],
            [5, 'Michael Brown', 'Bartender', 4],
            [6, 'Sarah Wilson', 'Front of house', 4],
            [7, 'David Davis', 'Chef', 3],
            [8, 'Olivia Martinez', 'Waiter', 5],
            [9, 'Daniel Miller', 'Manager', 4],
            [10, 'Sophia Garcia', 'Bartender', 3],
            [11, 'Matthew Rodriguez', 'Front of house', 5],
            [12, 'Emma Lopez', 'Chef', 4],
            [13, 'Ethan Lee', 'Waiter', 3],
            [14, 'Ava Harris', 'Manager', 5],
            [15, 'Liam Clark', 'Bartender', 4],
            [16, 'Chloe Young', 'Front of house', 4],
            [17, 'Mason Allen', 'Chef', 3],
            [18, 'Isabella King', 'Waiter', 5],
            [19, 'Jacob Wright', 'Manager', 4],
            [20, 'Amelia Hill', 'Bartender', 3],
            [21, 'Sophie Turner', 'Front of house', 5],
            [22, 'Oliver White', 'Chef', 4],
            [23, 'Grace Brown', 'Waiter', 3],
            [24, 'William Scott', 'Manager', 5],
            [25, 'Natalie Adams', 'Bartender', 4],
            [26, 'Benjamin Carter', 'Front of house', 4],
            [27, 'Zoe Hall', 'Chef', 3],
            [28, 'Henry Reed', 'Waiter', 5],
            [29, 'Victoria Bell', 'Manager', 4],
            [30, 'Jack Wood', 'Bartender', 3]
        ]

        count = 0
        for record in menu_data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            staff_order_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]), tags=(tag,))
            count += 1

        scrollbar = ttk.Scrollbar(tree_view_frame, orient='vertical', command=staff_order_tree.yview)
        staff_order_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        staff_order_tree.pack(side='left')

        staff_order_tree.pack(side='left')

# Button frame ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#1A1A1A')
        bottom_label.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()