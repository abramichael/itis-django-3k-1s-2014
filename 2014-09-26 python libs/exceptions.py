try:
    f = open("1.txt")
except IOError as e:
    print "Oops"

else:
    try:
        print f.read()
        a = 2 / 0
    except ZeroDivisionError:
        print "zero"
    finally:
        print "==FINALLY=="
        f.close()
        
class MyError(Exception):
    def __init__(self,errno,msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg
        
raise MyError(2,"AAAA")
