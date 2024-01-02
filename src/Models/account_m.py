'''
Author: Alex Rogers
Date: 22/12/2023
Version: 1.1
'''

from typing import TypedDict, Union
from .base_m import ObservableModel
from database import dbfunc
from passlib.hash import sha256_crypt
import re




class Account(ObservableModel):
    
    def updateName(self,newName,currentuser):
        if (len(newName) > 0):
            currentuser.updateName(newName)
            self.trigger_event("update_view")
        else:
            print("ERROR: Please enter a name")
            return
        
    def updatePassword(self,newPassword,rePassword,currentuser):
        if(str(newPassword) == str(rePassword)):
            newPassword = sha256_crypt.hash(newPassword)
            currentuser.updatePassword(newPassword)
        else:
            print("ERROR: Password is not the same")
        
            
        
    
    
                
    
                
    
        