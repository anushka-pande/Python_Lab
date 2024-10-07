import time
# First approach which checks even and odd conditions in if-elif and increments 1 accordingly.
def get_even_odd_count1(L):
	even, odd = 0, 0
	for i in L:
		if i % 2 == 0:
			even += 1
		elif i % 2 == 1:
			odd += 1
	return even, odd

# Second approach which increments even and odd count by incrementing the condition (true = 1, false = 0) in it.
def get_even_odd_count2(L):
	even, odd = 0, 0
	for i in L:
		even += (1 - i % 2)
		odd += i % 2
	return even, odd

# Third approach which checks even and odd in if-else block and increments 1 accordingly
def get_even_odd_count3(L):
	even, odd = 0, 0
	for i in L:
		if i % 2:
			odd += 1
		else:
			even += 1
	return even, odd

# Fourth approach which checks the LSB bit of binary and increments 1 accordingly.
def get_even_odd_count4(L):
	even, odd = 0, 0
	for i in L:
		if int(bin(i)[-1]) == 0:
			even += 1
		else:
			odd += 1
	return even, odd

# Function to check the performance	
def check_performance(approaches):
	sample1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	avg_time_taken = []
	for approach in approaches:
		for _ in range(10):
			approach(sample1)
	for approach in approaches:
		time_taken = []
		for _ in range(1000):
			start_time = time.time()
			approach(sample1)
			end_time = time.time()
			time_taken.append(end_time - start_time)
		avg_time_taken.append(sum(time_taken) / 1000)
	return avg_time_taken

# Funtion to find the percentage of better approaches
def better_approach():
	list_of_time = check_performance([get_even_odd_count1, get_even_odd_count2, get_even_odd_count3, get_even_odd_count4])
	apr1, apr2, apr3, apr4 = list_of_time[0], list_of_time[1], list_of_time[2], list_of_time[3]
	percent_apr2 = ((apr1 - apr2) / apr1) * 100
	percent_apr3 = ((apr1 - apr3) / apr1) * 100
	percent_apr4 = ((apr1 - apr4) / apr1) * 100
	
	print("Approach1 is the base approach.")
	
	if percent_apr2 < 0:
		print(f"Approach 1 is {-percent_apr2}% slower than approach 2")
	else:
		print(f"Approach 1 is {percent_apr2}% faster than approach 2")
	if percent_apr3 < 0:
		print(f"Approach 1 is {-percent_apr3}% slower than approach 3")
	else:
		print(f"Approach 1 is {percent_apr3}% faster than approach 3")
	if percent_apr4 < 0:
		print(f"Approach 1 is {-percent_apr4}% slower than approach 4")
	else:
		print(f"Approach 1 is {percent_apr4}% faster than approach 4")

	fastest_time = min(list_of_time)
	fastest_index =  list_of_time.index(fastest_time)
	print(f"Approach {fastest_index + 1} is the fastest.")

better_approach()

