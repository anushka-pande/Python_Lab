def isPalindrome(text):
	return text == text[::-1]
	
	
def fun(L):
	count = 0
	set_of_valid_obj = {list, tuple, set}
	set_of_count = {str, int}
	
	for item in L:
		type_of_item = type(item)
		if type_of_item in set_of_count:
			if type_of_item == int:
				item = str(item)
			if len(item) % 6 == 3:
				count += isPalindrome(item)
		elif type_of_item in set_of_valid_obj:
			count += fun(item)
			
	return count
	
L = eval(input("Enter a list object containing strings, integers, lists, tuples, or sets: "))
print(f"NUmber of valid palindromes: {fun(L)}")
