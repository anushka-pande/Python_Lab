def slice(object, slicing_parameter):
	# Return object immediately if it is empty
	if isinstance(object, str) and len(object) == 0:
		return "'" + "'"
	elif isinstance(object, list) and len(object) == 0:
		return []
	elif isinstance(object, tuple) and len(object) == 0:
		return tuple()
	
	
	# Handling different lengths of the slicing parameters list
	if len(slicing_parameter) == 0:
		slicing_parameter = [None, None, None]
	elif len(slicing_parameter) == 1:
		slicing_parameter = [slicing_parameter[0], None, None]
	elif len(slicing_parameter) == 2:
		slicing_parameter = [slicing_parameter[0], slicing_parameter[1], None]
	elif len(slicing_parameter) == 3:
		slicing_parameter = [slicing_parameter[0], slicing_parameter[1], slicing_parameter[2]]
	else:
		return "ValueError: too many values to unpack. You can pass atmost 3 values."		

	start, stop, step = slicing_parameter
	
	if step is None:
		# default value of step
		step = 1
	elif step == 0:
		return "ValueError: Step must not be zero."
	
	# checking if start is None or not
	if start is None:
		# checking if step is positive or negative
		if step > 0:		
			start = 0
		else:
			start = len(object) - 1
	elif start < 0:
		start += len(object)

	# checking if stop is None or not
	if stop is None:
		# checking if step is positive or negative
		if step > 0:
			stop = len(object)
		else:
			stop = -1
	elif stop < 0:
		stop += len(object)
	elif stop > len(object):
		stop = len(object)
	
	result = []
	for i in range(start, stop, step):
		if len(object) == 0:
			return result
		else:
			result.append(object[i])

	if isinstance(object, str):
		return "'" + ''.join(result) + "'"
	if isinstance(object, tuple):
		return tuple(result)
	return result
	
user_input_object = eval(input("Enter a object which you want to slice: "))
user_input_slicing_parameter = eval(input("Enter a slicing parameter in a list format [start, stop, step]: "))

s = slice(user_input_object, user_input_slicing_parameter)
print(s)
