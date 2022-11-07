import tkinter as tk
from tkinter import *

class Add_Illness_Page(tk.Frame):
    
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.win.geometry("600x500")

        #page title
        self.page_label=tk.Label(self,text="Aggiungi patologia",font=("Helvetica",15))
        self.page_label.place(x=270,y=20)

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\    """,command=lambda : controller.show_frame("User_Page"))
        self.back_button.place(x=0,y=10)
        
        #illness input
        self.illness_label=tk.Label(self,text="Nome patologia",font=("Helvetica",15))
        self.illness_label.place(x=250,y=100)
        self.illness_input=tk.Entry(self)
        self.illness_input.place(x=300,y=130)

        #add illness button
        self.add_illness_button=tk.Button(self,text="Aggiungi patologia")
        self.add_illness_button.place(x=300,y=200)

        
