import random
player_win=0
computer_win=0
while computer_win < 2 and player_win < 2:
	print(f"player_wins = {player_win} and computer_wins = {computer_win}")
	p1 = input("Enter your choice: rock, paper, or scissors \n")
	if p1=="quit":
		break
	#p2 = input("Player 2: rock, paper, or scissors ")
	p2 =  random.randint(1,3)
	p3=str(p2)
	if p3=="1":
	 	p3="rock"
	elif p3== "2":
	 	p3="paper"
	elif p3=="3":
		p3="scissors"
	#print(p3)
	print(f"computer chooses "+ p3)

	if p1 == p3:
		print("Tt's a Draw")
	elif p1 == "rock" and p3 == "scissors":
		print("you win") 
		player_win+=1
	elif p1 == "paper" and p3 == "rock":
	    print("you win")
	    player_win+=1
	elif p1 == "scissors" and p3 == "paper":
	    print("you win")
	    player_win+=1
	else:
		print("computer wins")
		computer_win+=1
		
if computer_win==2:
	print("You SUCK go back to your mamma")
else:
	print("You are a genious!! Teach me master ")
			


