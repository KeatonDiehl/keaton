# File: Homework 3

# 3: Print Functions

def say_goodbye(name):
	name == 'keaton'
	print("Goodbye,", name)


def circle_area(radius):
	# calculates the area of a circle
	pi = 3.14
	circle_area = radius * pi ** 2
	print (circle_area)

# 4: Return Functions

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b


# 5: Conditionals

def min_max(readings):
	# return the max and min values of temperature
	return (min(readings) , max(readings))
readings = [15, 14, 17, 20, 23, 28, 20]


def is_weekend(day):
	# Return true if the day is a weekend (6 or 7)
	return day == 6 or day == 7

def fuel_efficiency(distance, fuel_used):
	# Return the fuel efficiency based on distance traveled and fuel used
	return distance / fuel_used

def secret_code(n):
	# Encrypt data by moving the last digit to the front
	last = n % 10		# dividing by 10 and taking the remainder yields only the last digit
	rest = n // 10		# dividing by 10 and removing the remainder yields the rest of the integer
	return int(str(last) + str(rest))		# adds the two numbers together in reverse order as strings, then transforms to integers

# 6: Loops

def power_function(x, y):
	# raises x to the power of y using a for loop
	result = 1
	for i in range(y):
		result *= x
	return result

def for_max(lst):
	# finds the maximum value from a list of integers
	m = lst[0] 		# start with the first element as max
	for integer in lst:		# cycle through the list looking for a value greater than m
		if integer > m:
			m = integer

	return m
def for_min(lst):
	# finds the minimum value from a list of integers
	m = lst[0]
	for integer in lst:
		if integer < m:
			m = integer
	return m

def while_max(lst):
        # finds the maximum value from a list of integers using a while loop
        i = 1           # start the counter on the second element
        m = lst[0]              # assume the max is the first element
        while i < len(lst):             # while the counter falls within the range of numbers in the list
                if lst[i] > m:
                    m = lst[i]
                i += 1          # move to the next item in the list
        return m
def while_min(lst):
		# finds the minimum value from a list of integers using a while loop
		i = 1           # start the counter on the second element
		m = lst[0]              # assume the min is the first element
		while i < len(lst):             # while the counter falls within the range of numbers in the list
			if lst[i] < m:
				m = lst[i]
			i += 1			# move to the next item in the list
			return m
lst = [132, 1, 234, 2, 0]
print(while_min(lst))

def sum_digits(n):
	# finds the sum of the integers in a number n
	n = abs(n)		# accounts for negative numbers
	total = 0
	while n > 0:
		digit = n % 10		# get the last digit
		total += digit		# add the digit to the the running total
		n //= 10		# drop the last digit 
	return total
n = 37283

print ("The sum of the digits of", n, "is", sum_digits(n))