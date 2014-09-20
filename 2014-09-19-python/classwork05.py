#import all with package
import math as m
print m.sin(3.14)

#import functions without package
from math import cos, tan as t, log
print cos(3.14)
print t(3.14)

#import all without package
from math import *