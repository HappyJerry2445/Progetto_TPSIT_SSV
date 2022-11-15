import tkinter as tk
from tkinter import *

class Delete_Account_Page(tk.Frame):
    
    def __init__(self, parent, controller,win,db):
        self.db=db
        self.win=win
        tk.Frame.__init__(self, parent,bg ="#ABCDEF")
        self.controller=controller
        self.win.geometry("600x500")
        self.password=tk.StringVar()

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\   """,command=lambda : controller.show_frame("User_Page"),bg="#D2D2D2")
        self.back_button.place(x=0,y=10)

        #page title
        self.page_label=tk.Label(self,text="Elimina Account",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.page_label.place(x=250,y=20)

        #password input
        self.password_label=tk.Label(self,text="Password",font=("Helvetica",15),fg="#000000")
        self.password_label.place(x=250,y=150)
        self.password_input=tk.Entry(self,textvariable=self.password)
        self.password_input.place(x=250,y=225)

        #add confirm delete button
        self.confirm_delete_button=tk.Button(self,text="Elimina account",command=lambda:db.delete_user(db.id,self.password.get()),fg="#FF0000",bg="#D2D2D2")
        self.confirm_delete_button.place(x=250,y=300)