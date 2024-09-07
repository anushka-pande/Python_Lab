valid_digits = {'1', '0'}

# Checks if the number is valid binary or not
def isValidBinary(num):
	if num.startswith('-'):
		num = num[1:]
	for i in num:
		if i not in valid_digits:
			return False
	return True
		
# Performs Binary Addition of two binary numbers
def binaryAddition(a, b):
	a = "".join(reversed(a))
	b = "".join(reversed(b))

	max_len = max(len(a), len(b))
	a = a.ljust(max_len, "0")
	b = b.ljust(max_len, "0")

	result = ""
	carry = 0

	for i in range(max_len):
		total = carry + int(a[i]) + int(b[i])
		if total == 0 or total == 1:
			result = str(total) + result
			carry = 0
		elif total == 2:
			result = "0" + result
			carry = 1
		else:  
			result = "1" + result
			carry = 1

	if carry:
		result = '1' + result

	return result
	
# Inverts the bits - 1's complement of a number
def invertBits(binary):
	inverted_bits = ""
	for bit in binary:
		if bit == '0':
			inverted_bits += '1'
		else:
			inverted_bits += '0'
	return inverted_bits
			
# Includes the loops for checking the nature of number
def binarySubtraciton(a, b):
	# Check Validation for strings starting with '0b' or '-0b'
	a = a.lower()
	b = b.lower()

	if a.startswith("-0b"):
		a = "-" + a[3:]
	elif a.startswith("0b"):
		a = a[2:]

	if b.startswith("-0b"):
		b = "-" + b[3:]
	elif b.startswith("0b"):
		b = b[2:]

	# Check if any of a or b is negative or both are negative or both are posititve	
	if "-" in a and "-" in b:
		a = a[1:]
		b = b[1:]
		a, b = b, a
		if isValidBinary(a) and isValidBinary(b):
			return subtraction(a, b)
		else:
			return "ValueError: Invalid Binary String.Binary string must contain 0s and 1s only."
	elif "-" in a:
		a = a[1:]
		if isValidBinary(a) and isValidBinary(b):
			return "-" + binaryAddition(a, b)
		else:
			return "ValueError: Invalid Binary String.Binary string must contain 0s and 1s only."
	elif "-" in b:
		b = b[1:]
		if isValidBinary(a) and isValidBinary(b):
			return binaryAddition(a, b)
		else:
			return "ValueError: Invalid Binary String.Binary string must contain 0s and 1s only."
	else:
		if isValidBinary(a) and isValidBinary(b):
			return subtraction(a, b)
		else:
			return "ValueError: Invalid Binary String.Binary string must contain 0s and 1s only."

# Supportive method, Performs binary subtraction using two's complement method
def subtraction(num1, num2):
	max_len = max(len(num1), len(num2))
	num1 = num1.rjust(max_len, '0')
	num2 = num2.rjust(max_len, '0')

	num2_compliment = invertBits(num2)
	addition_of_compliment = binaryAddition(num1, num2_compliment)

	if len(addition_of_compliment) == len(num1):
		return "-" + invertBits(addition_of_compliment)
	else:
		result = addition_of_compliment[1:]
		result = binaryAddition(result, "1")
		return result
	
a = input("Enter first binary number: ")
b = input("Enter second binary number: ")
if not (isValidBinary(a) and isValidBinary(b)): 
	print(binarySubtraciton(a, b))
else:
	print(f"Subtration of {a} - {b} in binary: {binarySubtraciton(a, b)}")

