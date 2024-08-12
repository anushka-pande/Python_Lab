# this method prints pattern with '*' and the entered number in middle

'''
for example - 
for n = 1             

    *                        
  * 1 *
* * * * * 

for n = 2

      *
    *   *
  *   2   *
    *   *
* * * * * * * 
* * * * * * *

and so on...
'''

def print_pattern1(n):       
	# checks if the number is positive integer or not
	# n is size or number of lines in the pattern
	if (n < 1):
		return "Enter a number greater than or equal to 1";
	elif(type(n) != int):                     # 1.0, 2.0, 8.0 etc float integers are valid
		n_str = str(n)
		if '.' in n_str:
			integer_part, decimal_part = n_str.split('.')
			if int(decimal_part) != 0:
				return "Enter positive integer greater than or equal to 1"
			else:                         
			# prints the pattern
				n = int(n)
				result = []
				# for upper part (hollow pyramid) with number
				inner_space = 3;
				for i in range(1, n + 2):
					if (i == 1):
						result.append(" " * (2 * n + 2) + "*" + "")
					elif (i == 2):
						if(n == 1):
							half_inner_space = (inner_space - 1) // 2;
							result.append(" " * ((2 * n + 4) - 2 * i) + "*" + " " * (half_inner_space) + "1"+ " " * (half_inner_space) + "*" + "")				
						else:
							result.append(" " * ((2 * n + 4) - 2 * i) + "*" + " " * (inner_space) + "*" + "")
					elif (i > 2) and (i < n + 1):
						inner_space += 4;
						result.append(" " * ((2 * n + 4) - 2 * i) + "*" + " " * (inner_space) + "*" + "")
					elif (i == n + 1):
						inner_space += 4;
						half_inner_space = (inner_space - 1) // 2;
						result.append(" " * ((2 * n + 4) - 2 * i) + "*" + " " * (half_inner_space) + str(n) + " " * (half_inner_space) + "*" + "")
				# for middle part (inverted hollow pyramid)
				if(n > 1):
					inner_space = 4 * (n - 1) - 1;
					for i in range(1, n):
						result.append(" " * (2 + 2 * i) + "*" + " " * (inner_space) + "*" + "")
						inner_space -= 4;
				# for lower part
				for i in range(1, n + 1):
					result.append("* " * (3 * n + 3 - n)+ "")
					
				return "\n".join(result) + "\n";


# input for the number of lines
n = float(input("Enter a number: "))
print()
# method call to print the pattern
p = print_pattern1(n)
print(p);



# this method prints the pattern with '+' and only one '-' at the bottom

'''
for example - 
for n = 1

  +
+   +
  -

for n = 2

    +
  +   +
+       +
  +   +
    -

'''

def print_pattern2(n):
	# n is size or number of lines in the pattern
	# for upper part
	inner_spaces = 3;
	for i in range(1, n + 2):
		if (i == 1):
			print(" " * (2 * n) + "+")
		elif (i > 1):
			print(" " * ((2 * n + 2) - 2 * i) + "+" + " " * (inner_spaces) + "+")
			inner_spaces += 4;
			
	# for lower part
	inner_spaces = 4 * (n - 1) - 1;
	for i in range(1, n + 1):
		if(i < n):
			print(" " * (2 * i) + "+" + " " * (inner_spaces) + "+")
			inner_spaces -= 4
		elif(i == n):
			print(" " * (2 * n) + "-")
	
# input for the number of lines		
user_input = int(input("Enter a number: "))
print()	
# method call to print the pattern
print_pattern2(user_input)
print()
			
# this method prints the pattern with '+' in upper hollow pyramid and with '-' in lower inverted hollow pyramid

'''
for example - 
for n = 1

  +
+   +
  -

for n = 2

    +
  +   +
+       +
  -   -
    -

'''		

def print_pattern3(n):
	# for upper part
	inner_spaces = 3;
	for i in range(1, n + 2):
		if (i == 1):
			print(" " * (2 * n) + "+")
		elif (i > 1):
			print(" " * ((2 * n + 2) - 2 * i) + "+" + " " * (inner_spaces) + "+")
			inner_spaces += 4;
			
	# for lower part
	inner_spaces = 4 * (n - 1) - 1;
	for i in range(1, n + 1):
		if(i < n):
			print(" " * (2 * i) + "-" + " " * (inner_spaces) + "-")
			inner_spaces -= 4
		elif(i == n):
			print(" " * (2 * n) + "-")
			
			
# input for the number of lines	
user_input = int(input("Enter a number: "))
print()	
# method call to print the pattern
print_pattern3(user_input)
print()

			
			
# this method works like % operator

'''
for example - 

Enter a numerator: 10.0
Enter a denominator: -3
-2.0

'''

def modulo(n , d):
# n is numerator
# d is denominator
	if d == 0:
		return "ZeroDivisionError: integer division or modulo by zero"
	else:
		div = n // d
		mod = n - div * d
		return mod;
	
n = float(input("Enter a numerator: "))
d = float(input("Enter a denominator: "))
m = modulo(n, d)
print(m)

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


