import tkinter as tk
from tkinter import *
from database_access import Database_access

class Add_Illness_Page(tk.Frame):
    def __init__(self, parent, controller,win,db):
        self.db=db
        self.win=win
        tk.Frame.__init__(self, parent,bg ="#ABCDEF")
        self.controller=controller
        self.win.geometry("600x500")

        self.illness_name=tk.StringVar()
        self.illness_description=tk.StringVar()

        #page title
        self.page_label=tk.Label(self,text="Aggiungi patologia",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.page_label.place(x=250,y=20)

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\    """,command=lambda : self._clean(),bg="#D2D2D2")
        self.back_button.place(x=0,y=10)
        
        #illness input
        self.illness_label=tk.Label(self,text="Nome patologia",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.illness_label.place(x=200,y=150)
        self.illness_input=tk.Entry(self,textvariable=self.illness_name)
        self.illness_input.place(x=350,y=150)
        self.description_illness_label=tk.Label(self,text="Descrizione patologia",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.description_illness_label.place(x=150,y=250)
        self.illness_description_input=tk.Entry(self,textvariable=self.illness_description)
        self.illness_description_input.place(x=350,y=250)

        #add illness button
        self.add_illness_button=tk.Button(self,command=lambda : self.db.illness_control(self.illness_name.get(),self.db.id,self.illness_description.get()),text="Aggiungi patologia",fg="#000000",bg="#D2D2D2")
        self.add_illness_button.place(x=250,y=350) 
        
    def _clean(self):
            self.illness_input.delete(0,tk.END)
            self.illness_description_input.delete(0,tk.END)
            self.controller.show_frame("User_Page")
        
