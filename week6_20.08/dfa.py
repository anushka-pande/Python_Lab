alpha = {'a', 'b'}
def dfa_endswithb(text):
	final_states = {'q1'}
	result = q0(text)
	if result in final_states:
		return "Accepted."
	else:
		return "Rejected."


def q0(text):
	if len(text) > 0:
		symbol = text[0]
		if symbol in alpha:
			if symbol == 'b':
				return q1(text[1:])
			else:
				return q0(text[1:])
		else:
			return "Rejected."
	else:
		return "q0"


def q1(text):
	if len(text) > 0:
		symbol = text[0]
		if symbol in alpha:
			if symbol == 'a':
				return q0(text[1:])
			else:
				return q1(text[1:])
		else:
			return "Rejected."
	else:
		return "q1"


user_input_string = input("Enter a string: ")
dfa = dfa_endswithb(user_input_string)
print(dfa)
