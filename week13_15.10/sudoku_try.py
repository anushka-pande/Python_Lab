import random
import math

# Create the empty game state
def create_game_state(size):
	# Create game state
	"""
	game_state = dict()
	for i in range(1, size + 1):
		game_state[i] = dict.fromkeys(range(1, size + 1), " ")		# Create a dict for each row with empty spaces
	return game_state
	"""
	return [list(" " * size) for i in range(size)]		# Using list comprehension
	
# Displays the current game board layout
def display_layout(game_state, size):
	print(" ---" * size)	# Print the top boundary of the board
	for i in range(size):
		for j in range(size):
			print('| {} '.format(game_state[i][j]), end = "")	# Display each cell's content
		print("|")	# Print the right boundary
		print(" ---" * size)	# Print the bottom boundary of the grid

def create_puzzle(size): 
	game_state = create_game_state(size)
	possibilities = set(range(1, size + 1))
	for row in range(size):
		for col in range(size):
			availablities = set(game_state[row] + [r[col] for r in game_state])
			candidates = list(possibilities - availablities)
			if candidates:
				game_state[row][col] = candidates[random.randint(0, len(candidates) - 1)]
			else:
				return create_puzzle(size)
	return game_state

def create_solution_copy(game_state):
	return [row[:] for row in game_state]
	
# Initialization function which initialize the game state (size x size)
def initialize():
	# Print welcome message
	print("Welcome to Sudoku!!")
	# User input for the size of the game state
	size = input("\nEnter size of the Sudoku game state (e.g., 3 for 3x3): ")
	
	# Validate size input
	if not size.isdigit() or int(size) < 3:
		print("Invalid input. Starting default 3x3.")
		size = 3
	else:
		size = int(size)
	
	game_state = create_puzzle(size)
	solution = create_solution_copy(game_state)
	
	levels = {1 : ("Very Easy", 20), 2 : ("Easy", 35), 3 : ("Medium", 50), 4 : ("Hard", 60), 5 : ("Very Hard", 75)}
	
	print("There are 5 levels of the game.")
	for key, value in levels.items():
		print(f"Level{key} : {value[0]}")
	level = int(input("Choose the game level: "))
	no_of_hidden_level = math.ceil((levels[level][1] * (size * size))/100)
	hidden_fields = []
	all_possibilities = list(range(size * size))
	for _ in range(no_of_hidden_level):
		n = all_possibilities.pop(random.randint(0, len(all_possibilities) - 1))
		hidden_fields.append((math.floor(n / size), (n % size)))
	for r,c in hidden_fields:
		game_state[r][c] = 'X'
	return game_state, hidden_fields, solution, size
	
def start_game(game_state, hidden_fields, size):
	# Display the initial game state 
	display_layout(game_state, size)
	for r, c in hidden_fields:
		game_state[r][c] = int(input(f"Enter value for {(r + 1, c + 1)}: "))
	display_layout(game_state, size)
	return game_state
	
def check_valid(game_state, size):
	for row in range(size):
		for col in range(size):
			value = game_state[row][col]
			if value != 'X':
				if not is_valid_value(game_state, row, col, value, size):
					return False
	return True
	
def is_valid_value(game_state, row, col, value, size):
	if game_state[row].count(value) > 1:
		return False
	if[game_state[i][col] for i in range(size)].count(value) > 1:
		return False
	return True

def stop_game(game_state, solution, size):
	if check_valid(game_state, size):
		print("Congratulations! All your entries are valid.")
	else:
		print("Game Over! There are invalid entries. Here is the correct solution.")
		display_layout(solution, size)
		

def sudoku():
	game_state, hidden_fields, solution, size = initialize()
	game_state = start_game(game_state, hidden_fields, size)
	stop_game(game_state, solution, size)

sudoku()



