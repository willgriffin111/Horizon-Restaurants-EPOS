import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel

'''
Author Jevhan Seechurn, Alex Rogers
Date: 18/12/2023
Version: 1.1
'''

class AdminView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='white')
        self.topbar()
        self.bottombar()
        self.Sidebar()
        self.staff_button_frame()
        self.staff_table_space()
        
    # button functions


    def staff_edit(self):
        print("Staff Edit button clicked")
        self.staff_frame.pack()
        self.staff_table_frame.pack()


    # Add Staff Window ------------------------------------------------------------------------------------------------------------------------------------------------|

    def add_staff_pop(self,restaurantNames):
        def destroy_window():
            self.staff_window.destroy()
    
        self.staff_window = Toplevel(self)
        self.staff_window.title("Staff add")
        self.staff_window.geometry('250x400')
        self.staff_window.configure(bg='white')
        self.staff_window.resizable(False, False)
    
        self.add_title = tk.Label(self.staff_window, text='Add Staff', fg='black', bg='white', font=("Arial", 18))
        self.add_title.pack(pady=10)

        self.add_resturant_option = tk.Label(self.staff_window, text='Restaurant:', fg='black', bg='white', font=("Arial", 14))
        self.add_resturant_option.pack(pady=10)

        self.option = restaurantNames
        self.chosen_restaurant_option = tk.StringVar(self.staff_window)
        self.chosen_restaurant_option.set(self.option[0])  

        self.restaurant_option = tk.OptionMenu(self.staff_window, self.chosen_restaurant_option, *self.option)
        self.restaurant_option.configure(bg='white',fg='black',width=10)
        self.restaurant_option.pack()
    
        self.add_name = tk.Label(self.staff_window, text='Full name:', fg='black', bg='white', font=("Arial", 14))
        self.add_name.pack(pady=10)
    
        self.name_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        self.name_box.pack()
    
        self.add_role = tk.Label(self.staff_window, text='Role:', fg='black', bg='white', font=("Arial", 14))
        self.add_role.pack(pady=10)
    
        self.role_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        self.role_box.pack()
    
        self.add_password = tk.Label(self.staff_window, text='Password:', fg='black', bg='white', font=("Arial", 14))
        self.add_password.pack(pady=10)
    
        self.password_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        self.password_box.pack()
    
        # Function to close the current window when the 'Add Staff' button is clicked
        self.add_submit = tk.Button(self.staff_window, width=4, height=2, text='Submit', borderwidth=0)
        self.add_submit.pack(pady=20)
        
    
        

    # Top bar ---------------------------------------------------------------------------------------------------------------------------------------------------------|

    def topbar(self):
        self.topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        self.topFrame.pack(fill=tk.X)

        self.label = tk.Label(self.topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        self.label.pack(fill=tk.BOTH, expand=True)

        self.top_underline = tk.Canvas(self.topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        self.top_underline.create_line(4, 2, 218, 2, width=2, fill='white')
        self.top_underline.pack(fill=tk.X)

        self.username = tk.Label(self.topFrame, text=" Admin: Alex Rogers ", fg='white', bg='#1A1A1A', font=('Arial', 14))
        self.username.pack(side=tk.RIGHT, anchor='e')
        self.username.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        self.user_id = tk.Label(self.topFrame, text="ID: 193812", fg='white', bg='#1A1A1A', font=('Arial', 14))
        self.user_id.pack(side=tk.RIGHT, anchor='e')
        self.user_id.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

    def Sidebar(self):
        self.sidebar = tk.Frame(self, height=478, bg='#474747')
        self.sidebar.pack(fill=tk.Y, side=tk.LEFT)

        self.side_label = tk.Label(self.sidebar,text="Admin Features",fg='white', bg='#474747', anchor='w', font=('Arial', 18),width=13)
        self.side_label.pack(padx=10,pady=15)


        self.home_btn = tk.Button(self.sidebar, text='Home', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.home_btn.pack(pady=30)

    # Staff button / Tree view  ----------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def staff_button_frame(self):
        self.staff_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white', height=120, width=480)
        self.staff_frame.pack(pady=10)
        self.staff_frame.lower()

        self.frame_label = tk.Label(self.staff_frame, text='Staff Management', fg='black', bg='white', font=("Arial", 18))
        self.frame_label.pack(pady=10)

        self.add_staff_btn = tk.Button(self.staff_frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.add_staff_btn.pack(side=tk.LEFT,padx=6)

        self.remove_staff_btn = tk.Button(self.staff_frame, text='Delete', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.remove_staff_btn.pack(side=tk.LEFT,padx=6)

        # edit_staff = tk.Button(self.staff_frame, text='Edit', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        # edit_staff.pack(side=tk.LEFT,padx=6)

        
    
    def staff_table_space(self):
        self.staff_table_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white', height=300, width=480)
        self.staff_table_frame.pack(pady=10)
        self.staff_table_frame.lower()

        self.staff_tree = ttk.Treeview(self.staff_table_frame, height=15)
        self.staff_tree['columns'] = ("ID", "Name", "Role", "Password", "Restaurant")
        column_width = 110

        # Formatting columns
        self.staff_tree.column("#0", width=0, minwidth=0)
        self.staff_tree.column("ID", anchor='center', width=90, minwidth=90)
        self.staff_tree.column("Name", anchor='w', width=column_width, minwidth=column_width)
        self.staff_tree.column("Role", anchor='w', width=column_width, minwidth=column_width)
        self.staff_tree.column("Password", anchor='center', width=column_width, minwidth=column_width)
        self.staff_tree.column("Restaurant", anchor='w', width=column_width, minwidth=column_width)

        # Formatting Headers 
        self.staff_tree.heading("ID", text="Staff ID", anchor='w')
        self.staff_tree.heading("Name", text="Staff Name", anchor='center')
        self.staff_tree.heading("Role", text="Role", anchor='center')
        self.staff_tree.heading("Password", text="Password", anchor='e')
        self.staff_tree.heading("Restaurant", text="Restaurant", anchor='e')

        # Add tag configurations for odd and even rows
        self.staff_tree.tag_configure('oddrow', background='white', foreground='black')
        self.staff_tree.tag_configure('evenrow', background='lightgray', foreground='black')

        self.staff_tree.pack(pady=10)
        
    def insert_data_staff(self, data = None):
        # For loop to generate the values in the database 
        if data != None:
            count = 0
            for record in data:
                tag = 'evenrow' if count % 2 == 0 else 'oddrow'
                self.staff_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[2], record[3], record[4], record[1]), tags=(tag,))
                count += 1
                
                
    def clear_staff_table(self):
        for record in self.staff_tree.get_children():
            self.staff_tree.delete(record)

  

    def editWindowPopup(self, tree, row_id, column_id):
        self.editWindow = Toplevel(self)
        self.editWindow.title("Edit Cell Value")
        self.editWindow.geometry("300x100")

        # Calculate column index
        self.column_index = int(column_id.replace('#', '')) - 1
        self.current_value = tree.item(row_id, 'values')[self.column_index]

        self.newValueUI = tk.Entry(self.editWindow)
        self.newValueUI.pack(pady=10)
        self.newValueUI.insert(0, self.current_value)
        
        self.save_btn = tk.Button(self.editWindow, text="Save")
        self.save_btn.pack()



    # bottom bar -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        self.bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        self.bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        self.bottom_label = tk.Label(self.bottomFrame, text="", bg='#1A1A1A')
        self.bottom_label.pack()


