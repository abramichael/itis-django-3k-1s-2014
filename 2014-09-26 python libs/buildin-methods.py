class CN:
    def __init__(self,a,b):
        self.re = a
        self.im = b
        
    def __add__(a,c):
        return CN(a.re + c.re, a.im + c.im)

    def __neg__(x):
        return CN(-x.re, -x.im)
    
    def __str__(self):
        return str(self.re) + " + i * " + str(self.im)

c1 = CN(1,2)
c2 = CN(2,3)
c3 = c1 + c2
print c3
print -c1

class Numbers3:
    def __init__(self):
        self.a = 2
        self.b = 3
        self.c = 4
    def __contains__(x,e):
        return (e==x.a or e == x.b or e == x.c)
    def __getitem__(x,e):
        if e == 1:
            return x.a
        elif e == 2:
            return x.b
        elif e == 3:
            return x.c
        else:
            raise Exception('aaa')
    def __call__(self, x):
        print x

        
n = Numbers3()
x = 2
y = 1
print x in n, y in n
print n[1], n[2], n[3]
n('Hello')
