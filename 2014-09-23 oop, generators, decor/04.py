class Student:
	def __init__(self, name):
		self.name = name
	def f(self):
		self.__age = 20
	def g(self):
		print self.__age
	def __str__(self):
		return "Student:" + self.name
	def __call__(self):
		print "Calling " + self.name

s = Student("Roma-Pasha")
s.f()
s.g()
print dir(s)
# Access to private x, not recommended
print s._Student__age

print s
s()