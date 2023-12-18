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
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
