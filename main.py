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

        # Entry for the user code
        userCodeLabel = tk.Label(container, text="User code:", bg='#1A58B5', fg='white', anchor='w', font=('inter', 14))
        userCodeLabel.pack(fill='x')
        userCodeEntry = tk.Entry(container, font=('inter', 14))
        userCodeEntry.pack(fill='x', pady=5)

        # Entry for the password
        passwordLabel = tk.Label(container, text="Password:", bg='#1A58B5', fg='white', anchor='w', font=('inter', 14))
        passwordLabel.pack(fill='x')
        passwordEntry = tk.Entry(container, show="*", font=('inter', 14))
        passwordEntry.pack(fill='x', pady=5)

        # Login button
        loginButton = tk.Button(container, text='Login',bg='white', command=self.login, fg='#1A58B5',width=20,height=2, font=('inter', 14))
        loginButton.pack(pady=20)

    def login(self):
        print("Login")

if __name__ == "__main__":
    app = App()
    app.mainloop()
