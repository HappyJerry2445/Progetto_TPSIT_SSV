import tkinter as tk
from tkinter import *
from login_page import Login_Page
from signup_page import Signup_Page
from user_page import User_Page
from change_password_page import Change_Password_Page
from illness_user_page import Illness_User_Page
from general_illness_page import General_Illness_Page
from add_illness_page import Add_Illness_Page
from delete_account_page import Delete_Account_Page
from database_access import Database_access


class tkinter_App(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("SSN Nazionale")
        self.resizable(False,False)
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        db=Database_access()
        self.frames={}
        for F in (Login_Page,Signup_Page,User_Page,Change_Password_Page,Illness_User_Page,General_Illness_Page,Add_Illness_Page,Delete_Account_Page):
            page_name=F.__name__
            frame=F(parent=container,controller=self, win=self,db=db)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame("Login_Page")
    
    
    
    def show_frame(self,cont):
        print(cont)
        frame=self.frames[cont]
        frame.tkraise()




