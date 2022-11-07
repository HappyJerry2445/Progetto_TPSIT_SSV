import tkinter as tk
from tkinter import *

class Change_Password_Page(tk.Frame):
    
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.win.geometry("600x500")

        #page title
        self.page_label=tk.Label(self,text="Cambia password",font=("Helvetica",15))
        self.page_label.place(x=280,y=20)

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\     """,command=lambda : controller.show_frame("User_Page"))
        self.back_button.place(x=0,y=10)

        #old password
        self.old_password_label=tk.Label(self,text="Password attuale",font=("Helvetica",10))
        self.old_password_label.place(x=195,y=100)
        self.old_password_input = tk.Entry(self)
        self.old_password_input.place(x=300,y=100)


        #new password
        self.new_password_label=tk.Label(self,text="Nuova password",font=("Helvetica",10))
        self.new_password_label.place(x=200,y=200)
        self.new_password_input = tk.Entry(self)
        self.new_password_input.place(x=300,y=200)

        #confirm password
        self.confirm_password_label=tk.Label(self,text="Conferma password",font=("Helvetica",10))
        self.confirm_password_label.place(x=180,y=300)
        self.confirm_password_input= tk.Entry(self)
        self.confirm_password_input.place(x=300,y=300)

        #success button
        self.confirm_button=tk.Button(self,text="Conferma")
        self.confirm_button.place(x=300,y=400)
