def f(c):
    def g():
        print "G"
    def h():
        print "H"

    if (c=='g'):
        return g
    elif (c=='h'):
        return h
    else:
        return None

function = f('g')
function()