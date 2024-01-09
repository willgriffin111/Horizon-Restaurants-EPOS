'''
*    Title: How To Organize Multi-frame TKinter Application With MVC Pattern
*    Author: Nazmul Ahsan
*    Date: Jan 6, 2023
*    Code version: 1.0
*    Availability: https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
*
'''


from tkinter import Tk


class Root(Tk):
    def __init__(self):
        super().__init__()

        start_width = 800
        min_width = 800
        start_height = 600
        min_height = 600

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title('Horizon Restaurant')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
