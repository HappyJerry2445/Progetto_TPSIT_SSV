
class user():
	def __init__(self,id=-1000,name='',surname='',is_male=-1,birth_date='',birth_place='',cf='',password='***'):
		self._id=id
		self._name=name
		self._surname=surname
		self._is_male=is_male
		self._birth_date=birth_date
		self._birth_place=birth_place
		self._cf=cf
		self._password=password

		
	def __str__(self):
		return f"""{self._id}, {self._name},{self._surname},{self._is_male},{self._birth_date},{self._birth_place},{self._cf}, {self._password}"""