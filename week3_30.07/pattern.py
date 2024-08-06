def print_pattern(n):
	if (n < 1):
		return "Enter a number greater than or equal to 1";
	elif(type(n) != int):
		n_str = str(n)
		if '.' in n_str:
			integer_part, decimal_part = n_str.split('.')
			if int(decimal_part) != 0:
				return "Enter positive integer greater than or equal to 1"
			else:
				n = int(n)
				result = []
				# for upper part (hollow pyramid) with number
				inner_space = 3;
				for i in range(1, n + 2):
					if (i == 1):
						result.append(" " * (2 * n + 2) + "*" + "")
					elif (i == 2):
						if(n == 1):
							half_inner_space = (inner_space - 1) // 2;
							result.append(" " * ((2 * n + 4) - 2 * i) + "*" + " " * (half_inner_space) + "1"+ " " * (half_inner_space) + "*" + "")				
						else:
							result.append(" " * ((2 * n + 4) - 2 * i) + "*" + " " * (inner_space) + "*" + "")
					elif (i > 2) and (i < n + 1):
						inner_space += 4;
						result.append(" " * ((2 * n + 4) - 2 * i) + "*" + " " * (inner_space) + "*" + "")
					elif (i == n + 1):
						inner_space += 4;
						half_inner_space = (inner_space - 1) // 2;
						result.append(" " * ((2 * n + 4) - 2 * i) + "*" + " " * (half_inner_space) + str(n) + " " * (half_inner_space) + "*" + "")
				# for middle part (inverted hollow pyramid)
				if(n > 1):
					inner_space = 4 * (n - 1) - 1;
					for i in range(1, n):
						result.append(" " * (2 + 2 * i) + "*" + " " * (inner_space) + "*" + "")
						inner_space -= 4;
				# for lower part
				for i in range(1, n + 1):
					result.append("* " * (3 * n + 3 - n)+ "")
					
				return "\n".join(result) + "\n";

n = float(input("Enter a number: "))
print()
p = print_pattern(n)
print(p);
