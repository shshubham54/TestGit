# import random
# ran_num=random.randint(1,10)
# y=int(input("Enter Your Choice from 1 to 10:- "))
# while y!=ran_num:
# 	if y>ran_num:
# 		print("too high, try again")
# 	else:
# 		print("too low, Try again")
# 	y=int(input("Enter Your Choice from 1 to 10 :- "))

# print("That is correct")








#play on a repeat
import random
ran_num=random.randint(1,10)
y=int(input("Enter Your Choice from 1 to 10:- "))
while True:
	if y>ran_num:
		print("too high, try again")
	elif y<ran_num:
		print("too low, Try again")

	else:
		print("WELL DONE that is correct!!")
		
		play_again=input("Enter (y) to keep playing the game and (n) to quit\n")
		if play_again=="y":
			ran_num=random.randint(1,10)
		else:
			print("Thank You for Playing")
			break

	y=int(input("Enter Your Choice from 1 to 10 :- "))

