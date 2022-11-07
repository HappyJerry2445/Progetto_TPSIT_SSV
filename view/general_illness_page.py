import tkinter as tk
from tkinter import *
import pandas as pd


class General_Illness_Page(tk.Frame):
    
    def __init__(self, parent, controller,win):
        self.win=win
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.win.geometry("600x500")

        #page title
        self.page_label=tk.Label(self,text="Lista Patologie",font=("Helvetica",15))
        self.page_label.place(x=270,y=20)

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\  """,command=lambda : controller.show_frame("User_Page"))
        self.back_button.place(x=0,y=10)
        
        #illness list
        self.illness_label=tk.Label(self,text="Lista Patologie Utenti",font=("Helvetica",15))
        self.illness_label.place(x=30,y=100)
        data=pd.read_csv("C:/Users/andre/OneDrive/Desktop/progetto tpsit parte 2/csv_malattie.csv")
        self.illness_df=pd.DataFrame(data)
        self.illness_list=Listbox(self,yscrollcommand=Scrollbar.set,height=10,width=50)
        self.illness_list.grid(sticky=tk.N)
        for row in range(len(self.illness_df)):
            self.illness_list.insert(END,self.illness_df.loc[row].at["lista malattie"])
        self.illness_list.place(x=30,y=150)