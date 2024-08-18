def change_case(str, style):
	if style == "c":
		return "Your desired string is: " + upper_c(str)
	elif style == "s":
		return "Your desired string is: " + lower_s(str)
	elif style == "r":
		return "Your desired string is: " + swapcase_r(str)
	elif style == "z":
		return "Your desired string is: " + zigzag_z(str)
	else:
		return "Invalid case type."
	
def upper_c(str):
	result = ""
	for char in str:
		if ord('a') <= ord(char) <= ord('z'):
			result += chr(ord(char) - 32)
		else:
			result += char
	return result
	
def lower_s(str):
	result = ""
	for char in str:
		if ord('A') <= ord(char) <= ord('Z'):
			result += chr(ord(char) + 32)
		else:
			result += char
	return result
	
def swapcase_r(str):
	result = ""
	for char in str:
		if ord('A') <= ord(char) <= ord('Z'):
			result += chr(ord(char) + 32)
		elif ord('a') <= ord(char) <= ord('z'):
			result += chr(ord(char) - 32)
		else:
			result += char
	return result
	

def zigzag_z(str):
	result = ""
	if len(str) == 0:
		return result

	if ord('A') <= ord(str[0]) <= ord('Z'):
		start_with_upper = True
	elif ord('a') <= ord(str[0]) <= ord('z'):
		start_with_upper = False
	else:
		return str


	for i, char in enumerate(str):
		if start_with_upper:
			if i % 2 == 0:
				if ord('A') <= ord(char) <= ord('Z'):
					result += chr(ord(char) + 32)
				else:
					result += char
			else:
				if ord('a') <= ord(char) <= ord('z'):
					result += chr(ord(char) - 32)
				else:
					result += char
		else:
			if i % 2 == 0:
				if ord('a') <= ord(char) <= ord('z'):
					result += chr(ord(char) - 32)
				else:
					result += char
			else:
				if ord('A') <= ord(char) <= ord('Z'):
					result += chr(ord(char) + 32)
				else:
					result += char

	return result
	
user_input_str = input("Enter a string: ")

print("")

print(" Enter c for upper case string ")
print(" Enter s for lower case string  ")
print(" Enter r for swapped(reversed) case string ")
print(" Enter z for zigzagged case string ")

print("")

user_input_style = input("Enter a style symbol you want to choose: ")

f = change_case(user_input_str, user_input_style)
print("")
print(f)

#print(change_case("Abcd", "c"))
#print(change_case("Abcd", "s"))
#print(change_case("AbCd", "r"))
#print(change_case("Abcd", "z"))
#print(change_case("abcd", "z"))
#print(change_case("Abcd", "a"))
