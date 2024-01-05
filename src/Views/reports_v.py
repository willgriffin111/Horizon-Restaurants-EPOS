import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta

salesData = {
    '2024-01-01': {
        'Birmingham': {'Restaurant1': 247, 'Restaurant2': 271},
        'Bristol': {'Restaurant1': 226, 'Restaurant2': 271},
        'Cardiff': {'Restaurant1': 196, 'Restaurant2': 264},
        'Glasgow': {'Restaurant1': 214, 'Restaurant2': 178},
        'Manchester': {'Restaurant1': 132, 'Restaurant2': 211},
        'Nottingham': {'Restaurant1': 188, 'Restaurant2': 267},
        'London': {'Restaurant1': 289, 'Restaurant2': 212}
    },
    '2024-01-10': {
        'Birmingham': {'Restaurant1': 247, 'Restaurant2': 248},
        'Bristol': {'Restaurant1': 228, 'Restaurant2': 125},
        'Cardiff': {'Restaurant1': 247, 'Restaurant2': 174},
        'Glasgow': {'Restaurant1': 134, 'Restaurant2': 223},
        'Manchester': {'Restaurant1': 218, 'Restaurant2': 248},
        'Nottingham': {'Restaurant1': 262, 'Restaurant2': 265},
        'London': {'Restaurant1': 269, 'Restaurant2': 253}
    },
    '2024-01-20': {
        'Birmingham': {'Restaurant1': 244, 'Restaurant2': 182},
        'Bristol': {'Restaurant1': 178, 'Restaurant2': 105},
        'Cardiff': {'Restaurant1': 103, 'Restaurant2': 291},
        'Glasgow': {'Restaurant1': 197, 'Restaurant2': 227},
        'Manchester': {'Restaurant1': 127, 'Restaurant2': 151},
        'Nottingham': {'Restaurant1': 177, 'Restaurant2': 245},
        'London': {'Restaurant1': 233, 'Restaurant2': 291}
    },
    '2024-01-30': {
        'Birmingham': {'Restaurant1': 121, 'Restaurant2': 296},
        'Bristol': {'Restaurant1': 293, 'Restaurant2': 223},
        'Cardiff': {'Restaurant1': 196, 'Restaurant2': 174},
        'Glasgow': {'Restaurant1': 169, 'Restaurant2': 154},
        'Manchester': {'Restaurant1': 187, 'Restaurant2': 238},
        'Nottingham': {'Restaurant1': 122, 'Restaurant2': 206},
        'London': {'Restaurant1': 162, 'Restaurant2': 192}
    },
    '2024-02-01': {
        'Birmingham': {'Restaurant1': 282, 'Restaurant2': 275},
        'Bristol': {'Restaurant1': 291, 'Restaurant2': 205},
        'Cardiff': {'Restaurant1': 255, 'Restaurant2': 126},
        'Glasgow': {'Restaurant1': 213, 'Restaurant2': 246},
        'Manchester': {'Restaurant1': 289, 'Restaurant2': 103},
        'Nottingham': {'Restaurant1': 287, 'Restaurant2': 240},
        'London': {'Restaurant1': 130, 'Restaurant2': 175}
    },
    '2024-02-10': {
        'Birmingham': {'Restaurant1': 264, 'Restaurant2': 178},
        'Bristol': {'Restaurant1': 144, 'Restaurant2': 279},
        'Cardiff': {'Restaurant1': 109, 'Restaurant2': 242},
        'Glasgow': {'Restaurant1': 271, 'Restaurant2': 139},
        'Manchester': {'Restaurant1': 261, 'Restaurant2': 257},
        'Nottingham': {'Restaurant1': 206, 'Restaurant2': 104},
        'London': {'Restaurant1': 187, 'Restaurant2': 180}
    },
    '2024-02-20': {
        'Birmingham': {'Restaurant1': 189, 'Restaurant2': 106},
        'Bristol': {'Restaurant1': 156, 'Restaurant2': 242},
        'Cardiff': {'Restaurant1': 248, 'Restaurant2': 167},
        'Glasgow': {'Restaurant1': 225, 'Restaurant2': 201},
        'Manchester': {'Restaurant1': 206, 'Restaurant2': 247},
        'Nottingham': {'Restaurant1': 245, 'Restaurant2': 136},
        'London': {'Restaurant1': 222, 'Restaurant2': 152}
    }
}

