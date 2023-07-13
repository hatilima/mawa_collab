class Person(object):
	def __init__(self, age, name):
		self.age = age
		self.name = name

	def show_person(self):
		print("The person is named "+self.name+".")
		print(self.name+" is "+str(self.age)+" years old!")



nyendwa = Person(2, "Chawanzi")

nyendwa.show_person()
