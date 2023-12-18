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