staffData = {
    'Will': (100,20,64,35.599,105),
    'Neil': (200,122,1000,400,10,67)
}


class ReportView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='white')
        self.topBar()
        self.bottomBar()
        self.sidebar()
        self.contentFrame = tk.Frame(self, bg='white')
        self.contentFrame.pack(fill=tk.BOTH, expand=True)
        self.showSalesReports(["",""])
        

    def showSalesReports(self,restaurantOptions):
        self.clearContent()
        self.salesLabel = tk.Label(self.contentFrame, text="Weekly Sales Reports", font=('Arial', 20))
        self.salesLabel.pack(pady=20)

        self.dateInputFrame = tk.Frame(self.contentFrame)
        self.dateInputFrame.pack(pady=10)

        self.startDateFrame = tk.Frame(self.dateInputFrame)
        self.startDateFrame.pack(side=tk.LEFT, padx=10)
        tk.Label(self.startDateFrame, text="Start Date (YYYY-MM-DD):").pack()
        self.startDateEnrty = tk.Entry(self.startDateFrame)
        self.startDateEnrty.pack()

        self.endDateFrame = tk.Frame(self.dateInputFrame)
        self.endDateFrame.pack(side=tk.LEFT, padx=10)
        tk.Label(self.endDateFrame, text="End Date (YYYY-MM-DD):").pack()
        self.endDateEntry = tk.Entry(self.endDateFrame)
        self.endDateEntry.pack()

        self.updateGraphButton = tk.Button(self.dateInputFrame, text="Update Graph")
        self.updateGraphButton.pack(side=tk.LEFT, padx=10)
        
        self.totalSalesLabel = tk.Label(self.contentFrame, text="")
        self.totalSalesLabel.pack(pady=10)
        
        

        self.selectedRestaurnant = tk.StringVar()
        self.restaurantDropdown = ttk.Combobox(self.contentFrame, textvariable=self.selectedRestaurnant, values=restaurantOptions)
        self.restaurantDropdown.current(0)
        self.restaurantDropdown.pack(pady=10)
        


        
    def getRestaurantOptions(self):
        options = ["Show All Restaurants"]

        firstDayData = salesData[list(salesData.keys())[0]]

        for city in firstDayData:
            for restaurant in firstDayData[city]:
                options.append(f"{city} - {restaurant}")
                
        return options
    
    
    def update_graph(self, days, totalSales, selected):
        print("Updating graph...")  
        if selected == "Show All Restaurants":
            self.cleargraph()
            # Plotting the new graph
            fig, ax = plt.subplots(figsize=(5, 4), dpi=75)
            ax.clear()  
            ax.plot(days, totalSales, label="Total Sales of All Restaurants")
            ax.set(xlabel='Week Starting', ylabel='Sales (£)', title='Weekly Sales Data - All Restaurants')
            ax.grid()
            plt.xticks(rotation=45)
            plt.tight_layout()

            self.canvas = FigureCanvasTkAgg(fig, master=self.contentFrame)  
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        elif selected:  
    

            self.cleargraph()

            # Plotting the new graph
            fig, ax = plt.subplots(figsize=(5, 4), dpi=75)
            ax.clear()  
            ax.plot(days, totalSales, label=f"Sales of {selected}")
            ax.set(xlabel='Week Starting', ylabel='Sales (£)', title=f'Weekly Sales Data - {selected}')
            ax.grid()
            plt.xticks(rotation=45)
            plt.tight_layout()


            self.canvas = FigureCanvasTkAgg(fig, master=self.contentFrame)  
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
    def cleargraph(self):
        if hasattr(self, 'canvas'):
                self.canvas.get_tk_widget().destroy()

    # def showStaffReports(self):
    #     self.clearContent()
    #     self.staffLabel = tk.Label(self.contentFrame, text="Staff Reports", font=('Arial', 20))
    #     self.staffLabel.pack(pady=20)

    #     self.selected_employee = tk.StringVar()
    #     self.emplyeeOptions = list(staffData.keys())  
    #     self.employeeDropdown = ttk.Combobox(self.contentFrame, textvariable=self.selected_employee, values=self.emplyeeOptions)
    #     self.employeeDropdown.current(0)  # Default selection is the first option
    #     self.employeeDropdown.pack(pady=10)
    #     self.employeeDropdown.bind("<<ComboboxSelected>>", self.updateStaffReport) 

    #     self.totalSalesLabel = tk.Label(self.contentFrame, text="", font=('Arial', 16))
    #     self.totalSalesLabel.pack(pady=10)

    #     self.updateStaffReport()

    # def updateStaffReport(self, event=None):
    #     self.selectedEmployees = self.selected_employee.get()
    #     self.emplyeeSales = staffData[self.selectedEmployees]


    #     self.totalSales = sum(self.emplyeeSales)
    #     self.numberOfOrders = len(self.emplyeeSales)
    #     self.averageOrderPrice = self.totalSales / self.numberOfOrders 

    #     self.displayText = (f"Total Sales for {self.selectedEmployees}: £{self.totalSales}\n"
    #                     f"Number of Orders: {self.numberOfOrders}\n"
    #                     f"Average Order Price: £{self.averageOrderPrice:.2f}")
    #     self.totalSalesLabel.config(text=self.displayText)
        
    
    # Staff performace tree view table ------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def showStaffReports(self):
        self.clearContent()
        self.top_frame = tk.Frame(self.contentFrame,bg='white')
        self.top_frame.pack(pady=20)

        self.frame_label = tk.Label(self.top_frame, text='Staff Performance Score', fg='black', bg='white', font=("Arial", 15))
        self.frame_label.pack()
        self.staff_perform_table_space()


    def staff_perform_table_space(self):
        self.mid_frame = tk.Frame(self.contentFrame, bg='white')
        self.mid_frame.pack(side='left',padx=10)

        self.mid_lbl_frame = tk.Frame(self.mid_frame, bg='white')
        self.mid_lbl_frame.pack()

        self.profit_label = tk.Label(self.mid_lbl_frame, text='Staff profit record', fg='black', bg='white', font=("Arial", 11))
        self.profit_label.pack(side='left',padx=70,pady=20)

        self.profit_label = tk.Label(self.mid_lbl_frame, text='Staff order record', fg='black', bg='white', font=("Arial", 11))
        self.profit_label.pack(side='left',padx=70,pady=20)
 
