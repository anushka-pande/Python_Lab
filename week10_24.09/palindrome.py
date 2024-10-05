def isPalindrome(text):
	return text == text[::-1]
	
	
def fun(L):
	count = 0
	set_of_valid_obj = {list, tuple, set}
	set_of_count = {str, int}
	
	for item in L:
		if type(item) in set_of_count:
			if type(item) == int:
				item = str(item)
			if len(item) % 6 == 3 and isPalindrome(item):
				count += 1
		elif type(item) in set_of_valid_obj:
			count += fun(list(item))
			
	return count
	
L = eval(input("Enter a list object containing strings, integers, lists, tuples, or sets: "))
print(f"Number of valid palindromes: {fun(L)}")
