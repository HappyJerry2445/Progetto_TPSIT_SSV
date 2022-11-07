import mysql.connector

class Database_access:
    def sign_up(lst=[]):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ssn"
        ) 
        mycursor = mydb.cursor()
        print("FUNZIONA")
        query=f"""INSERT INTO PATIENTS (FIRSTNAME,LASTNAME,CITYBORN,GENDER,CF,PASSWORD )VALUES(%s,%s,%s,%s,%s,%s )"""
        mycursor.execute(query,lst)
        result=mycursor.fetchall()
        print(query)
        print(result)
        mydb.commit()
        
