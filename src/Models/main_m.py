from .auth_m import Auth
from .admin_m import Admin



class Model:
    def __init__(self):
        self.auth = Auth()
        self.admin = Admin()
