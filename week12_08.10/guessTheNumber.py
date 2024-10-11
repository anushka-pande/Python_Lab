import random
def guessTheNumber():
	magic_num = random.randint(0, 10)
	num = int(input("Enter a number between 1 to 10: "))
	if num >= 0 and num <= 10:
		if num == magic_num:
			return "Congratulations! You guessed the number correctly."
		else:
			return "Better luck next time! You lose."
	else:
		return "Invalid Number."

print(guessTheNumber())
