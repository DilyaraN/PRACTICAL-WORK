import math
a=input('Enter a:')
a=int(a)
z=(math.pow(a,1/3)*math.sin(math.pow(a,5)))/(a+math.exp(a))
print('z=',z)