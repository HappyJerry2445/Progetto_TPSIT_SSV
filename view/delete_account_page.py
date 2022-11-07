import tkinter as tk
from tkinter import *

class Delete_Account_Page(tk.Frame):
    
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.win.geometry("600x500")

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\   """,command=lambda : controller.show_frame("User_Page"))
        self.back_button.place(x=0,y=10)

        #page title
        self.page_label=tk.Label(self,text="Elimina Account",font=("Helvetica",15))
        self.page_label.place(x=250,y=20)

        #password input
        self.password_label=tk.Label(self,text="Password",font=("Helvetica",15))
        self.password_label.place(x=250,y=100)
        self.password_input=tk.Entry(self)
        self.password_input.place(x=250,y=130)

        #add confirm delete button
        self.confirm_delete_button=tk.Button(self,text="Elimina account")
        self.confirm_delete_button.place(x=250,y=200)