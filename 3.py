import math
a=input('Enter a:')
a=int(a)
b=input('Enter b:')
b=int(b)
z=(math.sqrt(b-a))/(a**2)*abs(math.cos(math.radians(15)))/(math.sin(math.radians(15)))
print('z=',z)