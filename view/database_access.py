import mysql.connector
from User import user
from Illness import illness

class Database_access:
	def __init__(self,id=0):
		self.id=id

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
	
	def illness_in_list(self,illness_name,illness_description):
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			port=3306,
			database="ssn"
		)
		mycursor = mydb.cursor()
		query=f"""
			SELECT
				*
			FROM
				illness
			WHERE
				name = "{illness_name}"
		"""
		mycursor.execute(query)
		result=mycursor.fetchall()

		if len(result) > 0:
			for illness in result:
				print(illness)
				id={illness[0]}.__str__()
				id=id.replace("{"," ").replace("}"," ").strip()
				id=int(id)
		else:
			id=-1
		print(f"IL RISULTATO DI IN LIST {id}")
		return id
					

	def add_illness(self,illness_name,illness_description):
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="ssn") 
		mycursor = mydb.cursor()
		forte=f"""{illness_name},{illness_description}"""
		query=f"INSERT INTO ILLNESS (name,description) VALUES (%s,%s)"
		mycursor.execute(query,forte.split(","))
		result=mycursor.fetchall()
		mydb.commit()
		print(query)
		print(result)

	def illness_control(self,illness_name,id_user,illness_description):
		id_illness=self.illness_in_list(illness_name,illness_description)
		print(f"illness={id_illness}")
		if id_illness>0:
			self.illness_assosiaciotion(id_user,id_illness)
		else:
			self.add_illness(illness_name,illness_description)
			id_illness=self.illness_in_list(illness_name,illness_description)
			self.illness_assosiaciotion(id_user,id_illness)


	def illness_assosiaciotion(self,id_user,id_illness):
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="ssn") 
		mycursor = mydb.cursor()
		forte=f"""{id_user},{id_illness}"""
		print(f"FORTE={forte}")
		pippo=f"""INSERT INTO PATIENTS_ILLNESS (patient_fk,illness_fk) VALUES (%s,%s)"""
		mycursor.execute(pippo,forte.split(","))
		print(forte)
		print(pippo)
		mydb.commit()

	def user_in_list(cf,psw):

		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			port=3306,
			database="ssn"
		) 
		mycursor = mydb.cursor()
		query=f"""
			SELECT
				*
			FROM
				patients
			WHERE
				cf = "{cf.strip().upper()}"
			AND
				password = "{psw.strip()}"
			ORDER BY id ASC;
		"""
		mycursor.execute(query)
		result=mycursor.fetchall()
		if len(result) > 0:
			for utente in result:
				id={utente[0]}
		else:
			id=-1
		mycursor.close()
		print(id)
		return id

	#change password
	def change_password(self,id,password):
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			port=3306,
			database="ssn"
		) 
		mycursor = mydb.cursor()
		print(f"id={id},password={password}")
		query=f"""
			UPDATE 
				PATIENTS
			SET 
				password = "{password}"
			WHERE
				id = "{id}"
			
		"""
		mycursor.execute(query)
		result=mycursor.fetchall()
		mydb.commit()
		print(query)
		print(result)

	def show_illness(self,id_user):
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			port=3306,
			database="ssn"
		)
		l=[]
		mycursor=mydb.cursor()
		query=f"""
			SELECT
				* 
			FROM	
				patients_illness
			WHERE
				patient_fk = "{id_user}"
		"""
		mycursor.execute(query)
		result=mycursor.fetchall()
		for row in result:
			l.append(row[1])
		print(l)
		pippo=f"""
			SELECT
				 
			FROM	
				patients_illness
			WHERE
				patient_fk = "{id_user}"
		"""

	def illness_list(self):
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			port=3306,
			database="ssn"
		)
		ill=[]
		
		mycursor=mydb.cursor()
		query=f"""
			SELECT
				* 
			FROM	
				illness
		"""
		mycursor.execute(query)
		result=mycursor.fetchall()
		for illness in result:
			ill.append(illness[1])
			ill.append(illness[2])
			
		print(f"MALATTIE: {ill}")
		print(query)
		return ill

	def delete_user(self,id,password):
		mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="ssn") 
		mycursor = mydb.cursor()
		pippo=[]
		pippo.append(id)
		query=f"""
			SELECT
					password
			FROM
					PATIENTS
			WHERE
					ID={id}
		"""
		mycursor.execute(query)
		result=mycursor.fetchall()
		user_password=result
		user_password=str(result)
		user_password=user_password.replace("["," ").replace("("," ").replace("'"," ").replace(","," ").replace(")"," ").replace("]"," ")
		user_password=user_password.strip()
		print(f"LA PASSWORD DELL'UTENTE è: {user_password}")
		print(f"LA PASSWORD MANDATA è: {password}")
		if user_password==password:
			query="""DELETE FROM Patients WHERE id=%s"""
			q2="""DELETE FROM patients_illness WHERE patient_fk=%s"""
			mycursor.execute(q2,pippo)
			result=mycursor.fetchall()
			mydb.commit()
			mycursor.execute(query,pippo)
			result=mycursor.fetchall()
			mydb.commit()
		