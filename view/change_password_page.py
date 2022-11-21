import tkinter as tk
from tkinter import *

class Change_Password_Page(tk.Frame):
    
    def __init__(self, parent, controller,win,db):
        self.db=db
        self.win=win
        tk.Frame.__init__(self, parent,bg ="#ABCDEF")
        self.controller=controller
        self.win.geometry("600x500")
        self.confirm_password=tk.StringVar()
        self.new_password=tk.StringVar()

        #page title
        self.page_label=tk.Label(self,text="Cambia password",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.page_label.place(x=250,y=20)

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\     """,command=lambda : self._clean(),bg="#D2D2D2")
        self.back_button.place(x=0,y=10)

        #new password
        self.new_password_label=tk.Label(self,text="Nuova password",font=("Helvetica",10),fg="#000000")
        self.new_password_label.place(x=200,y=200)
        self.new_password_input = tk.Entry(self,textvariable=self.new_password)
        self.new_password_input.place(x=350,y=200)
        self.new_password_label=tk.Label(self,text="Conferma password",font=("Helvetica",10),fg="#000000")
        self.new_password_label.place(x=200,y=300)
        self.confirm_password_input = tk.Entry(self,textvariable=self.confirm_password)
        self.confirm_password_input.place(x=350,y=300)


        #success button
        self.confirm_button=tk.Button(self,text="Conferma",command=lambda : self.db.change_password(self.db.id,self.new_password.get(),self.confirm_password.get()),fg="#000000",bg="#D2D2D2")
        self.confirm_button.place(x=250,y=400)
    
    def _clean(self):
        self.new_password_input.delete(0,tk.END)
        self.confirm_password_input.delete(0,tk.END)
        self.controller.show_frame("User_Page")
