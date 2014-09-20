#!coding: utf-8
def d(day=20, month=9, year=2014):
    print "Date is: %s-%s-%s" % (day, month, year)
    # А вот так не надо делать!!! :
    # print "Date is: " + str(day) + \
    #         "-" + str(month) + "-" + str(year)

d(2, year=2010, month=1)