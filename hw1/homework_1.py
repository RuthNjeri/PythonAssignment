# Name: Ruth Waiganjo
# Section: 2.1
# Date: 23 April 2017
# homework_1.py

print ("********** Exercise 2.1 **********")

# Do your work for Exercise 2.1 here

player1 = input("Player 1:")

player2 = input("Player 2:")

if player1 and player2 in {"rock","paper","scissors"}:
	if player1 == player2:
		print ("It is a tie")

	elif player1 =="rock" and player2=="scissors":
		print("Player 1 wins. Congratulations!")

	elif player1 =="scissors" and player2=="rock":
		print("Player 2 wins. Congratulations!")

	elif player1 =="rock" and player2=="paper":
		print("Player 2 wins. Congratulations!")

	elif player1 =="paper" and player2=="rock":
		print("Player 1 wins. Congratulations!")

	elif player1 =="paper" and player2=="scissors":
		print("Player 2 wins. Congratulations!")

	elif player1 =="scissors" and player2=="paper":
		print("Player 1 wins. Congratulations!")

else:
	print("Please enter either rock, paper or scissors")



# ##### Template for Homework 1, exercises 1.2-1.4 ######

# print "********** Exercise 1.2 **********"

# # Do your work for Exercise 1.2 here

# print "Not implemented" # Delete this line when you write your code!


# print "********** Exercise 1.3 **********"

# # Do your work for Excercise 1.3 here. Hint - how many different
# # variables will you need?

# print "Not implemented" # Delete this line when you write your code!


# print "********** Exercise 1.4 **********"

# # Do your work for Exercise 1.4 here.

# print "Not implemented" # Delete this line when you write your code!

