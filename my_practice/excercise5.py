a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
num=[]
for number in a:
	if number in b:
		num.append(number)
print(num)

b=[new for new if new  in a & new  in b]