from tkinter import Tk


class Root(Tk):
    def __init__(self):
        super().__init__()

        startWidth = 800
        # min_width = 400
        startHeight = 600
        # min_height = 250

        self.geometry(f"{startWidth}x{startHeight}")
        # self.minsize(width=min_width, height=min_height)
        self.title("Horizon Restaurant")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
