'''
Author: Alex Rogers
Date: 22/12/2023
Version: 1.1
'''

from typing import TypedDict, Union
from .base_m import ObservableModel
from database import dbfunc
from passlib.hash import sha256_crypt
from tkinter import messagebox
import re




class Account(ObservableModel):
    
    def updateName(self,newName,currentuser):
        if (len(newName) > 0):
            currentuser.updateName(newName)
            self.trigger_event("update_view")
            messagebox.showinfo("Sucsess", "Name has been updated.")
        else:
            messagebox.showerror("Error", "Please enter a name.") 
            return
        
    def updatePassword(self,newPassword,rePassword,currentuser):
        if(str(newPassword) == str(rePassword)):
            newPassword = sha256_crypt.hash(newPassword)
            currentuser.updatePassword(newPassword)
            messagebox.showinfo("Sucsess", "Password has been updated.")
        else:
            messagebox.showerror("Error", "Password's are not the same.")
            
        
            
        
    
    
                
    
                
    
        