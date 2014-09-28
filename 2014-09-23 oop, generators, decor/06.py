import math

lst = range(10)
result_lst = map(math.exp, lst)
print result_lst

#for kids (6+)
#def check3(n):
#	return (n % 3 == 0)
#result_lst2 = filter(check3, lst)

#for adults (18+)
result_lst2 = filter(lambda x: x % 3 == 0, lst)
print result_lst2
