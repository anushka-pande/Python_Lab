set_of_brackets = {'(', '{', '[', '<', '>', ']', '}', ')'}
pairs = {
	'(' : ')',
	'[' : ']',
	'{' : '}',
	'<' : '>'
}
def check_validity(text):
	stack = []
	for symbol in text:
		if symbol in set_of_brackets:
			if symbol in pairs:
				stack.append(symbol)
			else:
				if stack:
					if pairs[stack[-1]] == symbol:
						stack.pop()
					else:
						return f"Invalid: Mismatched brakcet '{stack[-1]}' and '{symbol}'"
				else:
					return f"Invalid: Unmatched closing bracket '{symbol}'"
		else:
			return "Invalid: Non-bracket character '{symbol}'"
	
	if stack:
		return f"Invalid: Unmatched opening bracket '{stack[-1]}'"
	return "Valid."
	
def get_valid_invalid_text_count(texts_list):
	valid_count = 0
	invalid_count = 0
	
	for item in texts_list:
		if isinstance(item, list):
			v_count, i_count = get_valid_invalid_text_count(item)
			valid_count += v_count
			invalid_count += i_count
		if isinstance(item, tuple) or isinstance(item, set):
			v_count, i_count = get_valid_invalid_text_count(list(item))
			valid_count += v_count
			invalid_count += i_count
		if isinstance(item, str):
			result = check_validity(item)
			if result == "Valid.":
				valid_count += 1
			else:
				invalid_count += 1
			
	return valid_count, invalid_count

print(get_valid_invalid_text_count(['[{(', [45, ("()"),]]))
