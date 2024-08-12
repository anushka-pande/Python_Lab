# this method works like builtin method for string when condition is 'False' and allows overlapping in while counting the occurance of substring in string when condition is 'True'
# Approach 1
def count_pattern1(string, substring, condition):
	count = 0
	i = 0
	while i < len(string):
		if string[i:i+len(substring)] == substring:
			count += 1
			if not condition:
				i += len(substring) - 1
		i += 1
	return count
	
# taking inputs of string, substrin and condition from user
string = input("Enter a String: ")
substring = input("Enter a Substring: ")
condition = input("Enter if you want to allow overlapping or not (True/False): ")

# converting string into boolean
condition = condition.lower() == "true"
result1 = count_pattern1(string, substring, condition)
print(result1)

# this method works like builtin method for string when condition is 'False' and allows overlapping in while counting the occurance of substring in string when condition is 'True'
# Approach 2
def count_pattern2(string, substring, condition, start = 0):
	if start > len(string) - len(substring):
		return 0
	
	if string[start: start + len(substring)] == substring:
		if condition:
			return 1 + count_pattern2(string, substring, condition, start + 1)
		else:
			return 1 + count_pattern2(string, substring, condition, start + len(substring))
	else:
		return count_pattern2(string, substring, condition, start + 1)

# taking inputs of string, substrin and condition from user
string = input("Enter a String: ")
substring = input("Enter a Substring: ")
condition = input("Enter if you want to allow overlapping or not (True/False): ")

# converting string into boolean
condition = condition.lower() == "true"
result2 = count_pattern2(string, substring, condition)
print(result2)


