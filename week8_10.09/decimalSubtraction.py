# Dictionary that maps each string character to intger
str_to_int_dict = {
		'0' : 0,
		'1' : 1,
		'2' : 2,
		'3' : 3,
		'4' : 4,
		'5' : 5,
		'6' : 6,
		'7' : 7,
		'8' : 8,
		'9' : 9
}

# Check if the number is valid or not
def isValidDecimal(num):
	if num[0] == '-':
		num = num[1:]
	for i in num:
		if i not in str_to_int_dict:
			return False
	return True

# Converts string text into int
def str_to_int(text):
	# Check Validity
	if not isValidDecimal(text):
		return "Invalid Decimal number.Enter a valid number which contains digits from 0 to 9."
		
	# Check if the number is negative
	isNegative = False
	if text[0] == '-':
		isNegative = True
		text = text[1:]
	# Handle different lengths of the text
	length = len(text)
	if length == 0:
		return 0
	elif length == 1:
		return str_to_int_dict[text]
	else:
		return str_to_int_dict[text[0]] * pow(10, length - 1) + str_to_int(text[1:])
	# Return num with '-' if it is negative
	if isNegative:
		return -num
	else:
		return num

# Perfoms decimal subtraction digit-by-digit with borrow
def subtraction(num1, num2):
	# Assign result (an empty list), borrow (= 0) and len1 (for num1) and len2 (for num2)
	result = []
	borrow = 0
	len1, len2 = len(num1), len(num2)
	
	# Add leading 0s for a number whose length is less than the other
	if len1 > len2:
		num2 = num2.zfill(len1)
	elif len1 < len2:
		num1 = num1.zfill(len2)
	
	# Handle a case where num1, num2 and borrow all are 0
	if num1 == "0" and num2 == "0" and borrow == 0:
		return 0
	
	# 'For loop' to perform digit-by-digit subtraction and save result
	for i in range(len(num1) - 1, -1, -1):
		digit1 = str_to_int(num1[i])
		digit2 = str_to_int(num2[i]) + borrow
		if digit1 < digit2:
			digit1 += 10
			borrow = 1
		else:
			borrow = 0
		result.append(str(digit1 - digit2))
	result = ''.join(result[::-1]).lstrip('0')
	
	# Return result in int form
	if not result:
		result = '0'
	return str_to_int(result)
	
# Perform decimal addition digit-by-digit with carry
def decimalAddition(num1, num2):
	# Assign result (an empty list), carry (= 0) and len1 (for num1) and len2 (for num2)
	result = []
	carry = 0
	len1, len2 = len(num1), len(num2)
	
	# Add leading 0s for a number whose length is less than the other
	if len1 > len2:
		num2 = num2.zfill(len1)
	elif len1 < len2:
		num1 = num1.zfill(len2)
	
	# Handle a case where num1, num2 and carry all are 0
	if num1 == "0" and num2 == "0" and carry == 0:
		return 0
	
	# 'For loop' to perform digit-by-digit addition and save result and modify carry
	for i in range(len(num1) - 1, -1, -1):
		digit1 = str_to_int(num1[i])
		digit2 = str_to_int(num2[i])
		sum_digits = digit1 + digit2 + carry
		result.append(str(sum_digits % 10))
		carry = sum_digits // 10
		
	# Append final carry to the result if it is greater than 0
	if carry > 0:
		result.append(str(carry))
	
	# Return result in int form
	return str_to_int(''.join(result[::-1]))

# Contains if-elif block for edge cases where any one or both or none of the numbers can be negative
def decimalSubtraction(num1, num2):
	# Check Validity of both numbers
	if not (isValidDecimal(num1) and isValidDecimal(num2)):
		return "Invalid Decimal number.Enter a valid number which contains digits from 0 to 9."
	
	# Convert num1 and num2 strings to int
	n1 = str_to_int(num1)
	n2 = str_to_int(num2)
	
	# If numbers are equal
	if n1 == n2:
		return 0
		
	# Check if both or none or any of the numbers is negative
	if '-' in num1 and '-' not in num2:
		num1 = num1[1:]
		return -decimalAddition(num1, num2)
	elif '-' not in num1 and '-' in num2:
		num2 = num2[1:]
		return decimalAddition(num1, num2)
	elif '-' in num1 and '-' in num2:
		num1 = num1[1:]
		num2 = num2[1:]
		return decimalSubtraction(num2, num1)
	
	# Check if n1 is greater than n2 
	if n1 < n2:
		# If n1 > n2, swap and perform subtraction
		return -subtraction(num2, num1)
	else:
		return subtraction(num1, num2)
	
# Input section
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Method call
if not (isValidDecimal(num1) and isValidDecimal(num2)):
	print(decimalSubtraction(num1, num2))
else:
	print(f"Decimal Subtraction of ({num1}) - ({num2}) is {decimalSubtraction(num1, num2)}")

