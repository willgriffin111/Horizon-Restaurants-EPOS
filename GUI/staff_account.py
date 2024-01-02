import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel

'''
Author Jevhan Seechurn,
Date: 13/12/2023 3am lmao
Version: 1.0
'''

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('Staff Account')
        self.configure(bg='white')
        self.topbar()
        self.bottombar()
        self.Sidebar()
        self.account_detail_frame()
        self.account_button_frame()


    # button functions
    def staff_edit(self):
        print("staff edit button clicked")

    def menu_edit(self):
        print("menu edit button clicked")

    def home_btn(self):
        print("home button clicked")

    # Update account Window ------------------------------------------------------------------------------------------------------------------------------------------------|

    def update_account_pop(self):
        def destroy_window():
            self.staff_window.destroy()

        self.staff_window = Toplevel(self)
        self.staff_window.title("Update Account")
        self.staff_window.geometry('250x350')
        self.staff_window.configure(bg='white')
        self.staff_window.resizable(False, False)

        update_title = tk.Label(self.staff_window, text='Update Account', fg='black', bg='white', font=("Arial", 18))
        update_title.pack(pady=10)

        update_name = tk.Label(self.staff_window, text='Full Name:', fg='black', bg='white', font=("Arial", 14))
        update_name.pack(pady=10)

        name_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        name_box.pack()

        update_position = tk.Label(self.staff_window, text='Position:', fg='black', bg='white', font=("Arial", 14))
        update_position.pack(pady=10)

        position_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        position_box.pack()

        update_location = tk.Label(self.staff_window, text='Location:', fg='black', bg='white', font=("Arial", 14))
        update_location.pack(pady=10)

        location_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        location_box.pack()

        # Function to close the current window when the 'Add Staff' button is clicked
        def submit_and_destroy():
            self.add_staff_record(name_box, position_box, location_box)
            destroy_window()

        submit = tk.Button(
            self.staff_window,
            width=4,
            height=2,
            text='Submit',
            borderwidth=0,
            command=submit_and_destroy
        )
        submit.pack(pady=20)

    def add_staff_record(self, name_box, position_box, location_box):
        pass


    # Change password Window ------------------------------------------------------------------------------------------------------------------------------------------------|

    def change_pass_pop(self):
        def destroy_window():
            self.staff_window.destroy()

        self.staff_window = Toplevel(self)
        self.staff_window.title("Password Change")
        self.staff_window.geometry('250x300')
        self.staff_window.configure(bg='white')
        self.staff_window.resizable(False, False)

        change_title = tk.Label(self.staff_window, text='Change Password', fg='black', bg='white', font=("Arial", 18))
        change_title.pack(pady=10)

        new_password = tk.Label(self.staff_window, text='New password:', fg='black', bg='white', font=("Arial", 14))
        new_password.pack(pady=10)

        new_password_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        new_password_box.pack()

        re_password = tk.Label(self.staff_window, text='Re-enter Password:', fg='black', bg='white', font=("Arial", 14))
        re_password.pack(pady=10)

        re_password_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        re_password_box.pack()

        # Function to close the current window when the 'Add Staff' button is clicked
        def submit_and_destroy1():
            self.change_password(new_password_box, re_password_box)
            destroy_window()

        submit = tk.Button(
            self.staff_window,
            width=4,
            height=2,
            text='Submit',
            borderwidth=0,
            command=submit_and_destroy1
        )
        submit.pack(pady=20)

    def change_password(self, new_password_box, re_password_box):
        pass

    # Top bar ---------------------------------------------------------------------------------------------------------------------------------------------------------|

    def topbar(self):
        topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        topFrame.pack(fill=tk.X)

        label = tk.Label(topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)

        top_underline = tk.Canvas(topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        top_underline.create_line(4, 2, 218, 2, width=2, fill='white')
        top_underline.pack(fill=tk.X)

    def Sidebar(self):
        Sidebar = tk.Frame(self, height=478, bg='#474747')
        Sidebar.pack(fill=tk.Y, side=tk.LEFT)

        side_label = tk.Label(Sidebar,text="Staff Account",fg='white', bg='#474747', anchor='w', font=('Arial', 18),width=13)
        side_label.pack(padx=45,pady=15,anchor='center')

        log_off = tk.Button(Sidebar, text='Log off', command=self.staff_edit, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        log_off.pack(pady=30)

        home_btn = tk.Button(Sidebar, text='Home', command=self.home_btn, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        home_btn.pack(pady=30)

    # Tree view staff details ---------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def account_detail_frame(self):
        detail_frame = tk.Frame(self, borderwidth=25, bg='white',width=1, height=1)
        detail_frame.pack()

        frame_label = tk.Label(detail_frame, text='Staff Detail', fg='black', bg='white', font=("Arial", 18))
        frame_label.pack(pady=10)

        staff_name = tk.Label(detail_frame,text='Hey there Alex Rogers, here are you details', fg='black', bg='white', font=("Arial", 15))
        staff_name.pack(pady=10,anchor='w')

        staff_id = tk.Label(detail_frame,text='Staff ID: 12345678', fg='black', bg='white', font=("Arial", 15))
        staff_id.pack(pady=10,anchor='w')

        staff_role = tk.Label(detail_frame,text='Position: Maisies slave', fg='black', bg='white', font=("Arial", 15))
        staff_role.pack(pady=10,anchor='w')

        staff_location = tk.Label(detail_frame,text='Location ID: NE14ABJ', fg='black', bg='white', font=("Arial", 15))
        staff_location.pack(pady=10,anchor='w')



    # Staff button functions ----------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def account_button_frame(self):
        button_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=120,width=480)
        button_frame.pack()

        update_account = tk.Button(button_frame, text='Update name ', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=11,command=self.update_account_pop)
        update_account.pack(side=tk.LEFT,padx=6)

        remove_staff = tk.Button(button_frame, text='Update Password ', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=11,command=self.change_pass_pop)
        remove_staff.pack(side=tk.LEFT,padx=6)


    # bottom bar ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottom_label = tk.Label(bottomFrame, text="", bg='#1A1A1A')
        bottom_label.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()

