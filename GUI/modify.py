'''
FILE NAME: modify.py
AUTHOR: Will Griffin, Jevhan Seechurn
DATE: 19/12/2023
VERSION: 1.0
'''


import tkinter as Tk
from tkinter import Toplevel, messagebox

userName = "Will Griffin"
userId = "193812"
totalDiscount = 0


# FIRST ITEM IS THE ITEM NAME, SECOND IS THE QUANTITY, THIRD IS PRICE
order = {
            "Starter 1": (1, 6.50),
            "Main 3": (2, 10.00),
            "Dessert 5": (1, 4.50)
        }


class App(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Modify Page")
        self.configure(bg="#1A58B5")
        self.resizable(False, False)
        self.sidebar()
        self.topbar(userName=userName, userID=userId)
        self.mainButtons()
        self.bottombar()
        self.updateItemList()

        self.discount_window = None


    # Note Window ------------------------------------------------------------------------------------------------------------------------------------------------|

    def display_notes(self):
        self.discount_window = Toplevel(self)
        self.discount_window.title("Notes")
        self.discount_window.geometry('400x200')
        self.discount_window.configure(bg='#1A58B5')
        self.discount_window.resizable(False, False)
        self.discount_window.columnconfigure((0,1,2), weight=1)
        self.discount_window.rowconfigure((0,2), weight=1)
        self.discount_window.rowconfigure(1, weight=5)

        notes_label = Tk.Label(self.discount_window, text="Enter notes:", fg="white", bg="#1A58B5", font=("Arial", 16))
        notes_label.grid(column=0, row=0, sticky='ew')

        self.notes_text = Tk.Text(self.discount_window, height=2, width=40, font=("Arial", 15))
        self.notes_text.grid(column=0, sticky='ew',row=1, pady=15)

        button_frame = Tk.Frame(self.discount_window)
        button_frame.configure(bg='#1A58B5')
        button_frame.grid(column=0, row=2, sticky='we')
        button_frame.columnconfigure((0,1,2), weight=1)
        button_frame.rowconfigure(0, weight=1)

        cancel_btn = Tk.Button(button_frame, text="Cancel", command=self.discount_window.destroy, height=2, width=10)
        cancel_btn.grid(column=0, row=0)

        clear_btn = Tk.Button(button_frame, text="Clear", height=2, width=10)
        clear_btn.grid(column=1, row=0)

        continue_btn = Tk.Button(button_frame, text="Continue", command=self.Continue, height=2, width=10)
        continue_btn.grid(column=2, row=0)

        # notes_label = Tk.Label(self.discount_window, text="Enter notes:", fg="white", bg="#1A58B5", font=("Arial", 16))
        # notes_label.pack(pady=15)
        
        # self.notes_text = Tk.Text(self.discount_window, height=2, width=40, font=("Arial", 15))
        # self.notes_text.pack(pady=15)
        
        # cancel_btn = Tk.Button(self.discount_window, text="Cancel", command=self.discount_window.destroy, height=2, width=10)
        # cancel_btn.pack(side=Tk.LEFT, padx=10, pady=10)

        # continue_btn = Tk.Button(self.discount_window, text="Continue", command=self.Continue, height=2, width=10)
        # continue_btn.pack(side=Tk.RIGHT, padx=10, pady=10)


    def Continue(self):
        notes = self.notes_text.get("1.0", Tk.END)
        '''
        USE NOTES VAR AND INSERT INTO DB
        '''
        print("Notes:", notes)  
        self.discount_window.destroy()




    # Top bar of window -----------------------------------------------------------------------------------------------------------------------------------------|
    def topbar(self, userName, userID):
        topFrame = Tk.Frame(self, borderwidth=25, relief=Tk.FLAT, bg="#2976E9")
        topFrame.pack(fill=Tk.X)

        label = Tk.Label(topFrame, text="Horizon Restaurant", fg="white", bg="#2976E9", anchor="w", font=("Arial", 16), underline=True)
        label.pack(fill=Tk.BOTH, expand=True)

        topUnderline = Tk.Canvas(topFrame, height=2, bg="#2976E9", highlightthickness=0)
        topUnderline.create_line(4, 2, 143, 2, width=2, fill="white")
        topUnderline.pack(fill=Tk.X)

        username = Tk.Label(topFrame, text=f"User: {userName}", fg="white", bg="#2976E9", font=("Arial", 12))
        username.pack(side=Tk.RIGHT, anchor="e")
        username.place(relx=1.0, rely=0.5, anchor="e", x=-170, y=4)

        userIDLabel = Tk.Label(topFrame, text=f"ID: {userID}", fg="white", bg="#2976E9", font=("Arial", 12))
        userIDLabel.pack(side=Tk.RIGHT, anchor="e")
        userIDLabel.place(relx=1.0, rely=0.5, anchor="e", x=-90, y=4)
        
        refresh_button = Tk.Button(topFrame, text='Home', command=self.home, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        refresh_button.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

    def sidebar(self):
        self.sidebar = Tk.Frame(self, width=400, height=478, bg="#F0FFFF")
        self.sidebar.pack(fill=Tk.Y, side=Tk.LEFT)

        topBox = Tk.Frame(self.sidebar, bg="#F0FFFF")
        topBox.pack(anchor="nw", padx=10, pady=10)

        continue_btn = Tk.Button(topBox, text="Continue", bg="white", padx=20, pady=0, borderwidth=0, highlightthickness=0, height=4, width=17)
        continue_btn.pack(side=Tk.LEFT)

        posFrame = Tk.Frame(self.sidebar, bg="#F0FFFF", borderwidth=0, highlightthickness=0, border=None)
        posFrame.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)

        self.itemList = Tk.Listbox(posFrame, bg="#F0FFFF", fg='black',height=24)
        self.itemList.pack(fill=Tk.BOTH)

        Cancel_btn = Tk.Button(self.sidebar, text="Cancel",bg="white", padx=20, pady=0, borderwidth=0, highlightthickness=0, height=4, width=17)
        Cancel_btn.place(x=10, y=525)
        

    def get_selected_item(self):
        try:
            selected_index = self.itemList.curselection()[0]
            selected_item = self.itemList.get(selected_index)
            selected_item_key = " ".join(selected_item.split()[:2])  
            return selected_item_key
        except:
            messagebox.showerror("Error", "No item selected")
            return None

    def updateItemList(self):
        self.itemList.delete(0, Tk.END)
    
        for item, (quantity, price) in order.items():
            entry = f"{item} x {quantity} - £{price * quantity}"
            self.itemList.insert(Tk.END, entry)

        
    def mainButtons(self):
        box_height = 5
        box_width = 5

        Add_btn = Tk.Button(self,text="+",bg="white", padx=20, pady=0, borderwidth=0, highlightthickness=0, height=box_height, width=box_width, command=self.increaseQuantity)
        Add_btn.pack(side=Tk.LEFT,padx=10,pady=10)

        minus_btn = Tk.Button(self,text="-",bg="white", padx=20, pady=0, borderwidth=0, highlightthickness=0, height=box_height, width=box_width, command=self.decreaseQuantity)
        minus_btn.pack(side=Tk.LEFT,padx=10,pady=10)

        Notes_btn = Tk.Button(self,text="Notes",bg="white", padx=20, pady=0, borderwidth=0, highlightthickness=0, height=box_height, width=box_width,command=self.display_notes)
        Notes_btn.pack(side=Tk.RIGHT,padx=10,pady=10)

        delete_btn = Tk.Button(self,text="Delete",bg="white", padx=20, pady=0, borderwidth=0, highlightthickness=0, height=box_height, width=box_width, command=self.deleteItem)
        delete_btn.pack(side=Tk.RIGHT,padx=10,pady=10)

    def increaseQuantity(self):
        '''
        THIS WILL BE DB FUNCTIONS TO INCREASE QUANTITY IN THE DB AND UPDATE THE GUI WITH updateItemList()
        '''
        selected_item = self.get_selected_item()
        if selected_item:
            quantity, price = order[selected_item]
            order[selected_item] = (quantity + 1, price)
            self.updateItemList()
            
        

    def decreaseQuantity(self):
        '''
        THIS WILL BE DB FUNCTIONS TO INCREASE DECREASE IN THE DB AND UPDATE THE GUI WITH updateItemList()
        '''
        selected_item = self.get_selected_item()
        if selected_item:
            quantity, price = order[selected_item]
            if quantity > 1:  # MAKES SURE QUANTITY DOESN'T GO BELOW 1
                order[selected_item] = (quantity - 1, price)
                self.updateItemList()

    def deleteItem(self):
        '''
        THIS WILL BE DB FUNCTIONS TO INCREASE REMOVE FROM THE DB AND UPDATE THE GUI WITH updateItemList()
        '''
        selected_item = self.get_selected_item()
        if selected_item:
            del order[selected_item]
            self.updateItemList()
            
    # Bottom bar -----------------------------------------------------------------------------------------------------------------------------------------|
    def bottombar(self):
        bottomFrame = Tk.Frame(self, borderwidth=7, relief=Tk.FLAT, bg='#2976E9')
        bottomFrame.pack(fill=Tk.X, side=Tk.BOTTOM)
        bottom_label = Tk.Label(bottomFrame, text="", bg='#2976E9')
        bottom_label.pack()

        
    def home(self):
        print("Home")

        

if __name__ == "__main__":
    app = App()
    app.mainloop()