# Homework 4

# 3: Lists
''''''
# 3.1
favorite_foods = ['sushi', 'blueberries', 'chicken', 'fish', 'pasta']

print(favorite_foods[1])
print(favorite_foods[-1])

favorite_foods.append('salad')
print(favorite_foods)

favorite_foods.insert(0, 'apple')
print(favorite_foods)

del favorite_foods[2]
print(favorite_foods)

print(len(favorite_foods))

for i in favorite_foods:
    print(i.upper())

first_last_foods = favorite_foods[1:5:3]
print(first_last_foods)


if i in favorite_foods is 'potato':
    print('A Potato!')
else:
    print('No potato!')

# 3.2
numbers = list(range(21))
print(numbers)

def get_first_15(numbers):      # returns the first 15 elements
    return numbers[0:15]
print(get_first_15(numbers))        

first_15 = get_first_15(numbers)
def get_every_5th(first_15):     # returns every 5th element from get_first_15(numbers)
    return first_15[::5]
print(get_every_5th(first_15))

every_5th = get_every_5th(first_15)
def reverse_and_stride(every_5th):      # reverses and returns every third element from get_every_5th(first_15)
    return every_5th[::-3]
print(reverse_and_stride(every_5th))


# 3.3
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])

print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)


def sum_nested(numbers):
    tracker = 0           # Forgot to go by row
    for row in numbers:  
        for number in row:
            tracker += number
    return tracker
print(sum_nested(numbers))
'''
Error: 
TypeError: unsupported operand type(s) for +=: 'int' and 'list'
I origionally wrote the code below, which neglected to go row by row, and instead skipped straight to looking for numbers
def sum_nested(numbers):
     tracker = 0        
     for number in numbers:
             tracker += number
     return tracker
print(sum_nested(numbers))
'''

# 3.4
def matrix_5x5():       # Being perfectly honest, I had to go watch a youtube video to learn how to make a matrix
    matrix = []
    count = 1
    for i in range(5):
        row = []
        for i in range(5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix
print(matrix_5x5())
'''
def multiples_of_3(matrix_5x5):         # Worked on this forever, genuinely dont know what to do. I'll submit the homework with this unsolved and will work on it later
    new_matrix = []
    for row in matrix_5x5:              
        new_row = []                    # Didn't think to start the matrix as empty and then add into it
        for number in row:
            if number % 3 == 0:
                new_row.append('?')
            else:                       # Didn't return to a new row after the :
                new_row.append(number)
        new_matrix.append(new_row)      # Forgot to append the new rows into the new matrix
    return new_matrix
print(multiples_of_3(matrix_5x5))

TypeError: 'function' object is not iterable
I genuinely have no idea how to fix this. ChatGPT and youtube havent helped. I think i'm close, and ive fixed multiple bugs on this one problem, but this one won't go away :(
The line it quotes as having an error is 102, but that should be itterable since matrix_5x5 has three rows
'''


# def sum_numbers(multiples_of_3):        # Won't work without multiples_of_3, so i'll check on this after solving the bug above
#     sum = 0
#     for row in multiples_of_3:
#         for item in row:   
#             if item in row is '?':
#                 sum += 0
#         else:
#             sum += item
#     return sum
# print(sum_numbers(multiples_of_3))


# 4

# 4.1
ages = {
    'Katie': 30,
    'Mariam': 42,
    'Safia': 25,
    'Mira': 48
}

print(ages['Katie'])

ages['Mariam'] = 100
print(ages['Mariam'])

ages['Milana'] = 52
print(ages)

del ages['Mariam']
print(ages)

for name, age in ages.items():
    print(name, 'is', age)
'''
Error: 
ValueError: too many values to unpack (expected 2)
I origionally wrote the code below, which didn't use .items, that allows the funciton to consider multiple variable
for name, age in ages:
    print(name, 'is', age)
'''