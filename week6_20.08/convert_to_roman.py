def rom(text, text_base):
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
	
	# Method to convert decimal to roman
	def dec_to_rom(text):
		text = int(text)
		values = sorted(roman_numerals.keys(), reverse = True)
		roman = ""
		for value in values:
			while text >= value:
				roman += roman_numerals[value]
				text -= value
		return roman

	# Method to convert binary to roman
	def bin_to_rom(text):
		roman = dec_to_rom(int(text, 2))
		return roman

	# Method to convert octal to roman
	def oct_to_rom(text):
		roman = dec_to_rom(int(text, 8))
		return roman

	# Method to convert hexadecimal to roman
	def hex_to_rom(text):
		roman = dec_to_rom(int(text, 16))
		return roman
	
	result = ""
	
	# Handling text bases converting a text into roman accordingly
	if text_base == 10:
		result = dec_to_rom(text)
	elif text_base == 2:
		result = bin_to_rom(text)
	elif text_base == 8:
		result = oct_to_rom(text)
	elif text_base == 16:
		result = hex_to_rom(text)
	else: 
		return "ValueError: Text base is not valid. Enter a valid text base."
	return result

# Inputs for text, text_base
text = input("Enter a number: ")
print("Text bases: ")
print("2 for binary")
print("8 for octal")
print("10 for decimal")
print("16 for hexadecimal")
text_base = int(input("Enter base of the number: "))

# Method call, print result
print(rom(text, text_base))
