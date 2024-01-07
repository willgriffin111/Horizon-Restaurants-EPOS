from fpdf import FPDF
import matplotlib.pyplot as plt
'''
Author Jevhan Seechurn,
Date: 06/01/2024 
Version: 1.0
'''

class PDFProfit(FPDF):
    def header(self):
        # Title
        self.set_font('Helvetica', 'BU', 20)
        self.cell(30, 20, 'Horizon Restaurant',ln=True)

        
    def subHeader(self,title,date,name):
        # Report Sub header 
        self.set_font('Helvetica', '', 16)
        self.cell(30, 10, title,ln=True)

        # Date issued
        self.set_font('Helvetica', '', 12)
        self.cell(30,10,date,ln=True)

        # Name issued
        self.set_font('Helvetica', '', 12)
        self.cell(30,10,name,ln=True)

    def profit_title(self):
        self.set_font('Helvetica', '', 14)
        self.cell(30,20,'Staff Performance: Profit record',ln=True)

    def profit_record(self, table_data,RestName):

            self.set_font('Helvetica', '', 12)
            self.cell(76,20,RestName,ln=True, align='C')

            self.table_data = [("Staff ID", "Full name", "Position", "Total")]
            for data in table_data:
                self.table_data.append(data)

            # Table - Staff Profit record 
            self.set_font('Helvetica', '', 10)
            with self.table(width=150, col_widths=(15, 25, 20, 15),align='C',text_align="CENTER",) as table:
                for data_row in self.table_data:
                    row = table.row()
                    for datum in data_row:
                        row.cell(datum)

    def order_title(self):
        self.set_font('Helvetica', '', 14)
        self.cell(30,20,'Staff Performance: Order record',ln=True)


    def order_record(self, table_data, RestName):
        self.set_font('Helvetica', '', 12)
        self.cell(76,20,RestName,ln=True, align='C')

            # Dummy values for the table 
        self.table_data = [("Staff ID", "Full name", "Position", "Total Orders")]
        for data in table_data:
            self.table_data.append(data)

        # Table - Staff Order record 
        self.set_font('Helvetica', '', 10)
        with self.table(width=150, col_widths=(15, 25, 20, 15),align='C',text_align="CENTER",) as table:
            for data_row in self.table_data:
                row = table.row()
                for datum in data_row:
                    row.cell(str(datum))


    def create_line_graph(self,dates,total):
            # Data for the line graph

            # Create the line graph using matplotlib
            plt.figure(figsize=(6, 4))  # Set figure size
            plt.plot(dates, total, marker='o')  # Plot the data
            plt.xlabel('Date')  # X-axis label
            plt.ylabel('Sales (£)')  # Y-axis label
            plt.title('Sales Report: Overall')  # Title of the graph
            plt.grid(True)  # Enable grid
            plt.tight_layout()  # Adjust layout

            # Save the graph as an image (PNG)
            plt.savefig('preformace_graph.png', format='png', dpi=300)
            plt.close()  # Close the plot to avoid displaying it

    def add_line_graph_to_pdf(self,dates,total):
        self.create_line_graph(dates,total)
        self.add_page()  # Add a new page for the graph
        self.image('Preformace_graph.png', x=10, y=180, w=180, h=100)  # Insert the graph into the new page
        # Page footer goes here if needed

    def sales_record(self,dates,total):

            self.set_font('Helvetica', '', 12)
            self.cell(76,20,'Restaurant: London',ln=True, align='C')

            self.table_data = [("Date","Sales")]  # Append this before inserting data
            
            for i in range(len(dates)):
                self.table_data.append((str(dates[i]),str(total[i])))
                 

            # Table - Staff Profit record 
            self.set_font('Helvetica', '', 10)
            with self.table(width=152, col_widths=(20,15),align='C',text_align="CENTER",) as table:
                for data_row in self.table_data:
                    row = table.row()
                    for datum in data_row:
                        row.cell(datum)

    


    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
    