"""
import random
import time

# Function to display a welcome message with a delay for effect
def welcome_message():
	print("***********************************************************")
	print("*               Welcome to Tic-Tac-Toe!                   *")
	print("*             Get ready to have some fun!                 *")
	print("***********************************************************")
	time.sleep(1)	# A short pause for dramatice effect
	print("\nLet's get started!")

# Initialize funtion which initialize game (size x size) with empty spaces
def initialize(size):
	game_state = dict()
	for i in range(1, size + 1):
		game_state[i] = dict.fromkeys(range(1, size + 1), " ")	# Create a dict for each row with empty spaces
	return game_state

# Displays the current game board layout
def display_layout(game_state, size):
	print(" ---" * size)	# Print the top boundary of the board
	for i in range(1, size + 1):
		for j in range(1, size + 1):
			print('| {} '.format(game_state[i][j]), end = "")	# Display each cell's content
		print("|")	# Print the right boundary
		print(" ---" * size)	# Print the bottom boundary of the grid

# Checks if there is a winner after each move
def check_result(game_state, size):
	# Check each row for a winner
	for row in range(1, size + 1):
		if game_state[row][1] != " " and all(game_state[row][col] == game_state[row][1] for col in range(1, size + 1)):
			return game_state[row][1]
	
	# Check each coloumn for a winner
	for col in range(1, size + 1):
		if game_state[1][col] != " " and all(game_state[row][col] == game_state[1][col] for row in range(1, size + 1)):
			return game_state[1][col]
	
	# Check the main diagonal for a winner
	if game_state[1][1] != " " and all(game_state[i][i] == game_state[1][1] for i in range(1, size + 1)):
		return game_state[1][1]
	
	# Check the anti-diagonal for a winner
	if game_state[1][size] != " " and all(game_state[i][size - i + 1] == game_state[1][size] for i in range(1, size + 1)):
		return game_state[1][size]
	
	return None	# No winner yet or Tie

# The start_game function starts the game loop and manages player turns
def start_game(game_state, size):	
	# Get player names and create symbols (initials) for each player
	player1 = input("\nEnter Name Of The Player 1: ")
	player2 = input("\nEnter Name Of The Player 2: ")
	
	print(f"\nHello {player1} and {player2}! Let's see who will be the Tic-Tac-Toe master!\n")
	players = [player1[0].upper(), player2[0].upper()]	# Take first letters of their names
	if len(set(players)) == 1:	# Ensure the symbols are different
		players[1] = player2[1].upper()
	
	current_player = random.choice(players)	# Randomly pick the starting player
	moves = 0	# Track the number of moves made
	grid = size * size	# Total number of cells
	
	print(f"{current_player} will start the game!\n")
	display_layout(game_state, size)	# Display initial empty board
	
	# Game loop
	while moves < grid:		
		# Get valid move imput from the current player
		while True:
			input_move = input(f"{current_player}, Enter your move \nPlease enter two integers separated by one space (row col): ").split()
			if len(input_move) == 2 and input_move[0].isdigit() and input_move[0].isdigit():
				row, col = int(input_move[0]), int(input_move[1])
				
				if 1 <= row <= size and 1 <= col <= size and game_state[row][col] == " ":
					game_state[row][col] = current_player
					break
				else:
					print("Invalid input or position already taken. Try again.")
			else:
				print("Please enter two valid integers.")
		
		display_layout(game_state, size)	# Display the updated board
		moves += 1
		
		# Check for a winner after enough moves have been made
		if moves >= (size * len(players) - 1):
			winner = check_result(game_state, size)
			if winner:
				winner_name = player1 if winner == players[0] else player2
				print(f"\nCongratulations {winner_name}, you win!\n")
				break
			
		# Switch turn between players
		current_player = players[0] if current_player == players[1] else players[1]
	# When all moves are used and there is no winner
	else:
		print("\nIt's a Tie! Well played both of you!\n")
		
# Play game function to control the flow of game
def play_game():
	# Display the welcome message
	welcome_message()
	
	# user input for the board size and validate input
	size = input("\nEnter the size of the Tic-Tac-Toe board (e.g., 3 for 3x3): ")

	if not size.isdigit() or int(size) < 3:
		print("Invalid input. Starting default 3x3 board.")
		size = 3
	else:
		size = int(size)
	
	# Initialize the game board and start the game
	gs = initialize(size)
	start_game(gs, size)


# Start the game by calling the Play game function
play_game()
"""


