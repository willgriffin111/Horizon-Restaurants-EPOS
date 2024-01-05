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
        self.topbar()
        self.bottombar()
        self.Sidebar()
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

        username = tk.Label(topFrame, text=" User: Alex Rogers ", fg='white', bg='#1A1A1A', font=('Arial', 14))
        username.pack(side=tk.RIGHT, anchor='e')
        username.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        user_id = tk.Label(topFrame, text="ID: 193812", fg='white', bg='#1A1A1A', font=('Arial', 14))
        user_id.pack(side=tk.RIGHT, anchor='e')
        user_id.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

    def Sidebar(self):
        Sidebar = tk.Frame(self, height=478, bg='#474747')
        Sidebar.pack(fill=tk.Y, side=tk.LEFT)

        side_label = tk.Label(Sidebar,text="Kitchen Features",fg='white', bg='#474747', anchor='w', font=('Arial', 18),width=13)
        side_label.pack(padx=45,pady=15)

        self.home_btn = tk.Button(Sidebar, text='Home', command=self.home_btn, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.home_btn.pack(pady=30)

 # menu button functions ----------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def menu_button_frame(self):
        button_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=120,width=480)
        button_frame.pack()

        frame_label = tk.Label(button_frame, text='Menu Mangament', fg='black', bg='white', font=("Arial", 18))
        frame_label.pack(pady=15)

        add_menu = tk.Button(button_frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5,command=self.add_menu_item)
        add_menu.pack(side=tk.LEFT,padx=6)

        edit_menu = tk.Button(button_frame, text='Edit', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5,command=self.edit_menu_pop)
        edit_menu.pack(side=tk.LEFT,padx=6)

        remove_menu = tk.Button(button_frame, text='Delete', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5,command=self.verify_window)
        remove_menu.pack(side=tk.LEFT,padx=6)

        options = ['All', 'Starter','Main','Dessert','Beverage']
        selected_option = tk.StringVar(button_frame)
        selected_option.set(options[0])  # Set default value

        option_menu = tk.OptionMenu(button_frame, selected_option, *options)
        option_menu.configure(bg='white',fg='black',width=10)
        option_menu.pack(anchor='s')


