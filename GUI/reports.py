import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import numpy as np

salesData = {
    "2024-01-01": 1000,
    "2024-01-02": 1200,
    "2024-01-03": 1100,
    "2024-01-04": 800,
    "2024-01-05": 1250,
    "2024-01-06": 1300,
    "2024-01-07": 900,
    "2024-01-08": 950,
    "2024-01-09": 1230,
    "2024-01-10": 1100,
    "2024-01-11": 980,
    "2024-01-12": 1180,
    "2024-01-13": 1270,
    "2024-01-14": 930,
    "2024-01-15": 1150,
    "2024-01-16": 1190,
    "2024-01-17": 1260,
    "2024-01-18": 1050,
    "2024-01-19": 1340,
    "2024-01-20": 980,
    "2024-01-21": 1100,
    "2024-01-22": 1070,
    "2024-01-23": 1230,
    "2024-01-24": 1120,
    "2024-01-25": 1250,
    "2024-01-26": 1300,
    "2024-01-27": 940,
    "2024-01-28": 980,
    "2024-01-29": 1150,
    "2024-01-30": 1200,
    "2024-01-31": 1100,
    "2024-02-01": 1180,
    "2024-02-02": 1220,
    "2024-02-03": 1300,
    "2024-02-04": 900,
    "2024-02-05": 1000,
    "2024-02-06": 1150,
    "2024-02-07": 950,
    "2024-02-08": 1250,
    "2024-02-09": 1100,
    "2024-02-10": 1200,
    "2024-02-11": 1180,
    "2024-02-12": 1320,
    "2024-02-13": 1250,
    "2024-02-14": 940,
    "2024-02-15": 980,
    "2024-02-16": 1150,
    "2024-02-17": 1200,
    "2024-02-18": 1100,
    "2024-02-19": 1180,
    "2024-02-20": 1220,
    "2024-02-21": 1300,
    "2024-02-22": 900,
    "2024-02-23": 1000,
    "2024-02-24": 1150,
    "2024-02-25": 950,
    "2024-02-26": 1250,
    "2024-02-27": 1100,
    "2024-02-28": 1200
}

# Thanks gpt
def group_sales_by_week(sales_data):
    grouped_data = {}
    for date_str, sales in sales_data.items():
        date = datetime.strptime(date_str, "%Y-%m-%d")
        start_of_week = date - timedelta(days=date.weekday())
        week_str = start_of_week.strftime("%Y-%m-%d")
        if week_str not in grouped_data:
            grouped_data[week_str] = 0
        grouped_data[week_str] += sales
    return grouped_data

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title('Reports')
        self.configure(bg='white')

        self.topBar()
        self.bottomBar()
        self.sideBar()
        self.contentFrame = tk.Frame(self, bg='white')
        self.contentFrame.pack(fill=tk.BOTH, expand=True)
        self.showSalesReports()
        
    def home(self):
        print("Home")

    def showSalesReports(self):
        self.clearContent()
        salesLabel = tk.Label(self.contentFrame, text="Weekly Sales Reports", font=('Arial', 20))
        salesLabel.pack(pady=20)

        weekly_sales_data = group_sales_by_week(salesData)

        weeks = list(weekly_sales_data.keys())
        weekly_sales = list(weekly_sales_data.values())

        statsFrame = tk.Frame(self.contentFrame)
        statsFrame.pack(pady=10)

        totalRevenue = sum(weekly_sales)
        totalRevenueLabel = tk.Label(statsFrame, text=f"Total Revenue: £{totalRevenue}", font=('Arial', 14))
        totalRevenueLabel.pack(side=tk.LEFT, padx=10)
        
        totalProfit = sum([s * 0.1 for s in weekly_sales])  # Assuming 10% profit for simplicity
        totalProfitLabel = tk.Label(statsFrame, text=f"Total Profit: £{totalProfit:.2f}", font=('Arial', 14))
        totalProfitLabel.pack(side=tk.LEFT, padx=10)
        
        profitMargin = (totalProfit / totalRevenue) * 100 
        profitMarginLabel = tk.Label(statsFrame, text=f"Profit Margin: {profitMargin:.2f}%", font=('Arial', 14))
        profitMarginLabel.pack(side=tk.LEFT, padx=10)

        fig, ax = plt.subplots()
        ax.plot(weeks, weekly_sales)
        ax.set(xlabel='Week Starting', ylabel='Sales (£)', title='Weekly Sales Data')
        ax.grid()
        plt.xticks(rotation=45)

        canvas = FigureCanvasTkAgg(fig, master=self.contentFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




    def showStaffReports(self):
        self.clearContent()
        staffLabel = tk.Label(self.contentFrame, text="Staff Reports", font=('Arial', 20))
        staffLabel.pack(pady=20)

    def clearContent(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()

    def topBar(self):
        topFrame = tk.Frame(self, borderwidth=25, relief=tk.FLAT, bg='#1A1A1A')
        topFrame.pack(fill=tk.X)

        titleLabel = tk.Label(topFrame, text="Horizon Restaurant", fg='white', bg='#1A1A1A', anchor='w', font=('Arial', 25), underline=True)
        titleLabel.pack(fill=tk.BOTH, expand=True)

        topUnderline = tk.Canvas(topFrame, height=2, bg='#1A1A1A', highlightthickness=0)
        topUnderline.create_line(4, 2, 218, 2, width=2, fill='white')
        topUnderline.pack(fill=tk.X)
        
        usernameLabel = tk.Label(topFrame, text=" Admin: Alex Rogers ", fg='white', bg='#1A1A1A', font=('Arial', 14))
        usernameLabel.pack(side=tk.RIGHT, anchor='e')
        usernameLabel.place(relx=1.0, rely=0.5, anchor='e', x=-110, y=4)

        userIdLabel = tk.Label(topFrame, text="ID: 193812", fg='white', bg='#1A1A1A', font=('Arial', 14))
        userIdLabel.pack(side=tk.RIGHT, anchor='e')
        userIdLabel.place(relx=1.0, rely=0.5, anchor='e', x=-10, y=4)

    def sideBar(self):
        sideBar = tk.Frame(self, height=478, bg='#474747')
        sideBar.pack(fill=tk.Y, side=tk.LEFT)

        sideLabel = tk.Label(sideBar, text="Reports", fg='white', bg='#474747', anchor='w', font=('Arial', 18), width=13)
        sideLabel.pack(padx=45, pady=15)
        
        homeBtn = tk.Button(sideBar, text='Home', command=self.home, bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=15)
        homeBtn.pack(pady=30)
        
        salesReportsBtn = tk.Button(sideBar, text='Sales Reports', command=self.showSalesReports, bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=15)
        salesReportsBtn.pack(pady=30)
        
        staffReportsBtn = tk.Button(sideBar, text='Staff Reports', command=self.showStaffReports, bd=0, highlightthickness=0, highlightbackground='#2976E9', pady=10, border=None, width=15)
        staffReportsBtn.pack(pady=30)

    def bottomBar(self):
        bottomFrame = tk.Frame(self, borderwidth=7, relief=tk.FLAT, bg='black')
        bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)
        bottomLabel = tk.Label(bottomFrame, text="", bg='#1A1A1A')
        bottomLabel.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
