lst = [i*i for i in xrange(10)]
print lst

maximum = max([
	int(raw_input()) for i in xrange(int(raw_input()))
])

lst2 = [i*i for i in xrange(10) if i % 2]
print lst2