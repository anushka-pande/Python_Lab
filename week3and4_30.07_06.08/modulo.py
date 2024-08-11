# this method works like % operator

'''
for example - 

Enter a numerator: 10.0
Enter a denominator: -3
-2.0

'''

def modulo(n , d):
# n is numerator
# d is denominator
	if d == 0:
		return "ZeroDivisionError: integer division or modulo by zero"
	else:
		div = n // d
		mod = n - div * d
		return mod;
	
n = float(input("Enter a numerator: "))
d = float(input("Enter a denominator: "))
m = modulo(n, d)
print(m)

