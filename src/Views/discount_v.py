"""
Author: Shahbaz Bokhari
File name: discount_v.py
Date: 07/01/2023
"""
from datetime import datetime

import tkinter as tk
from tkinter import ttk, Entry, Label, Toplevel
from tkcalendar import DateEntry

class DiscountView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.style = ttk.Style()

        self.rowconfigure((0,1), weight=1)
        self.columnconfigure(0, weight=1)

        self.top_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#2976E9')
        self.top_frame.grid(row=0, column=0, sticky='nsew')
        self.top_frame.columnconfigure((0,1,2,3,4), weight=1)
        self.top_frame.rowconfigure((0,1,3,4), weight=1)

        Label(self.top_frame, text="Name", fg='white', bg='#2976E9', font=('Arial', 14)).grid(row=0, column=0)
        self.discount_name_entry_field = Entry(self.top_frame, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        self.discount_name_entry_field.grid(pady=10, row=1, column=0)

        Label(self.top_frame, text="Value: (%)", fg='white', bg='#2976E9', font=('Arial', 14)).grid(row=0, column=1)
        self.discount_value_entry_field = Entry(self.top_frame, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        self.discount_value_entry_field.grid(pady=10, row=1, column=1)

        # Using DateEntry for selecting the start date
        Label(self.top_frame, text="Start Date: ", fg='white', bg='#2976E9', font=('Arial', 14)).grid(row=0, column=2)
        self.start_date_entry = DateEntry(self.top_frame, width=14, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy-mm-dd")
        self.start_date_entry.grid(pady=10, row=1, column=2)

        # Using DateEntry for selecting the end date
        Label(self.top_frame, text="End Date", fg='white', bg='#2976E9', font=('Arial', 14)).grid(row=0, column=3)
        self.end_date_entry = DateEntry(self.top_frame, width=14, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy-mm-dd")
        self.end_date_entry.grid(pady=10, row=1, column=3)

        self.refresh_button = tk.Button(self.top_frame, text='Refresh', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.refresh_button.grid(pady=10, row=2, column=0)

        self.home_button = tk.Button(self.top_frame, text='Home', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.home_button.grid(pady=10, row=2, column=2)

        self.add_discount_button = tk.Button(self.top_frame, text='Add', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.add_discount_button.grid(pady=10, row=2, column=3)

        self.remove_discount_button = tk.Button(self.top_frame, text='Remove', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        self.remove_discount_button.grid(pady=10, row=2, column=4)

        self.username = tk.Label(self.top_frame, text=" User: Gordon ", fg='white', bg='#2976E9', font=('Arial', 14))
        self.username.grid(pady=10, row=3, column=3)

        self.user_id = tk.Label(self.top_frame, text="ID: 193812", fg='white', bg='#2976E9', font=('Arial', 14))
        self.user_id.grid(pady=10, row=3, column=4)

        self.discount_tree_view()

    def discount_tree_view(self):
        self.discount_table_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A58B5', height=300, width=480)
        self.discount_table_frame.grid(row=1, column=0, sticky='nsew')
        self.discount_table_frame.columnconfigure(0, weight=1)

        self.discount_tree = ttk.Treeview(self.discount_table_frame,height=15)
        self.discount_tree['columns'] = ("ID", "name", "start", "end","value")
        column_width = 120

        # Formatting columns
        self.discount_tree.column("#0", width=0, minwidth=0)
        self.discount_tree.column("ID", anchor='center', width=90, minwidth=90)
        self.discount_tree.column("name", anchor='w', width=column_width, minwidth=column_width)
        self.discount_tree.column("start",  anchor='w', width=35, minwidth=35)
        self.discount_tree.column("end", anchor='center', width=column_width, minwidth=column_width)
        self.discount_tree.column("value", anchor='w', width=column_width, minwidth=column_width)

        # Formatting Headers 
        self.discount_tree.heading("ID", text="Discount ID",anchor='center')
        self.discount_tree.heading("name", text="Discount Name",anchor='center')
        self.discount_tree.heading("start", text="Start Date",anchor='center')
        self.discount_tree.heading("end", text="End Date",anchor='center')
        self.discount_tree.heading("value", text="Value (%)",anchor='center')

        # Add tag configurations for odd and even rows
        self.discount_tree.tag_configure('oddrow', background='white', foreground='black')
        self.discount_tree.tag_configure('evenrow', background='lightgray', foreground='black')
            
        self.discount_tree.grid(pady=10, sticky='nsew', column=0)

    def clear_tree_view(self):
        # Clear existing rows in the treeview
        for row in self.discount_tree.get_children():
            self.discount_tree.delete(row)
    

    def insert_tree_view(self, data):
        # Populate treeview with updated data
        count = 0
        for record in data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'  # Give alternating colors to rows

            self.discount_tree.insert(parent='', index='end', iid=count, text="", values=record, tags=(tag,))
            count += 1


    def edit_window_popup(self, row_id, column_id):
        self.edit_window = Toplevel(self)
        self.edit_window.title("Edit Cell Value")
        self.edit_window.geometry("300x100")

        # Calculate column index
        self.column_index = int(column_id.replace('#', '')) - 1
        current_value = self.discount_tree.item(row_id, 'values')[self.column_index]

        self.new_value_entry = tk.Entry(self.edit_window)
        self.new_value_entry.pack(pady=10)
        self.new_value_entry.insert(0, current_value)
        
        self.save_changes_button = tk.Button(self.edit_window, text="Save")
        self.save_changes_button.pack()
    
    def date_edit_window_popup(self, row_id, column_id):
        self.edit_window = Toplevel(self)
        self.edit_window.title("Edit Cell Value")
        self.edit_window.geometry("300x100")

        # Calculate column index
        self.column_index = int(column_id.replace('#', '')) - 1
        current_value = self.discount_tree.item(row_id, 'values')[self.column_index]

        self.new_value_entry = DateEntry(self.edit_window, date_pattern="yyyy-mm-dd")
        self.new_value_entry.pack(pady=10)
        
        self.save_changes_button = tk.Button(self.edit_window, text="Save")
        self.save_changes_button.pack()

        

