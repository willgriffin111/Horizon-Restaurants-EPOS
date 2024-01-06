'''
Author Jevhan Seechurn,
Date: 13/12/2023 3am lmao
Version: 1.0

Author Shahbaz Bokhari,
Date: 05/01/2024
Version: 1.1
'''

import tkinter as tk
from tkinter import ttk, Toplevel, Label, Frame

''' TEMPORARY BUTTON IS ON LINE 152'''

class MenuEdit(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='white')
        self.style = ttk.Style()
        self.topbar()
        self.bottombar()
        #self.Sidebar()
        self.menu_button_frame()
        self.menu_table_space()

    # button functions 
    def home_btn(self):
        print("home button clicked")



 # Universal Verification window -----------------------------------------------------------------------------------------------------------------------------------|

    def verify_window(self):
        self.verification_window = Toplevel(self)
        self.verification_window.title("Verify page")
        self.verification_window.geometry('300x200')
        self.verification_window.configure(bg='white')
        self.verification_window.resizable(False, False)

        Verify_lable = tk.Label(self.verification_window,text="Are you sure?",font=("Arial", 18),bg='white',fg='black')
        Verify_lable.pack(pady=20)

        verify_frame_button = tk.Frame(self.verification_window, bg='white')
        verify_frame_button.pack(pady=0)

        proceed_btn = tk.Button(verify_frame_button, width=4, height=3, text='Proceed', borderwidth=0)
        proceed_btn.pack(pady=30,side=tk.LEFT,padx=20)

        Cancel_btn = tk.Button(verify_frame_button, width=4, height=3, text='Cancel', borderwidth=0)
        Cancel_btn.pack(pady=30,side=tk.LEFT,padx=20)

