# Funtion to calculate the weekday of a given date
def get_week_day(date, month, year):
	# Calculate the day of the week for a given date using zeller's congruence
	if month == 1 :
		month = 13
		year = year - 1
	if month == 2 :
		month = 14
		year = year - 1
	y_last = year%100
	y_first = year//100

	day = (date + ((13 * (month + 1)) // 5) + y_last + (y_last // 4) + (y_first // 4) + 5 * y_first)
	day = day % 7
	days = [
		"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
	]
	return days[day]

# Function to get the rows and columns for the specified layout
def get_rows_columns(layout):
	# Retturn the rows and columns for a given layout.
	layouts = ["1x12" , "2x6" , "3x4", "4x3", "6x2" , "12x1"]
	rows_columns = [[1,12] , [2,6], [3,4], [4,3], [6,2] , [12,1]]
	for i in range(0,6):
		if layout == layouts[i]:
			return rows_columns[i]

# Function to check if the given layout is valid
def is_valid_layout(layout):
	# Return true if the layout is valid
	valid_layouts = ["1x12" , "2x6" , "3x4", "4x3", "6x2" , "12x1"]
	for i in range(0,6):
		if layout == valid_layouts[i]:
			return True
	return False

# Function to check if a year is a leap year
def is_leap_year(year):
	# Return true if the year is a leao year, False otherwise
	if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
		return True
	return False

# Function to get the maximum days in a given month
def get_max_days_in_month(month, year):
	# Return the max no. of days in month
	months = [
		"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
	]
	days = [
		31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
	]
	if month == "February" and is_leap_year(year):
		return 29
	return int(days[months.index(month)])

current_month = 0
month_number = []
month = 1
layouts = ["1x12" , "2x6" , "3x4", "4x3", "6x2" , "12x1"]
abbreviated_days = "  Su Mo Tu We Th Fr Sa  "
months = [
	"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

# Functin to print the year header
def print_year_header(sep, year, layout):
	rows_columns = get_rows_columns(layout)
	spaces = 24 * rows_columns[1] + len(sep) * (rows_columns[1] - 1) - len(str(year))
	print(sep + sep * ((24 * rows_columns[1] // len(sep)) + (rows_columns[1] - 1)) + sep)
	print(sep + " " * len(sep) * ((24 * rows_columns[1] // len(sep)) + (rows_columns[1] - 1)) + sep)
	print(sep + " " * (spaces // 2) + str(year) +  " " * (spaces - (spaces // 2)) + sep)
	print(sep + " " * len(sep) * ((24 * rows_columns[1] // len(sep)) + (rows_columns[1] - 1)) + sep)
	print(sep + sep * ((24 * rows_columns[1] // len(sep)) + (rows_columns[1] - 1)) + sep)


# FUnction to print the month and week headers
def print_month_and_week_header(sep, layout):
	# Print the month and weekdays header
	global current_month
	months = [
	"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
	]
	rows_columns = get_rows_columns(layout)
	column_count = 1
	for i in range (0, rows_columns[1]):
		print(sep * column_count + " " * 24 + sep, end="")
		if i == 0:
		    column_count =0
	print("")
	column_count = 1
	for a in range(0, rows_columns[1]):
		length_of_month = len(months[current_month])
		padding_left = (24 - length_of_month) // 2
		padding_right = 24 - padding_left - length_of_month
		print(sep * column_count + " " * padding_left + months[current_month] + " " * padding_right + sep, end="")
		if a == 0:
		    column_count= 0
		current_month = current_month + 1
	print("")
	column_count = 1
	for a in range(0, rows_columns[1]) :
		print(sep * column_count + abbreviated_days + sep, end="")
		if a == 0 :
		    column_count = 0;
	print("")

def print_dates(symbol, year, layout):
	dates = []
	global month
	sep_boolean = True
	spaces = []
	max_days_in_month_number = []
	months = [
		"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
	]
	rows_columns = get_rows_columns(layout)
	days = [
		"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
	]
	for i in range(rows_columns[1]):
		max_days_in_month_number.append(get_max_days_in_month(months[i + month - 1], year))
		spaces.append(days.index(get_week_day(1, i + month, year)))
		dates.append(1)
	while any(max_days_in_month_number):
		for i in range(rows_columns[1]):
			if max_days_in_month_number[i] != 0:
				if i == 0:
					sep_boolean = True
				else:
					sep_boolean = False
				print(sep * sep_boolean + "  " + "   " * spaces[i], end="")
				for k in range(7 - spaces[i]):
					day_str = str(dates[i]).rjust(2)
					print(day_str + " ", end="")
					dates[i] += 1
					if dates[i] > max_days_in_month_number[i]:
						max_days_in_month_number[i] = 0
						print(" " * ((6 - k) * 3), end="")
						break
				sep_boolean = False	# Reset for next iteration
				print(" " + sep, end="")
				spaces[i] = 0
			else:
				if i == 0 :
					print(sep + " " * 24 + sep, end="")
				else :
					print (" " * 24 + sep, end="")
		print("")
		sep_boolean = False
	for i in range (0, rows_columns[1]):
		if i == 0:
			print(sep + " " * 24 + sep, end="")
		else:
			print(" " * 24 + sep, end="")
	print("")
	print(sep + sep * ((24 * rows_columns[1] // len(sep)) + (rows_columns[1] - 1)) + sep)
	month += rows_columns[1]

# Welcome message
print("Welcome to the Yearly Calendar Generator!!")
print("This program allows you to generate a calendar for any year in various layouts.\n")
# Year input
year = int(input("Enter The Year between 1 to 9999: "))
print(f"Available layouts are: {[layouts[i] for i in range(len(layouts))]}")
if(year <= 0 or year > 9999):
	print("Invalid year! Please enter a year between 1 and 9999.")
else :
	layout = input("Enter layout: ")
	if is_valid_layout(layout) :
		sep = input("Enter a separation symbol (max 4 characters): ")
		if len(sep) <= 4 :
		        rows_columns = get_rows_columns(layout)
		        print_year_header(sep, year, layout)
		        for i in range(0, rows_columns[0]):
		                print_month_and_week_header(sep, layout)
		                print_dates(sep, year, layout)
		else :
		        print("Invalid symbol! Symbol length must not exceed 4 characters.")
	else :
		print("Invalid layout! Please choose from predefined layouts.")
                
# Exit message
print("\nThank you for using the Yearly Calendar Generator!")


