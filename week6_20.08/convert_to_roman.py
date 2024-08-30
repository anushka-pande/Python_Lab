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

def rom(text, text_base):
	result = ""
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

def dec_to_rom(text):
	text = int(text)
	values = sorted(roman_numerals.keys(), reverse = True)
	roman = ""
	for value in values:
		while text >= value:
				roman += roman_numerals[value]
				text -= value
	return roman
	
def bin_to_rom(text):
	roman = dec_to_rom(int(text, 2))
	return roman
	
def oct_to_rom(text):
	roman = dec_to_rom(int(text, 8))
	return roman
	
def hex_to_rom(text):
	roman = dec_to_rom(int(text, 16))
	return roman

'''
print(rom("3578", 10))		# output: MMMDLXXVIII
print(rom("1010", 2))		# output: X
print(rom("0b1010", 2))		# output: X
print(rom("0B1010", 2))		# output: X
print(rom("3577", 8))		# output: MCMXIX
print(rom("0o3577", 8))		# output: MCMXIX
print(rom("0O3577", 8))		# output: MCMXIX
print(rom("A82", 16))		# output: MMDCXC
print(rom("0xA82", 16))		# output: MMDCXC
print(rom("0XA82", 16))		# output: MMDCXC
print(rom("A82", 15))		# output: ValueError: Text base is not valid. Enter a valid text base.
'''

input_text = input("Enter a number: ")
print("Text bases: ")
print("2 for binary")
print("8 for octal")
print("10 for decimal")
print("16 for hexadecimal")
input_text_base = int(input("Enter base of the number: "))

print(rom(input_text, input_text_base))
