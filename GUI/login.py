""" 
AUTHOR : WILL GRIFFIN
DATE : 29/11/2023
VERSION : 1.0
"""
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")  
        self.title('Horizon Restaurant')
        self.configure(bg='#2976E9')  
        self.create_widgets()

    def create_widgets(self):
        
        container = tk.Frame(self, bg='#1A58B5', pady=75, padx=75)
        container.place(relx=0.5, rely=0.5, anchor='center')

        # Title label
        title = tk.Label(container, text="HORIZON RESTAURANT", bg='#1A58B5', fg='white', font=('inter', 24, 'bold'))
        title.pack(fill='x', pady=(0, 20))

        username = tk.StringVar()
        password = tk.StringVar()
        
        # Entry for the user code
        userCodeLabel = tk.Label(container, text="User code:", bg='#1A58B5', fg='white', anchor='w', font=('inter', 14))
        userCodeLabel.pack(fill='x')
        userCodeEntry = tk.Entry(container,textvariable=username, font=('inter', 14))
        userCodeEntry.pack(fill='x', pady=5)

        # Entry for the password
        passwordLabel = tk.Label(container, text="Password:", bg='#1A58B5', fg='white', anchor='w', font=('inter', 14))
        passwordLabel.pack(fill='x')
        passwordEntry = tk.Entry(container, show="*",textvariable=password, font=('inter', 14))
        passwordEntry.pack(fill='x', pady=5)

        # Login button
        loginButton = tk.Button(container, text='Login', command=lambda : self.login(username, password), fg='black', bg='#1A58B5', width=20, height=2, font=('inter', 14))
        loginButton.pack(pady=20)

    def login(self, username, password):
        print(f"Username: {username.get()}  Password: {password.get()}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
