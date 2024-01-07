'''
Author Will Griffin
Date: 12/12/2023
Version: 1.0

Author: Shahbaz Bokhari
Date: 28/12/2023
Version: 1.1
'''

import tkinter as tk
from tkinter import ttk, Toplevel, messagebox, Frame
import random

class InventoryModifyView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='#1A58B5')
        self.style = ttk.Style()
        self.topBar()
        self.inventoryTree()
        self.inv_table_space()
        
    def topBar(self):
        self.topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#2976E9')
        self.topFrame.pack(fill=tk.X)

        # The Label 'Horizon Restaurant'
        label = tk.Label(self.topFrame, text="Horizon Restaurant", fg='white', bg='#2976E9', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)

        # Underlines the Label 
        canvas = tk.Canvas(self.topFrame, height=2, bg='#2976E9', highlightthickness=0)
        canvas.create_line(4, 2, 218, 2, width=2, fill='white')
        canvas.pack(fill=tk.X)

        # Username
        self.username = tk.Label(self.topFrame, text=" User: Gordon ", fg='white', bg='#2976E9', font=('Arial', 14))
        self.username.pack(side=tk.RIGHT, anchor='e')
        self.username.place(relx=1.0, rely=0.5, anchor='e', x=-350, y=4)

        # User ID
        self.user_id = tk.Label(self.topFrame, text="ID: 193812", fg='white', bg='#2976E9', font=('Arial', 14))
        self.user_id.pack(side=tk.RIGHT, anchor='e')
        self.user_id.place(relx=1.0, rely=0.5, anchor='e', x=-260, y=4)

        # Refresh Button
        self.refresh_button = tk.Button(self.topFrame, text='Refresh', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.refresh_button.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        # Home Button
        self.home_button = tk.Button(self.topFrame, text='Home', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.home_button.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)
        
        # mainFrame = tk.Frame(self, bg='#1A58B5')
        # mainFrame.pack(fill=tk.BOTH, expand=True)
        
    def inventoryTree(self):
        self.main_frame = tk.Frame(self, bg='#1A58B5')
        self.main_frame.pack()
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=10)

        self.inventory_frame = tk.Frame(self.main_frame, borderwidth=25, bg='#1A58B5', height=120, width=480)
        self.inventory_frame.grid(column=1, row=1, sticky='we')
        self.inventory_frame.rowconfigure(1, weight=1)
        self.inventory_frame.columnconfigure((0,1), weight=5)
        self.inventory_frame.columnconfigure(2, weight=1)

        self.add_inventory_item_btn = tk.Button(self.inventory_frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.add_inventory_item_btn.grid(row=1, column=0, sticky='we', padx=2)

        self.remove_inventory_item_btn = tk.Button(self.inventory_frame, text='Delete', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.remove_inventory_item_btn.grid(row=1, column=1, sticky='we', padx=2)

        self.update_item_option_list()
    
    def update_item_option_list(self, new_list=[], item_filter_selected=None):
        self.item_type_option_list = new_list
        self.selected_option = tk.StringVar(self.inventory_frame)
        if len(self.item_type_option_list) > 0:
            # self.selected_option.set(self.item_type_option_list[0])  # Set default value
            # self.option_menu = tk.OptionMenu(self.inventory_frame, self.selected_option, *self.item_type_option_list)
            # self.option_menu.configure(bg='#1A58B5',fg='white')
            # self.option_menu.grid(row=1, column=2, sticky='nswe', padx=2)
            self.style.configure(
                "TCombobox",
                foreground='white',
                arrowcolor='black',
                font=('Helvetica', 13)
            )

            self.type_filter_combobox = ttk.Combobox(self.inventory_frame, values=self.item_type_option_list, textvariable=self.selected_option, state="readonly")
            self.type_filter_combobox.configure(style="TCombobox")
            self.type_filter_combobox.grid(row=1, column=2, sticky='nswe', padx=2)
            # Set the default selection to the first item on initialisation
            if item_filter_selected is None:
                self.type_filter_combobox.current(0)
            # This ensures the filter doesnt reset every time the user add, delete or update an item
            elif item_filter_selected in self.item_type_option_list:
                index = self.item_type_option_list.index(item_filter_selected)
                self.type_filter_combobox.current(index)

    def add_inventory_pop(self):
        self.inventory_window = Toplevel(self)
        self.inventory_window.title("Inventory add")
        self.inventory_window.geometry('250x400')
        self.inventory_window.configure(bg='white')
        self.inventory_window.resizable(False, False)
    
        add_title = tk.Label(self.inventory_window, text='New Inventory', fg='black', bg='white', font=("Arial", 18))
        add_title.pack(pady=10)
    
        add_name = tk.Label(self.inventory_window, text='Item name:', fg='black', bg='white', font=("Arial", 14))
        add_name.pack(pady=10)
    
        self.name_entry_field = tk.Entry(self.inventory_window, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        self.name_entry_field.pack()
    
        add_qty = tk.Label(self.inventory_window, text='Quantity:', fg='black', bg='white', font=("Arial", 14))
        add_qty.pack(pady=10)
    
        self.qty_entry_field = tk.Entry(self.inventory_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        self.qty_entry_field.pack()
    
        add_reorder = tk.Label(self.inventory_window, text='Re-order level:', fg='black', bg='white', font=("Arial", 14))
        add_reorder.pack(pady=10)

        self.reorder_entry_field = tk.Entry(self.inventory_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        self.reorder_entry_field.pack()

        inv_type = tk.Label(self.inventory_window, text='Type:', fg='black', bg='white', font=("Arial", 14))
        inv_type.pack(pady=10)
    
        self.type_entry_field = tk.Entry(self.inventory_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        self.type_entry_field.pack()
        
        self.submit_new_item_btn = tk.Button(self.inventory_window, text='Submit',bg='white',width=5,height=2)
        self.submit_new_item_btn.pack(pady=10)
        
    
    def inv_table_space(self):
        self.inventory_table_frame = tk.Frame(self.main_frame, borderwidth=25, relief=tk.FLAT, bg='#1A58B5', height=300, width=480)
        self.inventory_table_frame.grid(column=1, row=2)

        self.inventory_tree = ttk.Treeview( self.inventory_table_frame,height=15)
        self.inventory_tree['columns'] = ("ID", "Name", "Qty", "re-order","inventory-type")
        column_width = 120

        # Formatting columns
        self.inventory_tree.column("#0", width=0, minwidth=0)
        self.inventory_tree.column("ID", anchor='center', width=90, minwidth=90)
        self.inventory_tree.column("Name", anchor='w', width=column_width, minwidth=column_width)
        self.inventory_tree.column("Qty",  anchor='w', width=35, minwidth=35)
        self.inventory_tree.column("re-order", anchor='center', width=column_width, minwidth=column_width)
        self.inventory_tree.column("inventory-type", anchor='w', width=column_width, minwidth=column_width)

        # Formatting Headers 
        self.inventory_tree.heading("ID", text="Item ID",anchor='w')
        self.inventory_tree.heading("Name", text="Item Name",anchor='center')
        self.inventory_tree.heading("Qty", text="Qty",anchor='center')
        self.inventory_tree.heading("re-order", text="Re-order level",anchor='e')
        self.inventory_tree.heading("inventory-type", text="Inventory type",anchor='e')

        # Add tag configurations for odd and even rows
        self.inventory_tree.tag_configure('oddrow', background='white', foreground='black')
        self.inventory_tree.tag_configure('evenrow', background='lightgray', foreground='black')
            
        self.inventory_tree.grid(pady=10)
        

    def insert_tree_view(self, data):
        # Populate treeview with updated data
        count = 0
        for record in data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'     # Give alternating colours to rows
            
            
            stock = int(record[2])
            reorder_level = int(record[3])
            is_available = bool(record[5])

            # Check if stock is lower than re-order level, so we can give it a custom colour
            if stock <= reorder_level:
                tag = 'lowstock'   # my custom tag for low stock, ITS MINE
            # This tag is for items just added to the menu, by default their stock and reorder level will be 0, so it will be highlighted by green
            if stock == 0 and reorder_level == 0:
                tag = 'justadded'
            # This tag is for items that have been deleted from the menu
            if not(is_available):
                tag = 'notavailable'

            self.inventory_tree.insert(parent='', index='end', iid=count, text="", values=record, tags=(tag,))
            count += 1

        # Setting background colour for MY TAGS
        self.inventory_tree.tag_configure('lowstock', background='#FFAE42', foreground='white') # YELLOW FOR LOW STOCK background='#EB5160', foreground='#d42839'
        self.inventory_tree.tag_configure('justadded', background='#77DD77', foreground='white') # GREEN FOR NEWLY ADDED MENU ITEMS
        self.inventory_tree.tag_configure('notavailable', background='#d42839', foreground='white') # RED FOR ITEMS DELETED FROM MENU
    
    
    def clear_tree_view(self):
        # Clear existing rows in the treeview
        for row in self.inventory_tree.get_children():
            self.inventory_tree.delete(row)

    def editWindowPopup(self, row_id, column_id):
        self.edit_window = Toplevel(self)
        self.edit_window.title("Edit Cell Value")
        self.edit_window.geometry("300x100")

        # Calculate column index
        self.column_index = int(column_id.replace('#', '')) - 1
        current_value = self.inventory_tree.item(row_id, 'values')[self.column_index]

        self.new_value_entry = tk.Entry(self.edit_window)
        self.new_value_entry.pack(pady=10)
        self.new_value_entry.insert(0, current_value)
        
        self.save_changes_button = tk.Button(self.edit_window, text="Save")
        #, command=lambda: self.saveNewValue(tree, row_id, column_index, newValueUI.get(), editWindow)
        self.save_changes_button.pack()
    
    # def update_new_value(self, row_id, column_id, new_value):
    #     column_index = int((column_id).replace('#', '')) - 1
    #     currentValues = list(self.inventory_tree.item(int(row_id), 'values'))
    #     currentValues[int(column_index)] = new_value
    #     self.inventory_tree.item(int(row_id), values=currentValues)
    #     self.edit_window.destroy()