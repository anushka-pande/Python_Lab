import random
"""
def initialize(size):
	game_state = dict()
	for i in range(1, size + 1):
		d = dict()
		for j in range(1, size + 1):
			d[j] = ""
		game_state[i] = d
	return game_state

gs = initialize(3)
print(gs)
"""
def initialize(size):
	game_state = dict()
	for i in range(1, size + 1):
		game_state[i] = dict.fromkeys(range(1, size + 1), " ")
	return game_state

"""	
gs = initialize(3)
gs[1][1] = 'A'
print(gs)
"""


def display_layout(game_state, size):
	print(" ---" * size)
	for i in range(1, size + 1):
		for j in range(1, size + 1):
			print('| {} '.format(game_state[i][j]), end = "")
		print("|")
		print(" ---" * size)

"""
gs = initialize(3)
print(display_layout(gs, 3))
"""

def check_result(game_state, size):
	for row in range(1, size + 1):
		if game_state[row][1] != " " and all(game_state[row][col] == game_state[row][1] for col in range(1, size + 1)):
			return game_state[row][1]
	
	for col in range(1, size + 1):
		if game_state[1][col] != " " and all(game_state[row][col] == game_state[1][col] for row in range(1, size + 1)):
			return game_state[1][col]
	
	if game_state[1][1] != " " and all(game_state[i][i] == game_state[1][1] for i in range(1, size + 1)):
		return gaem_state[1][1]
	
	if game_state[1][size] != " " and all(game_state[i][size - i + 1] == game_state[1][size] for i in range(1, size + 1)):
		return gaem_state[1][size]
	
	return None

def start_game(game_state, size):
	player1 = input("Enter Name Of The Player 1: ")
	player2 = input("Enter Name Of The Player 2: ")
	
	players = [player1[0].upper(), player2[0].upper()]
	if len(set(players)) == 1:
		players[1] = player2[1].upper()
	
	current_player = random.choice(players)
	previous_player = current_player
	moves = 0
	grid = size * size
	print(display_layout(game_state, size))
	while moves < grid:
		current_player = players[0] if previous_player == players[1] else players[1]
		previous_player = current_player
		
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
		print(display_layout(game_state, size))
		moves += 1
		
		if moves >= (size * len(players) - 1):
			winner = check_result(game_state, size)
			if winner:
				winner_name = player1 if winner == players[0] else player2
				print(f"{winner_name} wins.")
				break
	else:
		print("It's a Tie!")
		

gs = initialize(3)
print(start_game(gs, 3))


