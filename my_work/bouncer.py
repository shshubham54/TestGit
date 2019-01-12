age =(input("how old are you:- "))
if age:
	age=int(age)
	if age >= 18 and age < 21:
		print("where is ur band")
	elif age>21:
		print("welcome")
	else:
		print("SORRY! u r not allowed")

else:
	print("i repeat whats ur age")