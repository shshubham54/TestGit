a=int(input("Enter the no:-"))
x=list(range(2,round(a/2+1)))
num=[]
for i in x:
	if a%i==0:
			num.append(i)

print(num)