import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import numpy as np

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

def groupSalesByWeek(salesData):
    groupedData = {}
    cities = ["Birmingham", "Bristol", "Cardiff", "Glasgow", "Manchester", "Nottingham", "London"]
    
    for dateStr, sales in salesData.items():
        date = datetime.strptime(dateStr, "%Y-%m-%d")
        sartOfWeek = date - timedelta(days=date.weekday())
        weekStr = sartOfWeek.strftime("%Y-%m-%d")

        if weekStr not in groupedData:
            groupedData[weekStr] = {city: {"Restaurant1": 0, "Restaurant2": 0} for city in cities}

        for city in sales:
            for restaurant, revenue in sales[city].items():
                groupedData[weekStr][city][restaurant] += revenue
    
    return groupedData

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

        self.selected_restaurant = tk.StringVar()
        restaurantOptions = self.getRestaurantOptions()
        restaurantDropdown = ttk.Combobox(self.contentFrame, textvariable=self.selected_restaurant, values=restaurantOptions)
        restaurantDropdown.current(0)  
        restaurantDropdown.pack(pady=10)
        restaurantDropdown.bind("<<ComboboxSelected>>", self.update_graph)  

        # Initial Graph
        self.update_graph()
        
    def getRestaurantOptions(self):
        options = ["Show All Restaurants"]

        firstDayData = salesData[list(salesData.keys())[0]]

        for city in firstDayData:
            for restaurant in firstDayData[city]:
                options.append(f"{city} - {restaurant}")
                
        return options
    
    
    def update_graph(self, event=None):
        print("Updating graph...")  
        selected = self.selected_restaurant.get()
        if selected == "Show All Restaurants":
            print("Showing data for all restaurants")

            weekly_sales_data = groupSalesByWeek(salesData)

            # Calculate total sales for all restaurants
            total_sales_per_week = {}
            for week, cities_data in weekly_sales_data.items():
                total_sales = 0
                for city in cities_data.values():
                    for restaurant_sales in city.values():
                        total_sales += restaurant_sales
                total_sales_per_week[week] = total_sales

            print(f"Weekly sales data for all restaurants: {total_sales_per_week}")

            if hasattr(self, 'canvas'):
                self.canvas.get_tk_widget().destroy()

            weeks = list(total_sales_per_week.keys())
            total_sales = list(total_sales_per_week.values())

            # Plotting the new graph
            fig, ax = plt.subplots(figsize=(5, 4), dpi=50)
            ax.clear()  # Clear previous plot
            ax.plot(weeks, total_sales, label="Total Sales of All Restaurants")
            ax.set(xlabel='Week Starting', ylabel='Sales (£)', title='Weekly Sales Data - All Restaurants')
            ax.grid()
            plt.xticks(rotation=45)
            plt.tight_layout()

            self.canvas = FigureCanvasTkAgg(fig, master=self.contentFrame)  
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        elif selected:  # Check if something else is selected
            selected_city, selected_restaurant = selected.split(' - ')
            print(f"Selected: {selected_city}, {selected_restaurant}")  

            weekly_sales_data = groupSalesByWeek(salesData)

            total_sales_per_week = {}
            for week, cities_data in weekly_sales_data.items():
                if selected_city in cities_data:
                    total_sales_per_week[week] = cities_data[selected_city].get(selected_restaurant, 0)

            print(f"Weekly sales data: {total_sales_per_week}")

            if hasattr(self, 'canvas'):
                self.canvas.get_tk_widget().destroy()

            weeks = list(total_sales_per_week.keys())
            total_sales = list(total_sales_per_week.values())

            # Plotting the new graph
            fig, ax = plt.subplots(figsize=(5, 4), dpi=50)
            ax.clear()  # Clear previous plot
            ax.plot(weeks, total_sales, label=f"Sales of {selected}")
            ax.set(xlabel='Week Starting', ylabel='Sales (£)', title=f'Weekly Sales Data - {selected}')
            ax.grid()
            plt.xticks(rotation=45)
            plt.tight_layout()


            self.canvas = FigureCanvasTkAgg(fig, master=self.contentFrame)  
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def showStaffReports(self):
        self.clearContent()
        staffLabel = tk.Label(self.contentFrame, text="Staff Reports", font=('Arial', 20))
        staffLabel.pack(pady=20)

        # Dropdown for employee selection
        self.selected_employee = tk.StringVar()
        emplyeeOptions = list(staffData.keys())  # List of employee names
        employeeDropdown = ttk.Combobox(self.contentFrame, textvariable=self.selected_employee, values=emplyeeOptions)
        employeeDropdown.current(0)  # Default selection is the first option
        employeeDropdown.pack(pady=10)
        employeeDropdown.bind("<<ComboboxSelected>>", self.updateStaffReport)  # Bind selection change event

        # Label to display total sales
        self.totalSalesLabel = tk.Label(self.contentFrame, text="", font=('Arial', 16))
        self.totalSalesLabel.pack(pady=10)

        # Initial update for the first employee
        self.updateStaffReport()

    def updateStaffReport(self, event=None):
        selectedEmployees = self.selected_employee.get()
        emplyeeSales = staffData[selectedEmployees]

        # Calculate metrics
        totalSales = sum(emplyeeSales)
        numberOfOrders = len(emplyeeSales)
        averageOrderPrice = totalSales / numberOfOrders 

        # Update the display label
        displayText = (f"Total Sales for {selectedEmployees}: £{totalSales}\n"
                        f"Number of Orders: {numberOfOrders}\n"
                        f"Average Order Price: £{averageOrderPrice:.2f}")
        self.totalSalesLabel.config(text=displayText)



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
