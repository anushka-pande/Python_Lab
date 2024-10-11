import random
""" 
This game is called "Guess The Number."
It uses random library to generate an integer between the range of 0 to 10.
"""
def guessTheNumber():
	print("Welcome to the 'Guess The Number' game!!!")
	print("I have chosen a number between 0 to 10. Try to guess it!")
	magic_num = random.randint(0, 10)	# Generates a number between the range of 0 to 10
	
	num_input = input("Enter your choice between 0 to 10: ")	# Player input
	# This function includes few conditions the input must be integer and must be between the range of 0 to 10 
	if num_input.isdigit():
		num = int(num_input)
		if num < 0 or num > 10:
			return "Invalid Choice! Please choose a number between the range of 0 to 10."
		else:
			if num == magic_num:
				return "Congratulations! You guessed the number correctly."
			else:
				return f"Oops! The correct number was {magic_num}. Better luck next time!"
	else:
		return "Please enter a valid integer between the range of 0 to 10."

print(guessTheNumber())
