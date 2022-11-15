import tkinter as tk
from tkinter import *


class Illness_User_Page(tk.Frame):
    
    def __init__(self, parent, controller,win,db):
        self.db=db
        self.win=win
        tk.Frame.__init__(self, parent,bg ="#ABCDEF")
        self.controller=controller
        self.win.geometry("600x500")

        #back button
        self.back_button=tk.Button(self,text="""  
  __    
 / /___ 
< <(___)
 \_\  """,command=lambda : controller.show_frame("User_Page"),fg="#000000",bg="#D2D2D2")
        self.back_button.place(x=0,y=10)
        
        #page title
        self.page_label=tk.Label(self,text="Lista Patologie",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.page_label.place(x=250,y=20)

        #illness list
        self.illness_label=tk.Label(self,text="Lista Patologie Utente",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.illness_label.place(x=125,y=150)
        self.illness_list=Listbox(self,yscrollcommand=Scrollbar.set,height=10,width=50)
        self.illness_list.grid(sticky=tk.N)
        
        self.illness_list.place(x=125,y=200)

        self.illness_button=tk.Button(self,text="Mostra malattie",command=lambda : user_illness_show(self),fg="#000000",bg="#D2D2D2")
        self.illness_button.place(x=250,y=400)
        def user_illness_show(self):
            print(f"IL RISULTATO DELLE MALATTIE={self.db.show_illness(self.db.id)}")
            l=self.db.show_illness(self.db.id)
            for row in l:
                self.illness_list.insert(END,row)