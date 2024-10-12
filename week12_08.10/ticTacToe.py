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

# Initialize funtion which initialize game board (size x size) with empty spaces
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
	board_size = input("\nEnter the size of the Tic-Tac-Toe board (e.g., 3 for 3x3): ")

	if not board_size.isdigit() or int(board_size) < 3:
		print("Invalid input. Starting default 3x3 board.")
		board_size = 3
	else:
		board_size = int(board_size)
	
	# Initialize the game board and start the game
	gs = initialize(board_size)
	start_game(gs, board_size)


# Start the game by calling the Play game function
play_game()

