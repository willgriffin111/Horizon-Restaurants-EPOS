'''
Auther Will Griffin
Date: 12/12/2023
Version: 1.0
'''
import tkinter as tk
from tkinter import ttk, Toplevel

inventoryData = [
    ['123', 'potato', '123', '123', 'ingredient'],
    ['456', 'Apples', '456', '456', 'ingredient'],
    ['789', 'Oranges', '789', '789', 'ingredient'],
    ['111', 'Bananas', '111', '111', 'ingredient'],
    ['222', 'Berries', '222', '222', 'ingredient'],
    ['333', 'Grapes', '333', '333', 'ingredient'],
    ['444', 'Pineapple', '444', '444', 'ingredient'],
    ['555', 'Watermelon', '555', '555', 'ingredient'],
    ['666', 'Peaches', '666', '666', 'ingredient'],
    ['777', 'Plums', '777', '777', 'ingredient'],
    ['888', 'Kiwi', '888', '888', 'ingredient'],
    ['999', 'Mango', '999', '999', 'ingredient'],
    ['101', 'Strawberries', '101', '101', 'ingredient'],
    ['202', 'Blueberries', '202', '202', 'ingredient'],
    ['303', 'Raspberries', '303', '303', 'ingredient'],
    ['404', 'Blackberries', '404', '404', 'ingredient'],
    ['505', 'Pears', '505', '505', 'ingredient'],
    ['606', 'Cherries', '606', '606', 'ingredient'],
    ['707', 'Lemons', '707', '707', 'ingredient'],
    ['808', 'Limes', '808', '808', 'ingredient'],
    ['909', 'Spoons', '909', '909', 'equipment'],
    ['010', 'Forks', '010', '010', 'equipment'],
    ['111', 'Knives', '111', '111', 'equipment'],
    ['212', 'Plates', '212', '212', 'equipment'],
    ['313', 'Bowls', '313', '313', 'equipment']
]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('Horizon Restaurant')
        self.resizable(False, False)
        self.configure(bg='#1A58B5')
        self.topBar()
        self.inventoryTree()
        self.inv_table_space()
        
    def topBar(self):

        topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#2976E9')
        topFrame.pack(fill=tk.X)

        # The Label 'Horizon Restaurant'
        label = tk.Label(topFrame, text="Horizon Restaurant", fg='white', bg='#2976E9', anchor='w', font=('Arial', 25), underline=True)
        label.pack(fill=tk.BOTH, expand=True)

        # Underlines the Label 
        canvas = tk.Canvas(topFrame, height=2, bg='#2976E9', highlightthickness=0)
        canvas.create_line(4, 2, 218, 2, width=2, fill='white')
        canvas.pack(fill=tk.X)

        # Username
        username = tk.Label(topFrame, text=" User: Gordon ", fg='white', bg='#2976E9', font=('Arial', 14))
        username.pack(side=tk.RIGHT, anchor='e')
        username.place(relx=1.0, rely=0.5, anchor='e', x=-350, y=4)

        # User ID
        user_id = tk.Label(topFrame, text="ID: 193812", fg='white', bg='#2976E9', font=('Arial', 14))
        user_id.pack(side=tk.RIGHT, anchor='e')
        user_id.place(relx=1.0, rely=0.5, anchor='e', x=-260, y=4)

        # Refresh Button
        refresh_button = tk.Button(topFrame, text='Refresh', command=self.refreshGUI, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        refresh_button.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        # Home Button
        refresh_button = tk.Button(topFrame, text='Home', command=self.home, bd=0, highlightthickness=0,highlightbackground='#2976E9', pady=10, border=None)
        refresh_button.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)
        
        # mainFrame = tk.Frame(self, bg='#1A58B5')
        # mainFrame.pack(fill=tk.BOTH, expand=True)
        
    def inventoryTree(self):
        self.inventory_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A58B5', height=120, width=480)
        self.inventory_frame.pack()
        self.inventory_frame.lower()

        frame_label = tk.Label(self.inventory_frame, text='Inventory Management', fg='black', bg='#1A58B5', font=("Arial", 18))
        frame_label.pack(pady=10)

        add_staff = tk.Button(self.inventory_frame, text='Add', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5,command=self.add_inventory_pop)
        add_staff.pack(side=tk.LEFT,padx=6)

        remove_staff = tk.Button(self.inventory_frame, text='Delete', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        remove_staff.pack(side=tk.LEFT,padx=6)

        # edit_staff = tk.Button(self.inventory_frame, text='Edit', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=5)
        # edit_staff.pack(side=tk.LEFT,padx=6)

        options = ['All', 'Ingredient','Equipment']
        selected_option = tk.StringVar(self.inventory_frame)
        selected_option.set(options[0])  # Set default value

        option_menu = tk.OptionMenu(self.inventory_frame, selected_option, *options)
        option_menu.configure(bg='#1A58B5',fg='black',width=10)
        option_menu.pack(anchor='n')
        
    def add_inventory_pop(self):


        self.inventory_window = Toplevel(self)
        self.inventory_window.title("Inventory add")
        self.inventory_window.geometry('250x400')
        self.inventory_window.configure(bg='#1A58B5')
        self.inventory_window.resizable(False, False)
    
        add_title = tk.Label(self.inventory_window, text='New Inventory', fg='black', bg='white', font=("Arial", 18))
        add_title.pack(pady=10)
    
        add_name = tk.Label(self.inventory_window, text='Item name:', fg='black', bg='white', font=("Arial", 14))
        add_name.pack(pady=10)
    
        name_box = tk.Entry(self.inventory_window, width=14, fg='black', bg='lightgrey', borderwidth=0, border=None)
        name_box.pack()
    
        add_qty = tk.Label(self.inventory_window, text='Quantity:', fg='black', bg='white', font=("Arial", 14))
        add_qty.pack(pady=10)
    
        qty_box = tk.Entry(self.inventory_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        qty_box.pack()
    
        add_reorder = tk.Label(self.inventory_window, text='Re-order level:', fg='black', bg='white', font=("Arial", 14))
        add_reorder.pack(pady=10)

        reorder_box = tk.Entry(self.inventory_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        reorder_box.pack()

        inv_type = tk.Label(self.inventory_window, text='Type:', fg='black', bg='white', font=("Arial", 14))
        inv_type.pack(pady=10)
    
        type_box = tk.Entry(self.inventory_window, width=14, fg='black', bg='lightgrey', borderwidth=0)
        type_box.pack()
    
    def inv_table_space(self):
        self.inventory_table_frame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A58B5', height=300, width=480)
        self.inventory_table_frame.pack(pady=10)
        self.inventory_table_frame.lower()

        self.inventory_tree = ttk.Treeview( self.inventory_table_frame,height=15)
        self.inventory_tree['columns'] = ("ID", "Name", "Qty", "re-order","inventory-type")
        column_width = 120

        # Formatting columns
        self.inventory_tree.column("#0", width=0, minwidth=0)
        self.inventory_tree.column("ID", anchor='center', width=90, minwidth=90)
        self.inventory_tree.column("Name", anchor='w', width=column_width, minwidth=column_width)
        self.inventory_tree.column("Qty",  anchor='w', width=35, minwidth=35)
        self.inventory_tree.column("re-order", anchor='center', width=column_width, minwidth=column_width)
        self.inventory_tree.column("inventory-type", anchor='w', width=column_width, minwidth=column_width)

        # Formatting Headers 
        self.inventory_tree.heading("ID", text="Item ID",anchor='w')
        self.inventory_tree.heading("Name", text="Item Name",anchor='center')
        self.inventory_tree.heading("Qty", text="Qty",anchor='center')
        self.inventory_tree.heading("re-order", text="Re-order level",anchor='e')
        self.inventory_tree.heading("inventory-type", text="Inventory type",anchor='e')

        # Add tag configurations for odd and even rows
        self.inventory_tree.tag_configure('oddrow', background='white', foreground='black')
        self.inventory_tree.tag_configure('evenrow', background='lightgray', foreground='black')


        # For loop to generate the values in the database 
        count = 0
        for record in inventoryData:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            self.inventory_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3],record[4]), tags=(tag,))
            count += 1
            
        self.inventory_tree.bind("<Double-1>", self.onDoubleClick)

        self.inventory_tree.pack(pady=10)
        
        
        
    def refreshGUI(self):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
        self.topBar()
        self.inventoryTree()
        self.inv_table_space()   

        
            
    def onDoubleClick(self, event):
        rowId = self.inventory_tree.identify_row(event.y)
        columnId = self.inventory_tree.identify_column(event.x)
        if rowId and columnId:
            self.editWindowPopup(self.inventory_tree, rowId, columnId)
        
    def editWindowPopup(self, tree, row_id, column_id):
        editWindow = Toplevel(self)
        editWindow.title("Edit Cell Value")
        editWindow.geometry("300x100")

        # Calculate column index
        column_index = int(column_id.replace('#', '')) - 1
        current_value = tree.item(row_id, 'values')[column_index]

        newValueUI = tk.Entry(editWindow)
        newValueUI.pack(pady=10)
        newValueUI.insert(0, current_value)
        
        saveButton = tk.Button(editWindow, text="Save", command=lambda: self.saveNewValue(tree, row_id, column_index, newValueUI.get(), editWindow))
        saveButton.pack()

    def saveNewValue(self, tree, row_id, column_index, new_value, edit_window):
        currentValues = list(tree.item(row_id, 'values'))
        currentValues[column_index] = new_value
        tree.item(row_id, values=currentValues)
        edit_window.destroy()

    
    def home(self):
        print("Home")

          

if __name__ == "__main__":
    app = App()
    app.mainloop()
