def sandwich(somefood):
	
	def wrapper():
		print kind + "Bread"
		somefood()
		print kind + "Bread"
		
	return wrapper

@sandwich()
def food():
	print "Meat"
	
food()