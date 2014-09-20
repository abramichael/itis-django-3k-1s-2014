x = 2
y = 3

print locals()

def f():
    global x
    z = 3
    u = 8
    x = 5
    print locals()
    print globals()

f()
