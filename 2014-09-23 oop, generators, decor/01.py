#generator
def f():
	i = 0
	while i < 100:
		yield i
		i += 1

for i in f():
	print i

#same thing
for i in xrange(100):
	print i