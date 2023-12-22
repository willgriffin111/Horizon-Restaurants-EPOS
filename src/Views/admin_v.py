import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel

'''
Author Jevhan Seechurn, Alex Rogers
Date: 18/12/2023
Version: 1.1
'''
# Dummy values for the database 
data = [
    [987654, "Alice Smith", "Front of house", "54321"],
    [234567, "Bob Johnson", "Manager", "23456"],
    [345678, "Eva Williams", "Chef", "34567"],
    [456789, "David Brown", "Kitchen staff", "45678"],
    [567890, "Sophia Davis", "Front of house", "56789"],
    [678901, "Oliver Wilson", "Chef", "67890"],
    [789012, "Mia Martinez", "Kitchen staff", "78901"],
    [890123, "William Anderson", "Manager", "89012"],
    [901234, "Charlotte Taylor", "Front of house", "90123"],
    [112233, "Amelia Thomas", "Chef", "11223"],
    [334455, "James White", "Front of house", "33445"],
    [556677, "Emily Garcia", "Kitchen staff", "55667"],
    [778899, "Michael Lee", "Manager", "77889"],
    [990011, "Abigail Rodriguez", "Chef", "99001"],
    [224466, "Sophie Harris", "Front of house", "22446"],
    [448822, "Alexander King", "Kitchen staff", "44882"],
    [661144, "Grace Clark", "Manager", "66114"],
    [883322, "Jack Wright", "Chef", "88332"],
    [990044, "Ava Scott", "Front of house", "99004"],
    [557788, "Lucas Green", "Kitchen staff", "55778"],
    [112211, "Liam Turner", "Chef", "11221"],
    [334433, "Olivia Hall", "Front of house", "33443"],
    [556699, "Jessica Adams", "Kitchen staff", "55669"],
    [770011, "Noah Parker", "Manager", "77001"],
    [889922, "Isabella Carter", "Chef", "88992"],
]

class AdminView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='white')
        self.topbar()
        self.bottombar()
        self.Sidebar()
        self.button_frame()
        self.table_space()



    # Add Staff Window ------------------------------------------------------------------------------------------------------------------------------------------------|

    def add_staff_pop(self):
        def destroy_window():
            self.staff_window.destroy()
    
        self.staff_window = Toplevel(self)
        self.staff_window.title("Staff add")
        self.staff_window.geometry('250x340')
        self.staff_window.configure(bg='white')
        self.staff_window.resizable(False, False)
    
        self.add_title = tk.Label(self.staff_window, text='Add Staff', fg='black', bg='white', font=("Arial", 18))
        self.add_title.pack(pady=10)
    
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
        self.submit = tk.Button(self.staff_window, width=4, height=2, text='Submit', borderwidth=0,
                           command=lambda: [self.add_staff_record(self.name_box, self.role_box, self.password_box), destroy_window()])
        self.submit.pack(pady=20)
        

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
        self.side_label.pack(padx=45,pady=15)


        self.staff_edit_btn = tk.Button(self.sidebar, text='Staff', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.staff_edit_btn.pack(pady=30)

        self.menu_edit_btn = tk.Button(self.sidebar, text='Menu', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.menu_edit_btn.pack(pady=30)

        self.home_btn = tk.Button(self.sidebar, text='Home', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.home_btn.pack(pady=30)

    # Staff button functions ----------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def button_frame(self):
        self.button_Frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=120,width=480)
        self.button_Frame.pack(pady=10)

        self.add_staff_btn = tk.Button(self.button_Frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5,command=self.add_staff_pop)
        self.add_staff_btn.pack(side=tk.LEFT,padx=6)

        self.remove_staff_btn = tk.Button(self.button_Frame, text='Delete', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.remove_staff_btn.pack(side=tk.LEFT,padx=6)

        self.edit_staff_btn = tk.Button(self.button_Frame, text='Edit', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        self.edit_staff_btn.pack(side=tk.LEFT,padx=6)

        self.options = ['All', 'Manager', 'Chef', 'Front of house', 'Kitchen staff']
        self.selected_option = tk.StringVar(self.button_Frame)
        self.selected_option.set(self.options[0])  # Set default value

        self.option_menu = tk.OptionMenu(self.button_Frame, self.selected_option, *self.options)
        self.option_menu.configure(bg='white',fg='black',width=10)
        self.option_menu.pack(anchor='s')



    # Tree view table ------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    def table_space(self):
        self.mid_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=300,width=480)
        self.mid_frame.pack(pady=10,)
        self.edit_staff_table()
        
    def edit_staff_table(self, data = None):
        self.staff_tree = ttk.Treeview(self.mid_frame,height=15)
        self.staff_tree['columns'] = ("ID", "Name", "Role", "Password")
        self.column_width = 130

        # Formatting columns
        self.staff_tree.column("#0", width=0, minwidth=0)
        self.staff_tree.column("ID", anchor='center', width=90, minwidth=90)
        self.staff_tree.column("Name", anchor='w', width=self.column_width, minwidth=self.column_width)
        self.staff_tree.column("Role",  anchor='w', width=self.column_width, minwidth=self.column_width)
        self.staff_tree.column("Password", anchor='center', width=self.column_width, minwidth=self.column_width)

        # Formatting Headers 
        self.staff_tree.heading("ID", text="Staff ID",anchor='w')
        self.staff_tree.heading("Name", text="Staff Name",anchor='center')
        self.staff_tree.heading("Role", text="Role",anchor='center')
        self.staff_tree.heading("Password", text="Password",anchor='e')

        # Add tag configurations for odd and even rows
        self.staff_tree.tag_configure('oddrow', background='white', foreground='black')
        self.staff_tree.tag_configure('evenrow', background='lightgray', foreground='black')

        # For loop to generate the values in the database 
        if data != None:
            count = 0
            for record in data:
                tag = 'evenrow' if count % 2 == 0 else 'oddrow'
                self.staff_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]), tags=(tag,))
                count += 1

        self.staff_tree.pack(pady=10)

    # bottom bar -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        self.bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        self.bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        self.bottom_label = tk.Label(self.bottomFrame, text="", bg='#1A1A1A')
        self.bottom_label.pack()



