import random
""" 
This game is called "Guess The Number And Win the Prize."
It uses random library to generate an integer between a particular range.
"""
def guessTheNumWinPrizes():
	print("Welcome to the 'Guess The Number And Win The Prize' game!!!")
	print("I have chosen a number between 0 to 100. Try to guess it!")
	print("You have 5 attempts to guess the number.")
	magic_num = random.randint(0, 100)	# generate a random number between 0 to 100
	attempts = 5		# Attempts given to the player
	entered_amount = 10	# Amount paid by player
	
	# A dictionary that defines the rewards according to the attempts
	rewards = {
		1 : 5, 
		2 : 3, 
		3 : 2, 
		4 : 1.5, 
		5 : 1
	}
	# Helper function to check how far is the guessed number from magic number.
	def checkUserInput(num, magic_num):
		difference = magic_num - num
		# Analysis based on the difference between magic number and guessed number
		if difference > 20:
			return f"The {num} is too small."
		elif 0 < difference <= 20:
			return f"The {num} is a little small."
		elif difference == 0:  
			return True
		elif -20 <= difference < 0:
			return f"The {num} is a little large."
		elif difference < -20:
			return f"The {num} is too large."
		
	# For loop that iterates from attempt 1 to 5, taking player input in each attempt and checking the input using helper function also includes few conditions like input must be int and it must be between 0 to 100 else the loop terminates.
	for i in range(1, attempts + 1):
		print(f"\nAttempt {i}: ")
		num_input = input("Enter a number between 0 to 100: ")
		
		if num_input.isdigit():
			num = int(num_input)
			if num >= 0 and num <= 100:
				result = checkUserInput(num, magic_num)
				if result is True:
					# reward per attempt accoding to rewards dictionary
					reward = entered_amount * rewards[i]
					return f"Congratulations! You guessed the {magic_num} in the {i} attempt and won Rs.{int(reward)}!"
				else:
					print(result)
			else:
				return "Invalid Number. Please enter a valid number between the range of 0 to 100."
		else:
			return "Invalid input. Please enter an integer between the range of 0 to 100."
	# If all attempts are used but player didn't guessed the number correctly, for loop terminates and else part is executed.
	else:
		return f"Sorry! You have used all attempts. The correct number was {magic_num}.You lost Rs.10!"

# Function call
print(guessTheNumWinPrizes())