# Staff performance tree view (Profits made ) -------------------------------------------------------------------------------------------------------------------------------------------------------|

        self.tree_view_frame = tk.Frame(self.mid_frame, bg='white')
        self.tree_view_frame.pack(side='left',padx=10)

        self.staff_profit_tree = ttk.Treeview(self.tree_view_frame,height=14)
        self.staff_profit_tree['columns'] = ("ID", "Name", "role", "profit")
        self.column_width = 65

        # Formatting columns
        self.staff_profit_tree.column("#0", width=0, minwidth=0)
        self.staff_profit_tree.column("ID", anchor='center', width=50, minwidth=30)
        self.staff_profit_tree.column("Name", anchor='w', width=self.column_width, minwidth=self.column_width)
        self.staff_profit_tree.column("role",  anchor='w', width=self.column_width, minwidth=self.column_width)
        self.staff_profit_tree.column("profit", anchor='center', width=50, minwidth=50)


        # Formatting Headers 
        self.staff_profit_tree.heading("ID", text="Staff ID",anchor='center')
        self.staff_profit_tree.heading("Name", text="Name",anchor='center')
        self.staff_profit_tree.heading("role", text="Position",anchor='center')
        self.staff_profit_tree.heading("profit", text="Profit total",anchor='center')


        # Add tag configurations for odd and even rows
        self.staff_profit_tree.tag_configure('oddrow', background='white', foreground='black')
        self.staff_profit_tree.tag_configure('evenrow', background='lightgray', foreground='black')


        self.style = ttk.Style()
        self.style.configure("Treeview", font=('Arial', 8)) 
        self.style.configure("Treeview.Heading", font=('Arial', 8, 'bold'))


        self.scrollbar = ttk.Scrollbar(self.tree_view_frame, orient='vertical', command=self.staff_profit_tree.yview)
        self.staff_profit_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        self.staff_profit_tree.pack(side='left')

        self.staff_profit_tree.pack(side='left')

