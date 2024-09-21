import time
def factorial_1(num):
	if num < 0:
		return "Invalid number."
	if num < 2:
		return 1
	else:
		fact = 1
		for i in range(1, num + 1):
			fact *= i
		return fact

# print(factorial_1(5))

def factorial_2(num):
	if num < 0:
		return "Invalid number."
	if num > 1:
		fact = 1
		for i in range(1, num + 1):
			fact *= i
		return fact
	else:
		return 1
	
# print(factorial_2(5))

def f1():
	for num in range(1, 1500, 2):
		x = factorial_1(num)
		
def f2():
	for num in range(1, 1500, 2):
		x = factorial_2(num)
		
def check_performance(approaches):
	avg_time_taken = []
	for approach in approaches:
		time_taken = []
		for i in range(500):
			start_time = time.time()
			approach()
			end_time = time.time()
			time_taken.append(end_time - start_time)
		avg_time_taken.append(sum(time_taken) / 500)
	return avg_time_taken
	

def check_performance_multiple_times(iterations):
	f1_wins = 0
	f2_wins = 0
	
	for _ in range(iterations):
		times = check_performance([f1, f2])
		if times[0] < times[1]:
			f1_wins += 1
		elif times[0] > times[1]:
			f2_wins += 1
		
	if f1_wins > f2_wins:
		return f"f1 is faster: f1 won {f1_wins} times, f2 won {f2_wins} times"
	elif f1_wins < f2_wins:
		return f"f2 is faster: f1 won {f1_wins} times, f2 won {f2_wins} times"
	else:
		return f"It's a tie: both f1 and f2 won {f1_wins} times"	
		
		
print(check_performance_multiple_times(200))


