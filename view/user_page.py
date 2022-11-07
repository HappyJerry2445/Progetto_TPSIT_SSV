import tkinter as tk
from tkinter import *

class User_Page(tk.Frame):
    
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.win.geometry("600x500")

        #page title
        self.page_label=tk.Label(self,text="User",font=("Helvetica",15))
        self.page_label.place(x=270,y=20)

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\   """,command=lambda : controller.show_frame("Login_Page"))
        self.back_button.place(x=0,y=10)

        #user illness list
        self.user_illness_button=tk.Button(self,text="Patologie utente",command=lambda : controller.show_frame("Illness_User_Page"))
        self.user_illness_button.place(x=250,y=100)

        #add illness
        self.add_illnes_button=tk.Button(self,text="Aggiungi patologia",command=lambda : controller.show_frame("Add_Illness_Page"))
        self.add_illnes_button.place(x=250,y=140)

        #general illness list
        self.general_illnes_button=tk.Button(self,text="Lista patologie",command=lambda : controller.show_frame("General_Illness_Page"))
        self.general_illnes_button.place(x=250,y=180)

        #change password
        self.change_password_button=tk.Button(self,text="Cambia password",command=lambda : controller.show_frame("Change_Password_Page"))
        self.change_password_button.place(x=250,y=220)
        
        #delete account
        self.delete_account_button=tk.Button(self,text="Elimina account",command=lambda : controller.show_frame("Delete_Account_Page"))
        self.delete_account_button.place(x=250,y=260)