# Staff performance tree view (Profits made ) -------------------------------------------------------------------------------------------------------------------------------------------------------|

        self.tree_view_frame = tk.Frame(self.mid_frame, bg='white')
        self.tree_view_frame.pack(side='left',padx=10)

        self.staff_order_tree = ttk.Treeview(self.tree_view_frame,height=14)
        self.staff_order_tree['columns'] = ("ID", "Name", "role", "order")

        # Formatting columns
        self.staff_order_tree.column("#0", width=0, minwidth=0)
        self.staff_order_tree.column("ID", anchor='center', width=50, minwidth=50)
        self.staff_order_tree.column("Name", anchor='w', width=self.column_width, minwidth=self.column_width)
        self.staff_order_tree.column("role",  anchor='w', width=self.column_width, minwidth=self.column_width)
        self.staff_order_tree.column("order", anchor='center', width=50, minwidth=50)


        # Formatting Headers 
        self.staff_order_tree.heading("ID", text="Staff ID",anchor='center')
        self.staff_order_tree.heading("Name", text="Name",anchor='center')
        self.staff_order_tree.heading("role", text="Position",anchor='center')
        self.staff_order_tree.heading("order", text="Order Total",anchor='center')


        # Add tag configurations for odd and even rows
        self.staff_order_tree.tag_configure('oddrow', background='white', foreground='black')
        self.staff_order_tree.tag_configure('evenrow', background='lightgray', foreground='black')


        self.style = ttk.Style()
        self.style.configure("Treeview", font=('Arial', 8)) 
        self.style.configure("Treeview.Heading", font=('Arial', 8, 'bold'))



        self.scrollbar = ttk.Scrollbar(self.tree_view_frame, orient='vertical', command=self.staff_order_tree.yview)
        self.staff_order_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        self.staff_order_tree.pack(side='left')

        self.staff_order_tree.pack(side='left')
        
    def insertIntoStaffProfit(self,data):
        count = 0
        for record in data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            self.staff_profit_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]), tags=(tag,))
            count += 1
            
    def insertIntoStaffOrder(self,data):
        count = 0
        for record in data:
            tag = 'evenrow' if count % 2 == 0 else 'oddrow'
            self.staff_order_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3]), tags=(tag,))
            count += 1



    def clearContent(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()

    def topBar(self):
        self.topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        self.topFrame.pack(fill=tk.X)

        self.titleLabel = tk.Label(self.topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        self.titleLabel.pack(fill=tk.BOTH, expand=True)

        self.topUnderline = tk.Canvas(self.topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        self.topUnderline.create_line(4, 2, 218, 2, width=2, fill='white')
        self.topUnderline.pack(fill=tk.X)
        
        self.usernameLabel = tk.Label(self.topFrame, text=" Admin: Alex Rogers ", fg='white', bg='#1A1A1A', font=('Arial', 14))
        self.usernameLabel.pack(side=tk.RIGHT, anchor='e')
        self.usernameLabel.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        self.userIdLabel = tk.Label(self.topFrame, text="ID: 193812", fg='white', bg='#1A1A1A', font=('Arial', 14))
        self.userIdLabel.pack(side=tk.RIGHT, anchor='e')
        self.userIdLabel.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

    def sidebar(self):
        self.sideBar = tk.Frame(self, height=478, bg='#474747')
        self.sideBar.pack(fill=tk.Y, side=tk.LEFT)

        self.sideLabel = tk.Label(self.sideBar, text="Reports", fg='white', bg='#474747', anchor='w', font=('Arial', 18), width=13)
        self.sideLabel.pack(padx=10, pady=15)
        
        self.homeBtn = tk.Button(self.sideBar, text='Home', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=15)
        self.homeBtn.pack(pady=30)
        
        self.salesReportsBtn = tk.Button(self.sideBar, text='Sales Reports', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=15)
        self.salesReportsBtn.pack(pady=30)
        
        self.staffReportsBtn = tk.Button(self.sideBar, text='Staff Reports', bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=15)
        self.staffReportsBtn.pack(pady=30)

    def bottomBar(self):
        self.bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        self.bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        self.bottomLabel = tk.Label(self.bottomFrame, text="", bg='#1A1A1A')
        self.bottomLabel.pack()

