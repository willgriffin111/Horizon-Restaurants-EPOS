'''
Author: Niel Paraggua
Date: 18/12/2023
Version: 1.0
'''

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta




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
    
    
    def update_graph(self, days, totalSales, selected):
        print("Updating graph...")  
        self.dowloadReport_btn = tk.Button(self.dateInputFrame, text="Download Report")
        self.dowloadReport_btn.pack(side=tk.LEFT, padx=10)
            
        if selected == "Show All Restaurants":
            self.cleargraph()
            # Plotting the new graph
            fig, ax = plt.subplots(figsize=(5, 4), dpi=75)
            ax.clear()  
            ax.plot(days, totalSales, label="Total Sales of All Restaurants")
            ax.set(xlabel='Date', ylabel='Sales (£)', title='Weekly Sales Data - All Restaurants')
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
            ax.set(xlabel='Date', ylabel='Sales (£)', title=f'Weekly Sales Data - {selected}')
            ax.grid()
            plt.xticks(rotation=45)
            plt.tight_layout()


            self.canvas = FigureCanvasTkAgg(fig, master=self.contentFrame)  
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
            
    def cleargraph(self):
        if hasattr(self, 'canvas'):
                self.canvas.get_tk_widget().destroy()

        
    
    # Staff performace tree view table ------------------------------------------------------------------------------------------------------------------------------------------------------------------|

    def showStaffReports(self):
        self.clearContent()
        self.top_frame = tk.Frame(self.contentFrame,bg='white')
        self.top_frame.pack(pady=20)

        self.frame_label = tk.Label(self.top_frame, text='Staff Performance', fg='black', bg='white', font=("Arial", 15))
        self.frame_label.pack()
        
        self.staff_perform_table_space()


    def staff_perform_table_space(self):
        self.mid_frame = tk.Frame(self.contentFrame, bg='white')
        self.mid_frame.pack(side='left',padx=10)
        
        self.dowloadReport_btn = tk.Button(self.top_frame, text="Download Report")
        self.dowloadReport_btn.pack(pady=10)

        self.mid_lbl_frame = tk.Frame(self.mid_frame, bg='white')
        self.mid_lbl_frame.pack()

        self.profit_label = tk.Label(self.mid_lbl_frame, text='Staff profit record', fg='black', bg='white', font=("Arial", 11))
        self.profit_label.pack(side='left',padx=70,pady=10)

        self.profit_label = tk.Label(self.mid_lbl_frame, text='Staff order record', fg='black', bg='white', font=("Arial", 11))
        self.profit_label.pack(side='left',padx=70,pady=10)
 
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
        self.bottomLabel = tk.Label(self.bottomFrame, text="", bg='black')
        self.bottomLabel.pack()

