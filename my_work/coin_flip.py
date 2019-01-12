import random
a=random.randint(1,2)
def coin_toss():
	if a==1:
		return print("HEAD")
	else:
		return print("TAIL")
coin_toss()