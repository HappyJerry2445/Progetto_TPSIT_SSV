import tkinter as tk
from tkinter import *
from general_illness_page import *

class User_Page(tk.Frame):
    
    def __init__(self, parent, controller,win,db):
        self.db=db
        self.win=win
        tk.Frame.__init__(self, parent,bg ="#ABCDEF")
        self.controller=controller
        self.win.geometry("600x500")

        #page title
        self.page_label=tk.Label(self,text="User",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.page_label.place(x=250,y=20)

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\   """,command=lambda : controller.show_frame("Login_Page"))
        self.back_button.place(x=0,y=10)

        #user illness list
        self.user_illness_button=tk.Button(self,text="Patologie utente",command=lambda : controller.show_frame("Illness_User_Page"),fg="#000000",bg="#D2D2D2")
        self.user_illness_button.place(x=250,y=150)

        #add illness
        self.add_illnes_button=tk.Button(self,text="Aggiungi patologia",command=lambda : controller.show_frame("Add_Illness_Page"),fg="#000000",bg="#D2D2D2")
        self.add_illnes_button.place(x=250,y=200)

        #general illness list
        self.general_illnes_button=tk.Button(self,text="Lista patologie",command=lambda : controller.show_frame("General_Illness_Page"),fg="#000000",bg="#D2D2D2")
        self.general_illnes_button.place(x=250,y=250)

        #change password
        self.change_password_button=tk.Button(self,text="Cambia password",command=lambda : controller.show_frame("Change_Password_Page"),fg="#000000",bg="#D2D2D2")
        self.change_password_button.place(x=250,y=300)
        
        #delete account
        self.delete_account_button=tk.Button(self,text="Elimina account",command=lambda : controller.show_frame("Delete_Account_Page"),fg="#000000",bg="#D2D2D2")
        self.delete_account_button.place(x=250,y=350)

