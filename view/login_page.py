import tkinter as tk
from database_access import Database_access


class Login_Page(tk.Frame):
    def __init__(self,parent,controller,win,db):
        self.db=db
        
        #geometry
        self.win=win
        tk.Frame.__init__(self,parent,bg ="#ABCDEF")
        self.controller=controller
        self.win.geometry("600x500")

        #variables
        self.cf=tk.StringVar()
        self.password=tk.StringVar()

        self.page_label = tk.Label(self,text="Login",font=("Helvetica",15),fg="#000000")
        self.page_label.place(x=250,y=20)
        self.cf_label=tk.Label(self,text="C/F",font=("Helvetica",10),fg="#000000")
        self.cf_label.place(x=200,y=150)
        self.cf_input = tk.Entry(self,textvariable=self.cf)
        self.cf_input.place(x=250,y=150)
        self.password_label=tk.Label(self,text="Password",font=("Helvetica",10),fg="#000000")
        self.password_label.place(x=175,y=200)
        self.password_input = tk.Entry(self,textvariable=self.password)
        self.password_input.place(x=250,y=200)
        self.sign_in_button = tk.Button(self,text="Accedi",command=lambda : self.login_page(),fg="#000000",bg="#D2D2D2")        
        self.sign_in_button.place(x=150,y=350)
        self.sign_up_button = tk.Button(self,text="Registrati",command=lambda : controller.show_frame("Signup_Page"),fg="#000000",bg="#D2D2D2")
        self.sign_up_button.place(x=375,y=350)



    #new page method
    def New_Page(self):
        self.user_cf=self.cf.get()
        self.user_password=self.password.get()
        if self.Login_Method(self.user_cf,self.user_password):
            self.controllers.show_frame("User_Page")
        else:
            self.error_popup()


    def login_page(self):
        self.user_cf=self.cf.get()
        self.user_password=self.password.get()
        self.db.id=Database_access.user_in_list(self.user_cf,self.user_password).__str__()
        self.db.id=self.db.id.replace("{"," ").replace("}"," ").strip()
        self.db.id=int(self.db.id)
        print(self.db.id)
        if self.db.id > 0:
            self.controller.show_frame("User_Page")
        else:
            return self.pop_alert()




    def pop_alert(self):
        top= tk.Toplevel(self.win)
        top.geometry("400x200")
        top.title("errore")
        tk.Label(top,text= "Utente non presente!", font=('Helvetica',10)).place(x=150,y=75)
    
