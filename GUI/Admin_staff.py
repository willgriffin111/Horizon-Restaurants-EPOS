import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel

'''
Author Jevhan Seechurn,
Date: 13/12/2023 3am lmao
Version: 1.0
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

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('Admin Feature')
        self.configure(bg='white')
        self.topbar()
        self.bottombar()
        self.Sidebar()
        self.button_frame()

    # button functions
    def staff_edit(self):
        print("staff edit button clicked")

    def menu_edit(self):
        print("menu edit button clicked")

    def home_btn(self):
        print("home button clicked")

    # Add Staff Window ------------------------------------------------------------------------------------------------------------------------------------------------|

    def add_staff_pop(self):
        def destroy_window():
            self.staff_window.destroy()
    
        self.staff_window = Toplevel(self)
        self.staff_window.title("Staff add")
        self.staff_window.geometry('250x340')
        self.staff_window.configure(bg='white')
        self.staff_window.resizable(False, False)
    
        add_title = tk.Label(self.staff_window, text='Add Staff', fg='black', bg='white', font=("Arial", 18))
        add_title.pack(pady=10)
    
        add_name = tk.Label(self.staff_window, text='Full name:', fg='black', bg='white', font=("Arial", 14))
        add_name.pack(pady=10)
    
        name_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        name_box.pack()
    
        add_role = tk.Label(self.staff_window, text='Role:', fg='black', bg='white', font=("Arial", 14))
        add_role.pack(pady=10)
    
        role_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        role_box.pack()
    
        add_password = tk.Label(self.staff_window, text='Password:', fg='black', bg='white', font=("Arial", 14))
        add_password.pack(pady=10)
    
        password_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        password_box.pack()
    
        # Function to close the current window when the 'Add Staff' button is clicked
        submit = tk.Button(self.staff_window, width=4, height=2, text='Submit', borderwidth=0,
                           command=lambda: [self.add_staff_record(name_box, role_box, password_box), destroy_window()])
        submit.pack(pady=20)
        

    # Top bar ---------------------------------------------------------------------------------------------------------------------------------------------------------|

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


        staff_edit = tk.Button(Sidebar, text='Staff', command=self.staff_edit, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        staff_edit.pack(pady=30)

        menu_edit = tk.Button(Sidebar, text='Menu', command=self.menu_edit, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        menu_edit.pack(pady=30)

        home_btn = tk.Button(Sidebar, text='Home', command=self.home_btn, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        home_btn.pack(pady=30)

    # Staff button functions ----------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def button_frame(self):
        button_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=120,width=480)
        button_frame.pack(pady=10)

        add_staff = tk.Button(button_frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5,command=self.add_staff_pop)
        add_staff.pack(side=tk.LEFT,padx=6)

        remove_staff = tk.Button(button_frame, text='Delete', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        remove_staff.pack(side=tk.LEFT,padx=6)

        edit_staff = tk.Button(button_frame, text='Edit', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        edit_staff.pack(side=tk.LEFT,padx=6)

        options = ['All', 'Manager', 'Chef', 'Front of house', 'Kitchen staff']
        selected_option = tk.StringVar(button_frame)
        selected_option.set(options[0])  # Set default value

        option_menu = tk.OptionMenu(button_frame, selected_option, *options)
        option_menu.configure(bg='white',fg='black',width=10)
        option_menu.pack(anchor='s')



    # Tree view table ------------------------------------------------------------------------------------------------------------------------------------------------------------------|

        staff_tree = ttk.Treeview(self,height=15)
        staff_tree['columns'] = ("ID", "Name", "Role", "Password")
        column_width = 130

        # Formatting columns
        staff_tree.column("#0", width=0, minwidth=0)
        staff_tree.column("ID", anchor='center', width=90, minwidth=90)
        staff_tree.column("Name", anchor='w', width=column_width, minwidth=column_width)
        staff_tree.column("Role",  anchor='w', width=column_width, minwidth=column_width)
        staff_tree.column("Password", anchor='center', width=column_width, minwidth=column_width)

        # Formatting Headers 
        staff_tree.heading("ID", text="Staff ID",anchor='w')
        staff_tree.heading("Name", text="Staff Name",anchor='center')
        staff_tree.heading("Role", text="Role",anchor='center')
        staff_tree.heading("Password", text="Password",anchor='e')

        # Add tag configurations for odd and even rows
        staff_tree.tag_configure('oddrow', background='white', foreground='black')
        staff_tree.tag_configure('evenrow', background='lightgray', foreground='black')

        # For loop to generate the values in the database 
        count = 0
        for record in data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            staff_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]), tags=(tag,))
            count += 1

        staff_tree.pack(pady=10)

    # bottom bar -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#1A1A1A')
        bottom_label.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()

