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
	return "Valid"
	
print(check_validity("{<{>"))