# Top bar ---------------------------------------------------------------------------------------------------------------------------------------------------------|

    def topbar(self):
        topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        topFrame.pack(fill=tk.X)

        label = tk.Label(topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)

        top_underline = tk.Canvas(topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        top_underline.create_line(4, 2, 218, 2, width=2, fill='white')
        top_underline.pack(fill=tk.X)

        self.username = tk.Label(topFrame, text=" User: Alex Rogers ", fg='white', bg='#1A1A1A', font=('Arial', 14))
        self.username.pack(side=tk.RIGHT, anchor='e')
        self.username.place(relx=1.0, rely=0.5, anchor='e', x=-350, y=4)

        self.user_id = tk.Label(topFrame, text="ID: 193812", fg='white', bg='#1A1A1A', font=('Arial', 14))
        self.user_id.pack(side=tk.RIGHT, anchor='e')
        self.user_id.place(relx=1.0, rely=0.5, anchor='e', x=-260, y=4)

        self.home_btn = tk.Button(topFrame, text='Home', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=10)
        self.home_btn.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

        self.refresh_btn = tk.Button(topFrame, text='Refresh', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10,  border=None,width=10)
        self.refresh_btn.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)
  

    def Sidebar(self):
        Sidebar = tk.Frame(self, height=478, bg='#474747')
        Sidebar.pack(fill=tk.Y, side=tk.LEFT)

        side_label = tk.Label(Sidebar,text="Kitchen Features",fg='white', bg='#474747', anchor='w', font=('Arial', 18),width=13)
        side_label.pack(padx=45,pady=15)

        

 # menu button functions ----------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def menu_button_frame(self):
        self.menu_fuction_buttons_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=120,width=480)
        self.menu_fuction_buttons_frame.pack()

        frame_label = tk.Label(self.menu_fuction_buttons_frame, text='Menu Mangament', fg='black', bg='white', font=("Arial", 18))
        frame_label.pack(pady=15)

        self.add_menu_item_btn = tk.Button(self.menu_fuction_buttons_frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.add_menu_item_btn.pack(side=tk.LEFT,padx=6)

        self.edit_menu_item_btn = tk.Button(self.menu_fuction_buttons_frame, text='Edit', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.edit_menu_item_btn.pack(side=tk.LEFT,padx=6)

        self.remove_menu_item_btn = tk.Button(self.menu_fuction_buttons_frame, text='Delete', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.remove_menu_item_btn.pack(side=tk.LEFT,padx=6)


        self.style.configure(
                "TCombobox",
                foreground='black',
                arrowcolor='black',
                font=('Helvetica', 13)
            )
        self.category_filter_combobox = ttk.Combobox(self.menu_fuction_buttons_frame, state='readonly')
        self.category_filter_combobox.configure(style="TCombobox")
        self.category_filter_combobox.pack()

        self.update_category_option_list()


    def update_category_option_list(self, new_list=[], category_filter_selected=None):
        self.category_option_list = new_list
        self.selected_category_option = tk.StringVar(self.menu_fuction_buttons_frame)
        if len(self.category_option_list) > 0:
            self.category_filter_combobox['values'] = self.category_option_list
            self.category_filter_combobox['textvariable'] = self.selected_category_option
            # Set the default selection to the first item on initialisation
            if category_filter_selected is None:
                self.category_filter_combobox.current(0)
            # This ensures the filter doesnt reset every time the user add, delete or update an item
            elif category_filter_selected in self.category_option_list:
                index = self.category_option_list.index(category_filter_selected)
                self.category_filter_combobox.current(index)

# Add menu item window ------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def add_menu_item_popup(self):
        self.add_menu_item_window = Toplevel(self)
        self.add_menu_item_window.title("Add Menu Page")
        self.add_menu_item_window.geometry('350x450')
        self.add_menu_item_window.configure(bg='white')
        self.add_menu_item_window.resizable(False, False)

        # Left side of the pop up window for adding menu item

        left_frame = tk.Frame(self.add_menu_item_window, bg='white')
        left_frame.pack(fill=tk.BOTH, expand=True)

        left_frame_label = tk.Label(left_frame, text='New Menu item', fg='black', bg='white', font=("Arial", 18))
        left_frame_label.pack(pady=15)

        add_menu_name = tk.Label(left_frame, text='Name:', fg='black', bg='white', font=("Arial", 16))
        add_menu_name.pack(pady=10)
    
        self.add_menu_item_name_entry = tk.Entry(left_frame, width=20, fg='black', bg='white', highlightbackground="black", highlightcolor="blue", highlightthickness=2, font=("Arial", 16))
        self.add_menu_item_name_entry.pack()

        add_menu_category = tk.Label(left_frame, text='Category:', fg='black', bg='white', font=("Arial", 16))
        add_menu_category.pack(pady=10)        

        self.add_menu_item_category_entry = tk.Entry(left_frame, width=20, fg='black', bg='white', highlightbackground="black", highlightcolor="blue", highlightthickness=2, font=("Arial", 16))
        self.add_menu_item_category_entry.pack()

        add_menu_cost = tk.Label(left_frame, text='Price:', fg='black', bg='white', font=("Arial", 16))
        add_menu_cost.pack(pady=10)
    
        self.add_menu_item_price_entry = tk.Entry(left_frame, width=20, fg='black', bg='white', highlightbackground="black", highlightcolor="blue", highlightthickness=2, font=("Arial", 16))
        self.add_menu_item_price_entry.pack()

        add_menu_item_desc = tk.Label(left_frame, text='Description:', fg='black', bg='white', font=("Arial", 16))
        add_menu_item_desc.pack(pady=10)

        self.add_menu_item_desc_entry = tk.Entry(left_frame, width=20, fg='black', bg='white', highlightbackground="black", highlightcolor="blue", highlightthickness=2, font=("Arial", 10))
        self.add_menu_item_desc_entry.pack(fill=tk.BOTH)

        button_frame = tk.Frame(left_frame,bg='white')
        button_frame.pack(pady=10, fill=tk.BOTH)

        self.submit_new_item_btn = tk.Button(button_frame, text='Submit', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None)
        self.submit_new_item_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,  padx=2)

# Edit_menu table pop ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def edit_menu_popup(self, menu_data):
        print(menu_data)
        self.menu_edit_window = Toplevel(self)
        self.menu_edit_window.title("Edit Menu Page")
        self.menu_edit_window.geometry('650x560')
        self.menu_edit_window.configure(bg='white')
        self.menu_edit_window.resizable(False, False)

        self.menu_edit_window.columnconfigure((0), weight=1)
        self.menu_edit_window.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        add_title = tk.Label(self.menu_edit_window, text='Menu Edit ', fg='black', bg='white', font=("Arial", 18))
        add_title.grid(row=0)

        mid_frame = tk.Frame(self.menu_edit_window, borderwidth=25, relief=tk.FLAT, bg='white')
        mid_frame.grid(row=1)

        inventory_tree = ttk.Treeview(mid_frame,height=1)
        inventory_tree['columns'] = ("ID", "Name", "category", "cost", "description")
        column_width = 110

        # Formatting columns
        inventory_tree.column("#0", width=0, minwidth=0)
        inventory_tree.column("ID", anchor='center', width=90, minwidth=90)
        inventory_tree.column("Name", anchor='center', width=column_width, minwidth=column_width)
        inventory_tree.column("category",  anchor='center', width=column_width, minwidth=column_width)
        inventory_tree.column("cost", anchor='center', width=column_width, minwidth=column_width)
        inventory_tree.column("description", anchor='center', width=column_width, minwidth=column_width)

        # Formatting Headers 
        inventory_tree.heading("ID", text="Item ID",anchor='w')
        inventory_tree.heading("Name", text="Item",anchor='center')
        inventory_tree.heading("category", text="category",anchor='center')
        inventory_tree.heading("cost", text="Cost",anchor='e')
        inventory_tree.heading("description", text='Description', anchor='center')

        # Add tag configurations for odd and even rows
        inventory_tree.tag_configure('oddrow', background='white', foreground='black')
        inventory_tree.tag_configure('evenrow', background='lightgray', foreground='black')


        count = 0
        tag = 'evenrow' if count % 2 == 0 else 'oddrow'
        inventory_tree.insert(parent='', index='end', iid=count, text="", values=menu_data, tags=(tag,))

        inventory_tree.pack(pady=10)

        add_name = tk.Label(self.menu_edit_window, text='Item name:', fg='black', bg='white', font=("Arial", 14))
        add_name.grid(row=2)

        self.update_item_name_entry = tk.Entry(self.menu_edit_window, width=10, fg='black', bg='lightgrey', highlightbackground="black", highlightcolor="blue", highlightthickness=2)
        self.update_item_name_entry.grid(row=3, sticky='we')

        option_menu_lbl = tk.Label(self.menu_edit_window, text='Category:', fg='black', bg='white', font=("Arial", 14))
        option_menu_lbl.grid(row=4)

        self.update_item_category_entry = tk.Entry(self.menu_edit_window, width=10, fg='black', bg='lightgrey', highlightbackground="black", highlightcolor="blue", highlightthickness=2)
        self.update_item_category_entry.grid(row=5, sticky='we')

        cost_qty = tk.Label(self.menu_edit_window, text='Price:', fg='black', bg='white', font=("Arial", 14))
        cost_qty.grid(row=6)

        self.update_item_price_entry = tk.Entry(self.menu_edit_window, width=6, fg='black', bg='lightgrey', highlightbackground="black", highlightcolor="blue", highlightthickness=2)
        self.update_item_price_entry.grid(row=7, sticky='we')

        desc_label = tk.Label(self.menu_edit_window, text='Desc:', fg='black', bg='white', font=("Arial", 14))
        desc_label.grid(row=8)

        self.update_item_desc_entry = tk.Entry(self.menu_edit_window, width=6, fg='black', bg='lightgrey', highlightbackground="black", highlightcolor="blue", highlightthickness=2)
        self.update_item_desc_entry.grid(row=9, sticky='we')

        input_frame_button = tk.Frame(self.menu_edit_window, bg='black')
        input_frame_button.grid(row=10, sticky='nswe')
        input_frame_button.columnconfigure(0, weight=1)
        input_frame_button.rowconfigure(0, weight=1)

        self.submit_item_changes_btn = tk.Button(input_frame_button, width=4, height=3, text='Submit', borderwidth=0,command=self.verify_window)
        self.submit_item_changes_btn.grid(sticky='we',row=0, column=0, padx=2)

# Menu tree view table ------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def menu_table_space(self):
        mid_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=300,width=480)
        mid_frame.pack(pady=10,fill=tk.X, expand=True)

        self.menu_tree = ttk.Treeview(mid_frame,height=15, show='headings')
        self.menu_tree['columns'] = ("ID", "Name", "category", "cost", "desc")
        column_width = 100

        # Formatting columns
        self.menu_tree.column("#0", width=0, minwidth=0)
        self.menu_tree.column("ID", anchor='center', width=50, minwidth=50)
        self.menu_tree.column("Name", anchor='w', width=column_width, minwidth=column_width)
        self.menu_tree.column("category",  anchor='w', width=50, minwidth=50)
        self.menu_tree.column("cost", anchor='center', width=50, minwidth=50)
        self.menu_tree.column("desc", anchor='w', width=column_width, minwidth=column_width)

        # Formatting Headers 
        self.menu_tree.heading("ID", text="Item ID",anchor='center')
        self.menu_tree.heading("Name", text="Item",anchor='center')
        self.menu_tree.heading("category", text="Category",anchor='center')
        self.menu_tree.heading("cost", text="Cost",anchor='center')
        self.menu_tree.heading("desc", text='Description', anchor='w')

        # Add tag configurations for odd and even rows
        self.menu_tree.tag_configure('oddrow', background='white', foreground='black')
        self.menu_tree.tag_configure('evenrow', background='lightgray', foreground='black')

        menu_data = [
            [1, 'Pizza', 'Main', '£12.99', 'Click to view'],
            [2, 'Burger', 'Main', '£8.99', 'Click to view'],
            [3, 'Pasta', 'Main', '£10.49', 'Click to view'],
            [4, 'Salad', 'Starter', '£6.99', 'Click to view'],
            [5, 'Soup', 'Starter', '£5.49', 'Click to view'],
            [6, 'Steak', 'Main', '£18.99', 'Click to view'],
            [7, 'Fish & Chips', 'Main', '£11.99', 'Click to view'],
            [8, 'Ice Cream', 'Dessert', '£4.99', 'Click to view'],
            [9, 'Cake', 'Dessert', '£7.99', 'Click to view'],
            [10, 'Coffee', 'Beverage', '£2.49', 'Click to view'],
            [11, 'Sushi', 'Main', '£15.99', 'Click to view'],
            [12, 'Tacos', 'Main', '£9.49', 'Click to view'],
            [13, 'Nachos', 'Starter', '£7.99', 'Click to view'],
            [14, 'Fried Chicken', 'Main', '£13.49', 'Click to view'],
            [15, 'Ramen', 'Main', '£11.99', 'Click to view'],
            [16, 'Mousse', 'Dessert', '£6.49', 'Click to view'],
            [17, 'Smoothie', 'Beverage', '£4.49', 'Click to view'],
            [18, 'Margarita', 'Beverage', '£7.99', 'Click to view'],
            [19, 'Curry', 'Main', '£12.49', 'Click to view'],
            [20, 'Wings', 'Starter', '£8.99', 'Click to view']
            ]

        self.menu_tree.pack(pady=10,fill=tk.X, expand=True)
    
    def insert_tree_view(self, data):
        # Populate treeview with updated data
        count = 0
        for record in data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'     # Give alternating colours to rows
            self.menu_tree.insert(parent='', index='end', iid=count, text="", values=record, tags=(tag,))
            count += 1

    def clear_tree_view(self):
        # Clear existing rows in the treeview
        for row in self.menu_tree.get_children():
            self.menu_tree.delete(row)

# bottom bar -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#1A1A1A')
        bottom_label.pack()