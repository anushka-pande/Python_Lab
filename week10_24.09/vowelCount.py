vowels = set('aeiouAEIOU')
def count_vowels_in_string(s):
	vowel_count = {v: 0 for v in vowels}
	for char in s:
		if char in vowels:
			vowel_count[char] += 1
	return vowel_count

def are_vowel_count_equal(vowel_count):
	counts = []
	for count in vowel_count.values():
		if count > 0:
			counts.append(count)
	if not counts:
		return True
	first_count = counts[0]
	return all(c == first_count for c in counts)

def count_text(L):
	valid_str_count = 0
	valid_objects = {list, tuple, set}
	
	for item in L:
		type_of_item = type(item)
		if type_of_item == str:
			vowel_count = count_vowels_in_string(item)
			valid_str_count += are_vowel_count_equal(vowel_count)
		if type_of_item in valid_objects:
			valid_str_count += count_text(list(item))
	
	return valid_str_count
	
L = ["abcde", "Abcde", ("hello", "aero"), ["aAeEiIoOuU", {"ACE", "IO"}]]
print(count_text(L))
