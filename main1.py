#Задание 1 Семёнов Иван 44 22 122
from sys import argv
import math
script, x = argv
x=int(x)
if x < 1.5:
    y = math.sin(x)*x**0.5
else:
    y = math.e**(1.4*x*2)-4.9
print("y=",y)