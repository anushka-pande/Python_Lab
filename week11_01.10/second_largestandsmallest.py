def find_extremes(L):
	result = []
	valid_obj = (list, tuple, set)
	# Helper function to collect integers from the objects
	def collectInt(L):
		for item in L:
			if isinstance(item, int):
				result.append(item)
			elif isinstance(item, valid_obj):
				collectInt(item)
		return result
	unique_num = sorted(set(collectInt(L)))
	if len(unique_num) < 2:
		return None
	return unique_num[1], unique_num[-2]
print(find_extremes([58, 47, [20, 39, 0, 28], (37, 99), {21, 20, 10}, 45]))	
