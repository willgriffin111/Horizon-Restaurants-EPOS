
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title('Login')
        self.configure(background='#2976E9')  
        self.create_widgets()


    def create_widgets(self):        
        username = tk.StringVar()
        password = tk.StringVar()

        fields = {} # dictionary
        fields['username_label'] = ttk.Label(text='User ID:')
        fields['username'] = ttk.Entry(textvariable=username)   
        fields['password_label'] = ttk.Label(text='Password:')
        fields['password'] = ttk.Entry(textvariable=password, show="*")
        

        for field in fields.values():

            field.pack(anchor=tk.W, padx=50, pady=5, fill=tk.X, background='black')




        ttk.Button(text='Login', command=lambda : self.login(username, password)).pack(anchor=tk.W, padx=10, pady=5)    
    
    def login(self, username, password):
        print("User name : " + username.get() + "\nPassword : " + password.get())
        # tkm.showinfo("Alert!", "User name : " + username.get() + "\nPassword : " + password.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()


