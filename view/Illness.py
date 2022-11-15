class illness():
    def __init__(self,id,name,description):
        self._id=id
        self._name=name
        self._description=description

    def already_exist(self,name):
        if self._name.lower()==name.lower():
            return True
        else:
            return False
    
    def __str__(self):
        return f"""{self._id}, {self._name},{self._description}"""