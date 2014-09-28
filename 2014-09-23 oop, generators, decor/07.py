def sandwich(somefood):
	
	def wrapper():
		print "Bread"
		somefood()
		print "Bread"
		
	return wrapper

def food():
	print "Meat"
	
food()
print
food = sandwich(food)
food()