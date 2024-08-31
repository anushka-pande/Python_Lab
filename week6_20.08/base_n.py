def base(text, text_base, output_base):
	# Dictionary for roman numerals to integer conversion
	roman_numerals = {
		1 : 'I',
		4 : 'IV',
		5 : 'V',
		9 : 'IX',
		10 : 'X',
		40 : 'XL',
		50 : 'L',
		90 : 'XC',
		100 : 'C',
		400 : 'CD',
		500 : 'D',
		900 : 'CM',
		1000 : 'M'
	}
	# Dictionary for integer to roman numeral conversion
	roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Method to convert a text roman to decimal
	def romanToDec(text):
		total = 0
		prev_value = 0

		for char in reversed(text):
			value = roman_to_int[char]
			if value >= prev_value:
				total += value
			else:
				total -= value
			prev_value = value
		return total
	
	# Method to convert a tetx form decimal to roman
	def decToRoman(text):
		values = sorted(roman_numerals.keys(), reverse = True)
		roman = ""
		for value in values:
			while text >= value:
				roman += roman_numerals[value]
				text -= value
		return roman
	
	# Method to convert a text from decimal to any other base
	def convertFromDec(text, output_base):
		result = ""
		text = int(text)
		while text != 0:
			text, remainder = divmod(text, output_base)
			if remainder < 10:
				result = str(remainder) + result
			else:
				result = chr(remainder - 10 + ord('A')) + result
		return result
			
	# Method to convert a text from any other base to decimal	
	def convertToDec(text, text_base):
		result = 0
		text = text[::-1]
		for i, digit in enumerate(text):
			if '0' <= digit <= '9':
				num = ord(digit) - ord('0')
				result += num * (text_base ** i)
			else:
				num = ord(digit) - ord('A') + 10
				result += num * (text_base ** i)
		return str(result)
		
		
	# Method to check if the base is valid or not
	def validate_base(base):
		if base == 'R' or base == 'r':
			return True
		if isinstance(base, int) and 2 <= base <= 36:
			return True
		return False
	
	# Handling Roman numeral base
	if text_base in ['R', 'r']:
		text = romanToDec(text)
		text_base = 10
	else:
		if not validate_base(text_base):
			return "Invalid text_base"
	# Converting text into string
	text = str(text)
		
	# Handling Base prfixes
	if text.startswith(('0x','0X')):
		text = text[2:]
		text_base = 16
	elif text.startswith(('0b','0B')):
		text = text[2:]
		text_base = 2
	elif text.startswith(('0o', '0O')):
		text = text[2:]
		text_base = 8
	
	# Converting the text to Decimal first
	if text_base != 10:
		if not validate_base(text_base):
			return "Invalid text_base"
		text = convertToDec(text, text_base)
	
	# Converting decimal to the desired output base or roman numerals
	if output_base in ['R', 'r']:
		return decToRoman(int(text))
	else:
		if not validate_base(output_base):
			return "Invalid output_base"
		return convertFromDec(text, output_base)

# Inputs for text, text_base, output_base
text = input("Enter a text to convert: ")
text_base = input("Enter the base of the text (For example - 2, 9, 10, 25, 36, 'R' or 'r' for roman): ")
output_base = input("Enter the output base (For example - 2, 9, 10, 25, 36, 'R' or 'r' for roman): ")

# Handling the text_base and output_base if any of it is digit
if text_base.isdigit():
	text_base = int(text_base)
if output_base.isdigit():
	output_base = int(output_base)
	
# Method call, print result
print(base(text, text_base, output_base))
