class A(object):
    def __init__(self):
        print "Parent"
    def f(self):
        print 1
    
class B(A):
    def __init__(self):
		#calling parent constructor"
        super(B, self).__init__()
        print "Child"
    def f(self):
        super(B, self).f()
        print 2
        
b = B()
b.f()
    
