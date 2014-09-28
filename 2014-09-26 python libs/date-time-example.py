# -*- coding: cp1251 -*-
from datetime import *

print MINYEAR
print MAXYEAR

d = date(2013, 12, 4)
print d
print d.year
print d.month
print d.day

print date.today()
print date.fromtimestamp(0) #time.time()

print date.fromordinal(434242)

print d.ctime()

#���������� ���� � ���� ������� (iso_year, iso_week, iso_weekday), ��� ���� 
#iso_week �������� ����� � ��������� �� 1 �� 53, � ���� iso_weekday � ����� 
#� ��������� �� 1 (�����������) �� 7 (�����������). �������� 1 � ���� iso_
#week ������������� ������ ������ ����, ���������� �������. 
print d.isocalendar()

print d.isoformat()
print d.isoweekday()
print d.weekday()

d.replace(month=2)
print d.timetuple()

print d.toordinal()


print "=================="

t = time(21,4)
print t

print time.min
print time.max

print t.hour, t.minute, t.second

print t.isoformat()
t.replace(second=30)

dt = datetime(2014,02,15,20)
print dt
print datetime.combine(d,t)
print datetime.now()
print datetime.fromordinal(5)
print datetime.fromtimestamp(100)
print dt.date()
print dt.time()

td = timedelta(31)

##td = date1 - date2 ���������� ������ timedelta
##date2 = date1 + td ��������� �������� timedelta � ������� date
##date2 = date1 - td �������� �������� timedelta �� ������� date
##date1 < date2 ����������� ���

##td3 = td2 + td1 ���������� ��� ��������
##td3 = td2 - td1 �������� ���� �������� �� ������
##td2 = td1 * i �������� �� ����� �����
##td2 = i * td1
##td2 = td1 // i ������������� ������� �� i � ����������� ����
##td2 = -td1 ������� ����� � ����428 ����� 19. ������ ������������ ������� 
##td2 = +td1
##abs(td) ���������� ��������
##td1 < td2 �����������
##td1 <= td2
##td1 == td2
##td1 != td2
##td1 > td2
##td1 >= td2
