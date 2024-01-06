from fpdf import FPDF
import matplotlib.pyplot as plt
'''
Author Jevhan Seechurn,
Date: 06/01/2024 
Version: 1.0
'''

class PDF(FPDF):
    def header(self):
        # Title
        self.set_font('Helvetica', 'BU', 20)
        self.cell(30, 20, 'Horizon Restaurant',ln=True)

        # Report Sub header 
        self.set_font('Helvetica', '', 16)
        self.cell(30, 10, 'Directors Report',ln=True)

        # Date issued
        self.set_font('Helvetica', '', 12)
        self.cell(30,10,'Date: 12/01/2021',ln=True)

        # Date issued
        self.set_font('Helvetica', '', 12)
        self.cell(30,10,'Representative: Alex Rogers',ln=True)

    def profit_title(self):
        self.set_font('Helvetica', '', 14)
        self.cell(30,20,'Staff Performance: Profit record',ln=True)

    def profit_record(self, table_data):
        for i in range(3):

            self.set_font('Helvetica', '', 12)
            self.cell(76,20,'Restaurant: London',ln=True, align='C')

            self.table_data = [("Restaurant","Staff ID", "Full name", "Position", "Total")]
            for data in table_data:
                self.table_data.append(data)

            # Table - Staff Profit record 
            self.set_font('Helvetica', '', 10)
            with pdf.table(width=150, col_widths=(20,15, 25, 20, 15),align='C',text_align="CENTER",) as table:
                for data_row in self.table_data:
                    row = table.row()
                    for datum in data_row:
                        row.cell(datum)

    def order_title(self):
        self.set_font('Helvetica', '', 14)
        self.cell(30,20,'Staff Performance: Order record',ln=True)


    def order_record(self, table_data):
        for j in range(3):

            self.set_font('Helvetica', '', 12)
            self.cell(76,20,'Restaurant: London',ln=True, align='C')

             # Dummy values for the table 
            self.table_data = [("Restaurant","Staff ID", "Full name", "Position", "Total Orders")]
            for data in table_data:
                self.table_data.append(data)

            # Table - Staff Order record 
            self.set_font('Helvetica', '', 10)
            with pdf.table(width=150, col_widths=(20,15, 25, 20, 15),align='C',text_align="CENTER",) as table:
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

pdf = PDF()
table_data_profit = [("1","1", "James Smith", "Front", "£100"),
                 ("1","2", "Carlos Ramos", "Bar", "£100"),
                 ("1","3", "Cid Banks", "Front", "£100"),
                 ("1","4", "Stacey Cimon", "Front", "£100"),
                 ("1","4", "Jeremy Cimon", "Front", "£100")]
table_data = [
                 ("1","1", "James Smith", "Front", "30"),
                 ("1","2", "Carlos Ramos", "Bar", "30"),
                 ("1","3", "Cid Banks", "Front", "30"),
                 ("1","4", "Stacey Cimon", "Front", "30"),
                 ("1","4", "Jeremy Cimon", "Front", "30")]
pdf.add_page()
pdf.profit_title()
pdf.profit_record(table_data_profit)
pdf.order_title()
pdf.order_record(table_data)
pdf.output('Director report.pdf', 'F')