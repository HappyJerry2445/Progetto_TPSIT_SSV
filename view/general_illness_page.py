import tkinter as tk
from tkinter import *
import pandas as pd


class General_Illness_Page(tk.Frame):
    
    def __init__(self, parent, controller,win,db):
        self.win=win
        tk.Frame.__init__(self, parent,bg ="#ABCDEF")
        self.controller=controller
        self.win.geometry("600x500")

        #page title
        self.page_label=tk.Label(self,text="Lista Patologie",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.page_label.place(x=250,y=20)

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\  """,command=lambda : controller.show_frame("User_Page"),bg="#D2D2D2")
        self.back_button.place(x=0,y=10)
        
        #illness list
        self.illness_label=tk.Label(self,text="Lista Patologie Utenti",font=("Helvetica",15),fg="#000000")
        self.illness_label.place(x=125,y=150)
        self.illness_list=Listbox(self,yscrollcommand=Scrollbar.set,height=10,width=50)
        self.illness_list.grid(sticky=tk.N)
        self.ill=db.illness_list()
        for row in self.ill:
            self.illness_list.insert(END,row)
        self.illness_list.place(x=125,y=200)