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

#Возвращает дату в виде кортежа (iso_year, iso_week, iso_weekday), где поле 
#iso_week содержит число в диапазоне от 1 до 53, а поле iso_weekday – число 
#в диапазоне от 1 (понедельник) до 7 (воскресенье). Значение 1 в поле iso_
#week соответствует первой неделе года, включающей четверг. 
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

##td = date1 - date2 Возвращает объект timedelta
##date2 = date1 + td Добавляет разность timedelta к объекту date
##date2 = date1 - td Вычитает разность timedelta из объекта date
##date1 < date2 Сравнивание дат

##td3 = td2 + td1 Складывает две разности
##td3 = td2 - td1 Вычитает одну разность из другой
##td2 = td1 * i Умножает на целое число
##td2 = i * td1
##td2 = td1 // i Целочисленное деление на i с округлением вниз
##td2 = -td1 Унарные минус и плюс428 Глава 19. Службы операционной системы 
##td2 = +td1
##abs(td) Абсолютное значение
##td1 < td2 Сравнивание
##td1 <= td2
##td1 == td2
##td1 != td2
##td1 > td2
##td1 >= td2
