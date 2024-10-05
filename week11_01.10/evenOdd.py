# First approach which checks even and odd conditions in if-elif and increments 1 accordingly.
def get_even_odd_count1(L):
	even,odd = 0,0
	for i in L:
		if i%2==0:
			even+=1
		elif i%2==1:
			odd+=1
	return even,odd

# Second approach which increments even and odd count by incrementing the condition (true = 1, false = 0) in it.
def get_even_odd_count2(L):
	even,odd = 0,0
	for i in L:
		even+=(1-i%2)
		odd+= i%2
	return even,odd

# Third approach which checks even and odd in if-else block and increments 1 accordingly
def get_even_odd_count3(L):
	even,odd = 0,0
	for i in L:
		if i%2:
			odd+=1
		else:
			even+=1
	return even,odd

# Fourth approach which checks the LSB bit of binary and increments 1 accordingly.
def get_even_odd_count4(L):
	even,odd = 0,0
	for i in L:
		if int(bin(i)[-1])==0:
			even+=1
		else:
			odd+=1
	return even,odd

# Function to check the performance	
def check_performance(approaches):
	sample1 = [1,2,3,4,5,6,7,8,9,10]
	avg_time_taken = []
	for approach in approaches:
		for i in range(10):
			start_time = time.time()
			approach(sample1)
			end_time = time.time()
			time_taken =[]
			time_taken.append(end_time - start_time)
		avg_time_taken.append(sum(time_taken)/200)	#taking average of time taken by each approach

	return avg_time_taken

print(check performance([get_even_odd_count1 , get_even_odd_count2 , get_even_odd_count3 , get_even_odd_count4]))
