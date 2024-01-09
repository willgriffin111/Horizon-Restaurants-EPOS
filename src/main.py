'''
*    Title: How To Organize Multi-frame TKinter Application With MVC Pattern
*    Author: Nazmul Ahsan
*    Date: Jan 6, 2023
*    Code version: 1.0
*    Availability: https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
*
'''


from Models.main_m import Model
from Views.main_v import View
from Controllers.main_c import Controller



def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()

if __name__ == "__main__":
    main()

