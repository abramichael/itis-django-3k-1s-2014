def sum(a, b):
	return a + b

def fact(n):
	if isinstance(n, int):
		if n >= 2:
			return n * fact(n - 1)
		elif n < 0:
			raise ValueError
		else:
			return 1
	else:
		raise TypeError