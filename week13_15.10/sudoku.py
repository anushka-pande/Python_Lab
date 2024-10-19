import random
import math
import time

# Create the empty game state (size x size grid filled with empty spaces) 
def create_game_state(size):
	# # Using list comprehension to create 2D list
	return [list(" " * size) for i in range(size)]
	
# Displays the current game state layout with boundaries
def display_layout(game_state, size):
	print(" ---" * size)	# Print the top boundary of the game state
	for i in range(size):
		for j in range(size):
			print('| {} '.format(game_state[i][j]), end = "")	# Display each cell's content
		print("|")	# Print the right boundary
		print(" ---" * size)	# Print the bottom boundary of the game state

# Create a filled puzzle with random valid entries for the Sudoku game state
def create_puzzle(size): 
	game_state = create_game_state(size)
	possibilities = set(range(1, size + 1))	# Possible values for each cell
	for row in range(size):
		for col in range(size):
			# Check row-wise and column-wise available values
			availablities = set(game_state[row] + [r[col] for r in game_state])
			candidates = list(possibilities - availablities)
			if candidates:
				game_state[row][col] = candidates[random.randint(0, len(candidates) - 1)]
			else:
				return create_puzzle(size)	# Retry if stuck
	return game_state

# Create a copy of the complete solution before hiding values
def create_solution_copy(game_state):
	return [row[:] for row in game_state]	# Deep copy the game state
	
# Initialize the game, allowing the player to choose size and difficulty
def initialize():
	# Print welcome message
	print("***********************************************************")
	print("*                 Welcome to Sudoku!                      *")
	print("*             Get ready to have some fun!                 *")
	print("***********************************************************")
	time.sleep(2)	# A short pause for dramatice effect
	print("\nLet's get started!")
	
	# Get user input for the size of the Sudoku game state
	size = input("\nEnter size of the Sudoku game state (e.g., 3 for 3x3): ")
	
	# Validate the size input
	if not size.isdigit() or int(size) < 3:
		print("Invalid input. Starting default 3x3.")
		size = 3
	else:
		size = int(size)
	
	game_state = create_puzzle(size)
	solution = create_solution_copy(game_state)	# Copy the complete solution
	
	# Difficulty levels with hidden percentages
	levels = {1 : ("Very Easy", 20), 2 : ("Easy", 35), 3 : ("Medium", 50), 4 : ("Hard", 60), 5 : ("Very Hard", 75)}
	
	print("\nThere are 5 levels of the game.")
	for key, value in levels.items():
		print(f"Level{key} : {value[0]}")
	
	# Get player's difficulty choice
	level = int(input("Choose the game level (1 - 5): "))
	
	# Calculate the number of hidden cells based on the chosen level
	no_of_hidden_level = math.ceil((levels[level][1] * (size * size))/100)
	hidden_fields = []
	all_possibilities = list(range(size * size))
	
	# Randomly hide cells in the puzzle based on difficulty level
	for _ in range(no_of_hidden_level):
		n = all_possibilities.pop(random.randint(0, len(all_possibilities) - 1))
		hidden_fields.append((math.floor(n / size), (n % size)))
	
	for r,c in hidden_fields:
		game_state[r][c] = 'X'	# Mark the hidden cells with 'X'
	
	return game_state, hidden_fields, solution, size
	
# Start the game and let the player fill in the hidden values
def start_game(game_state, hidden_fields, size):
	display_layout(game_state, size)	# Display the initial game state 
	
	# Allow user input for each hidden cell
	for r, c in hidden_fields:
		while True:
			try:
				value = int(input(f"Enter value for {(r + 1, c + 1)}: "))
				if 1 <= value <= size:
					game_state[r][c] = value
					break
				else:
					print(f"Invalid input! Please enter a value between 1 and {size}.")
			except ValueError:
				print("Invalid input! Please enter a valid number.")
		
	display_layout(game_state, size)	# Show game state after player inputs
	return game_state
	
# Check if the player's inputs are valid row-wise and column-wise
def check_valid(game_state, size):
	for row in range(size):
		for col in range(size):
			value = game_state[row][col]
			if value != 'X':	# Ignore hidden cells
				if not is_valid_value(game_state, row, col, value, size):
					return False
	return True
	
# Helper function to check row-wise and column-wise validity
def is_valid_value(game_state, row, col, value, size):
	if game_state[row].count(value) > 1:	# Check if the value appears more than once in the row
		return False
	if[game_state[i][col] for i in range(size)].count(value) > 1:	# Check column-wise
		return False
	return True

# End the game and check if the player has won or lost, showing the solution if lost
def stop_game(game_state, solution, size):
	print("\nChecking your answers...")
	time.sleep(2)
	
	if check_valid(game_state, size):
		print("Congratulations! All your entries are valid.")
	else:
		print("Game Over! Some of your entries are invalid.")
		print("Here is the correct solution:")
		display_layout(solution, size)
		
# Main function to run the Sudoku game
def sudoku():
	game_state, hidden_fields, solution, size = initialize()
	game_state = start_game(game_state, hidden_fields, size)
	stop_game(game_state, solution, size)

sudoku()


