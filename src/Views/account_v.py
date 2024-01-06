import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel

'''
Author Jevhan Seechurn,
Date: 13/12/2023 3am lmao
Version: 1.0
'''

class AccountView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='white')
        self.topbar()
        self.bottombar()
        self.Sidebar()
        self.account_detail_frame()
        self.account_button_frame()




    # Update account Window ------------------------------------------------------------------------------------------------------------------------------------------------|

    def update_account_pop(self):

        self.staff_window = Toplevel(self)
        self.staff_window.title("Update Account")
        self.staff_window.geometry('250x350')
        self.staff_window.configure(bg='white')
        self.staff_window.resizable(False, False)

        self.update_title = tk.Label(self.staff_window, text='Update Account', fg='black', bg='white', font=("Arial", 18))
        self.update_title.pack(pady=10)

        self.update_name = tk.Label(self.staff_window, text='Full Name:', fg='black', bg='white', font=("Arial", 14))
        self.update_name.pack(pady=10)

        self.name_box = tk.Entry(self.staff_window, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        self.name_box.pack()

        self.submit_name_btn = tk.Button(
            self.staff_window,
            width=4,
            height=2,
            text='Submit',
            borderwidth=0
        )
        self.submit_name_btn.pack(pady=20)

    


    # Change password Window ------------------------------------------------------------------------------------------------------------------------------------------------|

    def change_pass_pop(self):
        

        self.staff_window = Toplevel(self)
        self.staff_window.title("Password Change")
        self.staff_window.geometry('250x300')
        self.staff_window.configure(bg='white')
        self.staff_window.resizable(False, False)

        self.change_title = tk.Label(self.staff_window, text='Change Password', fg='black', bg='white', font=("Arial", 18))
        self.change_title.pack(pady=10)

        self.new_password = tk.Label(self.staff_window, text='New password:', fg='black', bg='white', font=("Arial", 14))
        self.new_password.pack(pady=10)

        self.new_password_box = tk.Entry(self.staff_window, show="*", width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        self.new_password_box.pack()

        self.re_password = tk.Label(self.staff_window, text='Re-enter Password:', fg='black', bg='white', font=("Arial", 14))
        self.re_password.pack(pady=10)

        self.re_password_box = tk.Entry(self.staff_window, show="*", width=14, fg='black', bg='lightgrey', borderwidth=0)
        self.re_password_box.pack()


        self.submit_password_btn = tk.Button(
            self.staff_window,
            width=4,
            height=2,
            text='Submit',
            borderwidth=0,
            
        )
        self.submit_password_btn.pack(pady=20)


    # Top bar ---------------------------------------------------------------------------------------------------------------------------------------------------------|

    def topbar(self):
        self.topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        self.topFrame.pack(fill=tk.X)

        self.label = tk.Label(self.topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        self.label.pack(fill=tk.BOTH, expand=True)

        self.top_underline = tk.Canvas(self.topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        self.top_underline.create_line(4, 2, 218, 2, width=2, fill='white')
        self.top_underline.pack(fill=tk.X)

    def Sidebar(self):
        self.sidebar = tk.Frame(self, height=478, bg='#474747')
        self.sidebar.pack(fill=tk.Y, side=tk.LEFT)

        self.side_label = tk.Label(self.sidebar,text="Staff Account",fg='white', bg='#474747', anchor='w', font=('Arial', 18),width=13)
        self.side_label.pack(padx=45,pady=15,anchor='center')

        self.log_off = tk.Button(self.sidebar, text='Log off', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.log_off.pack(pady=30)

        self.home_btn = tk.Button(self.sidebar, text='Home', bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None,width=15)
        self.home_btn.pack(pady=30)

    # Tree view staff details ---------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def account_detail_frame(self):
        self.detail_frame = tk.Frame(self, borderwidth=25, bg='white',width=1, height=1)
        self.detail_frame.pack()

        self.frame_label = tk.Label(self.detail_frame, text='Staff Detail', fg='black', bg='white', font=("Arial", 18))
        self.frame_label.pack(pady=10)

        self.staff_name = tk.Label(self.detail_frame,text='Hey there Alex Rogers', fg='black', bg='white', font=("Arial", 15))
        self.staff_name.pack(pady=10,anchor='w')

        self.staff_id = tk.Label(self.detail_frame,text='Staff ID: 12345678', fg='black', bg='white', font=("Arial", 15))
        self.staff_id.pack(pady=10,anchor='w')

        self.staff_role = tk.Label(self.detail_frame,text='Position: ', fg='black', bg='white', font=("Arial", 15))
        self.staff_role.pack(pady=10,anchor='w')

        self.staff_location = tk.Label(self.detail_frame,text='Location ID: NE14ABJ', fg='black', bg='white', font=("Arial", 15))
        self.staff_location.pack(pady=10,anchor='w')



    # Staff button functions ----------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def account_button_frame(self):
        self.button_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='white',height=120,width=480)
        self.button_frame.pack()

        self.editname_btn = tk.Button(self.button_frame, text='Update name ', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=11)
        self.editname_btn.pack(side=tk.LEFT,padx=6)

        self.editpassword_btn = tk.Button(self.button_frame, text='Update Password ', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=11,command=self.change_pass_pop)
        self.editpassword_btn.pack(side=tk.LEFT,padx=6)


    # bottom bar ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        self.bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        self.bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        self.bottom_label = tk.Label(self.bottomFrame, text="", bg='#1A1A1A')
        self.bottom_label.pack()



