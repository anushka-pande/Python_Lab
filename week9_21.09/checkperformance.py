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
	
print(check_performance([f1, f2]))

# Create a function to call check_performance multiple times to check the winner function from f1 and f2
