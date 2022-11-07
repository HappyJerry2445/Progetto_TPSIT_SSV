import tkinter as tk
import json

class Login_Page(tk.Frame):
    def __init__(self,parent,controller,win):
        
        #geometry
        self.win=win
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.win.geometry("600x500")

        #variables
        self.cf=tk.StringVar()
        self.password=tk.StringVar()

        self.page_label = tk.Label(self,text="Login",font=("Helvetica",15))
        self.page_label.place(x=280,y=20)
        self.cf_label=tk.Label(self,text="C/F",font=("Helvetica",10))
        self.cf_label.place(x=235,y=150)
        self.cf_input = tk.Entry(self,textvariable=self.cf)
        self.cf_input.place(x=280,y=150)
        self.password_label=tk.Label(self,text="Password",font=("Helvetica",10))
        self.password_label.place(x=220,y=200)
        self.password_input = tk.Entry(self,textvariable=self.password)
        self.password_input.place(x=280,y=200)
        self.sign_in_button = tk.Button(self,text="Accedi",command=self.New_Page())        
        self.sign_in_button.place(x=210,y=350)
        self.sign_up_button = tk.Button(self,text="Registrati",command=lambda : controller.show_frame("Signup_Page"))
        self.sign_up_button.place(x=310,y=350)

    #login method
    def Login_Method(self,cf='',password=''):
        with open("C:/Users/andre/OneDrive/Desktop/progetto tpsit parte 2/Users.json", "r") as outfile:
            data=json.load(outfile)
            for u in data:
                print(u["c/f"])
                if cf.upper() == u["c/f"] and password == u["password"]:
                    return True
        return False

    #new page method
    def New_Page(self):
        self.user_cf=self.cf.get()
        self.user_password=self.password.get()
        if self.Login_Method(self.user_cf,self.user_password):
            self.controllers.show_frame("User_Page")
        else:
            self.error_popup()

    #
    def error_popup(self):
        top=tk.Toplevel(self.win)
        top.geometry("200x150")
        top.title("Not Logged")
        error_labelLabel=tk.Label(top, text= "Non hai eseguito la registrazione, utente non presente", font=("Helvetica",15)).place(x=70,y=75)
