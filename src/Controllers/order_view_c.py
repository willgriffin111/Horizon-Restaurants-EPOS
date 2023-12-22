
from Models.main_m import Model
from Views.main_v import View

class OrderViewController:
    
    
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["orderView"]
        self._bind()
    
    def _bind(self) -> None:
        #Binds controller functions with respective buttons in the view
        self.frame.homeButton.config(command=self.home)

        
    def home(self) -> None:
        self.view.switch("home")