import time
def isPalindrome(text):
	return text == text[::-1]
	
def fun1(L):
	for _ in range(10,100,2) :
		count = 0
		valid_obj_count = [int, str]
		valid_obj = [list, tuple, set]
		for item in L:
			type_of_item = type(item)
			if type_of_item in valid_obj_count:
				if type_of_item == int:
					item = str(item)
				if len(item) % 6 == 3:
					if isPalindrome(item):
						count += 1
			elif type_of_item in valid_obj:
				count += fun1(item)
	return count

def fun(L):
	for _ in range(10,100,2) :
		count = 0
		valid_obj_count = {int, str}
		valid_obj = {list, tuple, set}
		for item in L:
			type_of_item = type(item)
			if type_of_item in valid_obj_count:
				if type_of_item == int:
					item = str(item)
					count += (len(item) % 6 == 3 and item == item[::-1])
			elif type_of_item in valid_obj:
				count += fun(item)
	return count
	
def check_performance(approaches):
    sample1 = [12345, "level", 1221, [54321, 131], {"racecar", 131 , 98789}]
    avg_time_taken = []
    for approach in approaches:
        for _ in range(10):
            approach(sample1)
    for approach in approaches:
        time_taken = []
        for _ in range(100):
            start_time = time.time()
            approach(sample1)
            end_time = time.time()
            time_taken.append(end_time - start_time)
        avg_time_taken.append(sum(time_taken) / 100)
    
    return avg_time_taken

def better_approach():
    list_of_time = check_performance([fun1, fun])
    apr1, apr2 = list_of_time[0], list_of_time[1]
    percent_apr2 = ((apr1 - apr2) / apr1) * 100
    
    if percent_apr2 < 0:
        print(f"Approach 2 is {-percent_apr2}% faster than approach 1")
    else:
        print(f"Approach 1 is {percent_apr2}% faster than approach 2")

better_approach()


