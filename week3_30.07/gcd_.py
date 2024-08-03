import math;
def gcd(a, b):
	return math.gcd(a, b);
	
def gcd_multiple_num(*num):
	result = num[0]
	for n in num[1:]:
		result = gcd(result, n)
	return result;	
	
user_input = input("Enter numbers separates by spaces: ")
numbers = list(map(int, user_input.split()))

result = gcd_multiple_num(*numbers);
print("The GCD of numbers is: ", result)
