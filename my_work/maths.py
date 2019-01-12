import math
x=1
y=100
for i in range(1,100):
	z=(pow(x,i))/(math.factorial(i))
	#print(z)
	z=z+z
print(z)
m=math.exp(2)
print(m)
a=m-z
print(a)