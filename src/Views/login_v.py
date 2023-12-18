'''
Author: Will Griffin, Alex Rogers
Date: 14/12/2023
Version: 1.1
'''

import tkinter as tk

class LoginView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='#2976E9') 
        
        self.container = tk.Frame(self, bg='#1A58B5', pady=75, padx=75)
        self.container.place(relx=0.5, rely=0.5, anchor='center')

        # Title label
        self.title = tk.Label(self.container, text="HORIZON RESTAURANT", bg='#1A58B5', fg='white', font=('inter', 24, 'bold'))
        self.title.pack(fill='x', pady=(0, 20))
        
        # Entry for the user code
        self.userCodeLabel = tk.Label(self.container, text="User code:", bg='#1A58B5', fg='white', anchor='w', font=('inter', 14))
        self.userCodeLabel.pack(fill='x')
        self.staffId_entry = tk.Entry(self.container, font=('inter', 14))
        self.staffId_entry.pack(fill='x', pady=5)

        # Entry for the password
        self.passwordLabel = tk.Label(self.container, text="Password:", bg='#1A58B5', fg='white', anchor='w', font=('inter', 14))
        self.passwordLabel.pack(fill='x')
        self.password_entry = tk.Entry(self.container, show="*", font=('inter', 14))
        self.password_entry.pack(fill='x', pady=5)

        # Login button
        self.login_btn = tk.Button(self.container, text='Login' , fg='black', bg='#1A58B5', width=20, height=2, font=('inter', 14))
        self.login_btn.pack(pady=20)