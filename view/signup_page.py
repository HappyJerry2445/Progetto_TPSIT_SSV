import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from datetime import *
import pandas as pd
from database_access import Database_access

class Signup_Page(tk.Frame):
    
    def __init__(self, parent, controller,win,db):

        #variables
        self.db=db
        self.name=tk.StringVar()
        self.surname=tk.StringVar()
        self.gender=tk.IntVar()
        self.birth_date=DateEntry
        self.birth=tk.StringVar()
        self.password=tk.StringVar()

        #frame
        self.win=win
        tk.Frame.__init__(self, parent,bg ="#ABCDEF")
        self.controller=controller
        self.win.geometry("600x500")

        #page title
        self.page_label=tk.Label(self,text="Registrazione",font=("Helvetica",15),fg="#000000",bg="#ABCDEF")
        self.page_label.place(x=250,y=20)

        #back button
        self.back_button=tk.Button(self,text="""
  __    
 / /___ 
< <(___)
 \_\    """,command=lambda : controller.show_frame("Login_Page"),bg="#D2D2D2")
        self.back_button.place(x=0,y=10)
        
        #name and surname text box
        self.name_label=tk.Label(self,text="Nome",font=("Helvetica",10),fg="#000000")
        self.name_label.place(x=200,y=100)
        self.name_input = tk.Entry(self,textvariable=self.name)
        self.name_input.place(x=250,y=100)
        self.surname_label=tk.Label(self,text="Cognome",font=("Helvetica",10),fg="#000000")
        self.surname_label.place(x=200,y=150)
        self.surname_input = tk.Entry(self,textvariable=self.surname)
        self.surname_input.place(x=275,y=150)

        #gender radio button
        self.gender_label=tk.Label(self,text="Genere",font=("Helvetica",10),fg="#000000")
        self.gender_label.place(x=200,y=200)
        self.male_button=Radiobutton(self ,text="Maschio",variable=self.gender,value=1,fg="#000000",bg="#D2D2D2")
        self.male_button.place(x=250,y=200)
        self.female_button=Radiobutton(self ,text="Femmina",variable=self.gender,value=0,fg="#000000",bg="#D2D2D2")
        self.female_button.place(x=325,y=200)

        #birth date picker
        self.birth_date_label=tk.Label(self,text="Data di nascita",font=("Helvetica",10),fg="#000000")
        self.birth_date_label.place(x=200,y=250)
        self.birth_date=DateEntry(self)
        self.birth_date.place(x=350,y=250)
        self.birth=self.birth_date.get_date().strftime("%Y-%m-%d")
        print(self.birth)

        #birth place picker
        self.born_place_label=tk.Label(self,text="Comune di nascita",font=("Helvetica",10))
        self.born_place_label.place(x=150,y=300)
        data=pd.read_csv("C:/Users/andre/OneDrive/Desktop/progetto tpsit parte 2/elencoComuniAttuali_20221011.csv")
        self.comuni_df=pd.DataFrame(data)
        self.born_place=Listbox(self,yscrollcommand=Scrollbar(self).set,height=5,width=25)
        self.born_place.grid(sticky=tk.N)
        for row in range(len(self.comuni_df)):
            self.born_place.insert(END,self.comuni_df.loc[row].at["Denominazione"])
        self.born_place.place(x=300,y=300)
        

        #password
        self.password_label=tk.Label(self,text="Password",font=("Helvetica",10))
        self.password_label.place(x=200,y=400)
        self.password_input=tk.Entry(self,textvariable=self.password)
        self.password_input.place(x=300,y=400)

        #signup button
        self.signup_button= tk.Button(self,text="Registrati",command=lambda : self.Signup(),bg="#D2D2D2")
        self.signup_button.place(x=250,y=450)


    #transform data to create a json format
    def Sign_Up_Format(self):
        self.user_name=self.name.get()
        self.user_surname=self.surname.get()
        self.user_password=self.password.get()
        print(self.user_password)
        r=self.born_place.curselection().__str__()
        r=r.replace("(", " ").replace(","," ").replace(")"," ").strip()
        self.user_birth_place= self.born_place.get(0,tk.END)
        print(f"curse selection={self.born_place.curselection()}")
        #self.cf=self.code(self.user_surname,self.user_name,self.gender,self.user_birth_place)



    #lista prova
    def Signup(self):
        self.Sign_Up_Format()
        l=[]
        name=self.name.get()
        surname=self.surname.get()
        l.append(name)
        l.append(surname)
        r=self.born_place.curselection().__str__()
        r=r.replace("(", " ").replace(","," ").replace(")"," ").strip()
        r=int(r)
        print(f"r= {r}")
        birth_date=self.birth_date.get_date().strftime("%Y-%m-%d")
        l.append(r+1)
        gender=self.gender.get()
        cf=self.code(surname,name,birth_date,gender,self.born_place.get(r))
        l.append(gender)
        l.append(cf)
        password=self.password.get()
        l.append(password)
        print(l)
        Database_access.sign_up(l)

    #codes the name and the surname
    def codeNames(self,s='',isFname=False):
        s=str(s)
        s=s.upper()
        code=''.join([
            c
                for c in s
                            if
                                ord(c) in range(ord('B'),ord('Z')+1) and
                                c not in 'AEIOU'
                ])
        return f"{code[0]}{code[2:4]}" if len(code)>3 and isFname else f"{code}{''.join([c for c in s if c in 'AEIOU'])}XXX"[0:3]
    
    #codes the date
    def codeDate(self,bday = '2000-01-01', isMale = 1):
        return f"{bday[2:4]}{'ABCDEHLMPRST'[int(bday[5:7])-1]}{bday[8:] if isMale==1 else 40 +int(bday[8:])}"
    
    #codes the place
    def codePlace(self,city = ''):
        city=str(city)
        for c in open('C:/Users/andre/OneDrive/Desktop/progetto tpsit parte 2/elencoComuniAttuali_20221011.csv').read().split('\n'):
            if c.split(',')[1] == city.upper():
                return c.split(',')[0]
        return 'Z999'
    
    #gives the check code
    def codeCheck(self,code):
        check=[
                [
                    1,	0,	5,	7,	9,	13,	15,	17,	19,	21,
                    2,	4,	18,	20,	11,	3,	6,	8,	12,	14,
			        16,	10,	22,	25,	24,	23
                ],
                range(0,26)
                ]
        ck=0
        for i in range(0,len(code)):
            ck += check[i%2][ord(code[i])-(65 if ord(code[i])>= 65 else 48)]
        return chr(65 + ck%26)

    #gives the full c/f
    def code(self,lastname = '', firstname = '', bday = '', isMale = 1, city = ''):
        p_code = f"{self.codeNames(lastname)}{self.codeNames(firstname, True)}{self.codeDate(bday, isMale)}{self.codePlace(city)}"
        return f"{p_code}{self.codeCheck(p_code)}"

    