# Add menu item window ------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def add_menu_item(self):
        self.staff_window = Toplevel(self)
        self.staff_window.title("Add Menu Page")
        self.staff_window.geometry('650x380')
        self.staff_window.configure(bg='white')
        self.staff_window.resizable(False, False)

        # Left side of the pop up window for adding menu item

        left_frame = tk.Frame(self.staff_window, bg='white')
        left_frame.pack(fill=tk.Y, side=tk.LEFT)

        left_frame_label = tk.Label(left_frame, text='New Menu item', fg='black', bg='white', font=("Arial", 18))
        left_frame_label.pack(pady=15,padx=97)

        add_menu_name = tk.Label(left_frame, text='Name:', fg='black', bg='white', font=("Arial", 16))
        add_menu_name.pack(pady=10)
    
        menu_name_box = tk.Entry(left_frame, width=20, fg='black', bg='white', borderwidth=0, border=None, font=("Arial", 16))
        menu_name_box.pack()

        add_menu_category = tk.Label(left_frame, text='Category:', fg='black', bg='white', font=("Arial", 16))
        add_menu_category.pack(pady=10)        

        option_menu_category = ['Starter','Main','Dessert','Beverage']
        selected_option = tk.StringVar(left_frame)
        selected_option.set(option_menu_category[0])  # Set default value

        option_menu_category = tk.OptionMenu(left_frame, selected_option, *option_menu_category)
        option_menu_category.configure(bg='white',fg='black',width=16,font=("Arial", 16),borderwidth=3)
        option_menu_category.pack(anchor='s')

        add_menu_cost = tk.Label(left_frame, text='Price:', fg='black', bg='white', font=("Arial", 16))
        add_menu_cost.pack(pady=10)
    
        menu_cost_box = tk.Entry(left_frame, width=20, fg='black', bg='white', borderwidth=0, border=None, font=("Arial", 16))
        menu_cost_box.pack()

        button_frame = tk.Frame(left_frame,bg='white')
        button_frame.pack(pady=10)

        Submit_menu = tk.Button(button_frame, text='Submit', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5,command=self.verify_window)
        Submit_menu.pack(side=tk.LEFT,padx=20,pady=25)

        Cancel_menu = tk.Button(button_frame, text='Cancel', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        Cancel_menu.pack(side=tk.LEFT,padx=20,pady=25)


# Right side of the pop up adding menu item

        right_frame = tk.Frame(self.staff_window, bg='white')
        right_frame.pack(side=tk.RIGHT,fill=tk.Y)

        right_frame_label = tk.Label(right_frame, text='Add Ingredients', fg='black', bg='white', font=("Arial", 18))
        right_frame_label.pack(padx=97,pady=15)

# Lable frame for add ingredients

        ingredients_lbl_frame = tk.Frame(right_frame, bg='white')
        ingredients_lbl_frame.pack()

        ingredients_label = tk.Label(ingredients_lbl_frame, text='Name:', fg='black', bg='white', font=("Arial", 16))
        ingredients_label.pack(side=tk.LEFT,padx=80)

        ingredients_qty = tk.Label(ingredients_lbl_frame, text='Qty:', fg='black', bg='white', font=("Arial", 16),height=2)
        ingredients_qty.pack(side=tk.LEFT,padx=20)

# Entry frame for add ingredients

        ingredients_entry_frame = tk.Frame(right_frame, bg='white')
        ingredients_entry_frame.pack()

        ingredient_list = [
            'Flour', 'Sugar', 'Salt', 'Butter', 'Eggs', 'Milk',
            'Tomatoes', 'Onions', 'Garlic', 'Basil', 'Oregano',
            'Chicken', 'Beef', 'Lettuce', 'Cheese', 'Bread'
        ]

        def update_list(event):
            entered_text = event.widget.get()
            filtered_list = [lang for lang in ingredient_list if lang.lower().startswith(entered_text.lower())]
            event.widget['values'] = filtered_list  


        combo = ttk.Combobox(ingredients_entry_frame, values=ingredient_list,width=16)
        combo.pack(side=tk.LEFT,padx=20)    
        combo.bind("<KeyRelease>", update_list)


        qty_box1 = tk.Entry(ingredients_entry_frame, width=3, fg='black', bg='white', borderwidth=0, border=None, font=("Arial", 16))
        qty_box1.pack(side=tk.LEFT,padx=20)

# Tree view frame for add ingredients

        ingredients_tree_frame = tk.Frame(right_frame, bg='white')
        ingredients_tree_frame.pack()

        add_ingredients_tree = ttk.Treeview(ingredients_tree_frame,height=6)
        add_ingredients_tree['columns'] = ("Name", "qty-needed")
        column_width = 124

        # Formatting columns
        add_ingredients_tree.column("#0", width=0, minwidth=0)
        add_ingredients_tree.column("Name", anchor='center', width=column_width, minwidth=column_width)
        add_ingredients_tree.column("qty-needed",  anchor='center', width=column_width, minwidth=column_width)


        # Formatting Headers 
        add_ingredients_tree.heading("Name", text="Ingredient",anchor='center')
        add_ingredients_tree.heading("qty-needed", text="Qty",anchor='center')


        # Add tag configurations for odd and even rows
        add_ingredients_tree.tag_configure('oddrow', background='white', foreground='black')
        add_ingredients_tree.tag_configure('evenrow', background='lightgray', foreground='black')

        ingredient_add_data = [['Flour', 1],
                               ['Sugar',2],
                               ['Salt',1],
                               ['Tomato',2],
                               ['Sauce',2],
                               ['Honey',4]
                               ]
        
        count = 0
        for record in ingredient_add_data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            add_ingredients_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1]), tags=(tag,))
            count += 1

        add_ingredients_tree.pack(pady=10)

        
        button_frame = tk.Frame(right_frame,bg='white')
        button_frame.pack()

        add_ingredient = tk.Button(button_frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        add_ingredient.pack(side=tk.LEFT,padx=20,pady=20)

        Remove_ingredient = tk.Button(button_frame, text='Remove', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        Remove_ingredient.pack(side=tk.LEFT,padx=20,pady=20)



# Edit_menu table pop ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def edit_menu_pop(self):
        self.menu_edit_window = Toplevel(self)
        self.menu_edit_window.title("Edit Menu Page")
        self.menu_edit_window.geometry('400x360')
        self.menu_edit_window.configure(bg='white')
        self.menu_edit_window.resizable(False, False)

        add_title = tk.Label(self.menu_edit_window, text='Menu Edit ', fg='black', bg='white', font=("Arial", 18))
        add_title.pack(pady=10)

        mid_frame = tk.Frame(self.menu_edit_window, borderwidth=25, relief=tk.FLAT, bg='white')
        mid_frame.pack()

        inventory_tree = ttk.Treeview(mid_frame,height=1)
        inventory_tree['columns'] = ("Name", "category", "cost")
        column_width = 110

        # Formatting columns
        inventory_tree.column("#0", width=0, minwidth=0)
        inventory_tree.column("Name", anchor='center', width=column_width, minwidth=column_width)
        inventory_tree.column("category",  anchor='center', width=column_width, minwidth=column_width)
        inventory_tree.column("cost", anchor='center', width=column_width, minwidth=column_width)

        # Formatting Headers 
        inventory_tree.heading("Name", text="Item",anchor='center')
        inventory_tree.heading("category", text="category",anchor='center')
        inventory_tree.heading("cost", text="Cost",anchor='e')

        # Add tag configurations for odd and even rows
        inventory_tree.tag_configure('oddrow', background='white', foreground='black')
        inventory_tree.tag_configure('evenrow', background='lightgray', foreground='black')

        menu_data = [['Pizza', 'Main', '£12.99']]

        count = 0
        for record in menu_data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            inventory_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=(tag,))
            count += 1

        inventory_tree.pack(pady=10)

        input_frame_lbl = tk.Frame(self.menu_edit_window, bg='white',height=120,width=480)
        input_frame_lbl.pack(pady=10)

        add_name = tk.Label(input_frame_lbl, text='Item name:', fg='black', bg='white', font=("Arial", 14))
        add_name.pack(pady=2,side=tk.LEFT,padx=24)

        option_menu_lbl = tk.Label(input_frame_lbl, text='Category:', fg='black', bg='white', font=("Arial", 14))
        option_menu_lbl.pack(pady=2,side=tk.LEFT,padx=24)

        cost_qty = tk.Label(input_frame_lbl, text='Price:', fg='black', bg='white', font=("Arial", 14))
        cost_qty.pack(pady=2,side=tk.LEFT,padx=24)


        input_frame_box = tk.Frame(self.menu_edit_window, bg='white')
        input_frame_box.pack(pady=0)

        name_box = tk.Entry(input_frame_box, width=10, fg='black', bg='lightgrey', borderwidth=0, border=None)
        name_box.pack(side=tk.LEFT,padx=5)

        option_menu = ['Starter','Main','Dessert','Beverage']
        selected_option = tk.StringVar(self.menu_edit_window)
        selected_option.set(option_menu[0])  # Set default value

        option_menu = tk.OptionMenu(input_frame_box, selected_option, *option_menu)
        option_menu.configure(bg='white',fg='black',width=9,font=("Arial", 16),borderwidth=3)
        option_menu.pack(side=tk.LEFT,padx=5)
   
        cost_box = tk.Entry(input_frame_box, width=6, fg='black', bg='lightgrey', borderwidth=0)
        cost_box.pack(side=tk.LEFT,padx=10)

        input_frame_button = tk.Frame(self.menu_edit_window, bg='white')
        input_frame_button.pack(pady=0)

        submit = tk.Button(input_frame_button, width=4, height=3, text='Submit', borderwidth=0,command=self.verify_window)
        submit.pack(pady=30,side=tk.LEFT,padx=20)

        cancel = tk.Button(input_frame_button, width=4, height=3, text='Cancel', borderwidth=0)
        cancel.pack(pady=30,side=tk.LEFT,padx=20)

# Menu tree view table ------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def menu_table_space(self):
        mid_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=300,width=480)
        mid_frame.pack(pady=10,)

        menu_tree = ttk.Treeview(mid_frame,height=15)
        menu_tree['columns'] = ("ID", "Name", "category", "cost", "click-here")
        column_width = 100

        # Formatting columns
        menu_tree.column("#0", width=0, minwidth=0)
        menu_tree.column("ID", anchor='center', width=90, minwidth=90)
        menu_tree.column("Name", anchor='w', width=column_width, minwidth=column_width)
        menu_tree.column("category",  anchor='w', width=column_width, minwidth=column_width)
        menu_tree.column("cost", anchor='w', width=70, minwidth=70)
        menu_tree.column("click-here", anchor='w', width=column_width, minwidth=column_width)

        # Formatting Headers 
        menu_tree.heading("ID", text="Item ID",anchor='w')
        menu_tree.heading("Name", text="Item",anchor='center')
        menu_tree.heading("category", text="category",anchor='center')
        menu_tree.heading("cost", text="Cost",anchor='e')
        menu_tree.heading("click-here", text="Ingredients",anchor='e')

        # Add tag configurations for odd and even rows
        menu_tree.tag_configure('oddrow', background='white', foreground='black')
        menu_tree.tag_configure('evenrow', background='lightgray', foreground='black')

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


 # For loop to generate the values in the database 
        count = 0
        for record in menu_data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            menu_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4]), tags=(tag,))
            count += 1

        menu_tree.pack(pady=10)

# bottom bar -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#1A1A1A')
        bottom_label.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()