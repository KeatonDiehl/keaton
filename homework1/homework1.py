# File: homework1.py

# --- Variables and Data Types ---



a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a floating-point number, a rational number

c = 3j
print(c)
print(type(c)) # c is a complex number, with an imaginary part of j

d = "hello"
print(d)
print(type(d)) # d is a string, a set of letters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a set of numbers/letters

f = {"name": "Ellen," "favorite fruit," "strawberry"}
print(f)
print(type(f)) # f is a dictionary, representing an unordered collection of key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an immutable sequences of values

h = ["apple", "bannana", "strawberry"]
print(h)
print(type(h)) # h is a list, an ordered collection of items

i = True
print(i)
print(type(i)) # i is boolean, a data type that is either true or false

j = False
print(j)
print(type(j)) # j is boolean, a data type that is either true or false

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, an ordered collection of items

l = str(14)
print(l)
print(type(l)) # l is a string, treating the integer 14 and as text

m = 1e4
print(m)
print(type(m)) # m is a floating-point number, a rational number


# 1. Pretty sure I counted 8
# 2. float, str, list, bool, tuple, dict, complex, int
# 3. m and b are float; l and d are string; k, h, and e are lists
# 4. l is a string, since the function str() makes integers behave as text
# 5. Date

from datetime import date
n = my_date = date(2025, 9, 6)
print(n)
print(type(n))



# --- Booleans ---


print(10 > 9) # true, 9 < 10

print(10 == 9) # false, 9 does not equal 10

print(10 <= 9) # false, 10 is greater than 9

print(bool("abc")) # true, abc is a properly ordered list

print(bool(123)) # true, not an empty set

print(bool(["apple", "cherry", "banana"])) # true, not an empty set

print(bool(True)) # true, the function is defined as true

print(bool(False)) # false, the function is defined as false

print(bool("")) # false, the set is empty

print(bool(" ")) # true, the set is filled

print(bool(())) # false, the set is empty

print(bool([])) # false, the set is empty

print(bool({})) # false, the set is empty

print(bool(True and False)) # false, both true and false cannot be true at the same time

print(bool(True and True)) # true, true and true can be true at the same time

print(bool(False and False)) # false, both items are false

print(bool(True or False)) # true, I have no idea why

print(bool(True or True)) # true, only option is true

print(bool(False or False)) # false, only option is false

print(bool(not(False))) # true, the opposite of false is true

print(bool(not(True))) # false, the opposite of true is false

# Expressions returning true have full sets or their expressions equate to true. The vice versa is true for false values
# True or False, since i have no idea why it works
print(bool("Hello, world!")) # True since the set is full
print(bool(False or True and False)) # False since the first term is false



# --- Operators ---

# -- Arithmetic Operators --

print(10 + 5) # 15, python knows how to do addition
print(10 - 5) # 5, python knows how to do subtraction
print(2 * 4) # 8, python knows how to do multiplication
print(6 / 3) # 2, python knows how to do division
print(5 % 2) # 1, % takes the remainder of the funciton
print(3 ** 2) # 9, ** is the same as squaring a number
print(15 // 2) # 7, // runs division and then trunctuates the decimal

# -- Comparison Operators --

print(5 == 2) # false, 5 does not equal 2
print(10 != 10) # false, 10 factorial does not equal 10
print(2 < 5) # true, 2 is less than 5
print (12 > 5) # true, 12 is greater than 5
print(5 <= 6) # true, 5 is less than or equal to 6
print(1 >= 10) # false, 1 is less than 10

# -- Assignments Operators --

"""
x = 5 # I DONT KNOW HOW TO MAKE THESE WORK
print(x += 5) # 
print(x -= 4) #
print(x *= 3) #
"""

# -- Logical Operators --


# 1. And checks if BOTH conditions are True, only then will it return TRUE
True and (5 > 2) # True
True and (5 < 2) # False

# 2. Or checks if AT LEAST ONE condition is true, only returns false when both are false
True or (5 < 2) # True
False or (5 < 2) # False

# 3. Not reverses the truth value, making something that is True into something False
not(4 < 2) # True
not(4 > 2) # False

# -- More Questions --

# 1. / preforms division, while // divides and tunctuates the decimal
# 2. % takes the remainder of the function, while // trunctuates it
# 3. Use %
print(21 % 4)
# 4. No clue I dont understand this part


# --- Strings ---

my_string = "hello"
print(my_string) # prints hello
print(my_string[0]) # prints h, the first letter
print(my_string[1]) # prints e, the second letter
print(my_string[2]) # prints l, the third letter
print(my_string[3]) # prints l, the fourth letter
print(my_string[4]) # prints o, the fifth letter
print(my_string[-1]) # prints o, the last letter
print(my_string[1:3]) # prints el, the second and fourth letters
print(my_string[0:5:2]) # prints hlo, the first, second to last, and last letters
print(len(my_string)) # prints 5, the numbers of letters in the word hello
print(my_string + "goodbye") # prints hellogoodbye
print(7 * my_string) # prints hellohellohellohellohellohellohello, 7 times "hello"

# 1. Slicing is when you take only specific parts of your string, such as in [1:3] and [0:5:2]
# 2. hello, my name is is oski
name = "oski"
print("hello, my name is", name)
# 3. hello, my name is oski
name = "oski"
print(f"hello, my name is {name}")
# 4. 3 uses f-strings, a way to easily embed variables into text


# --- Terminal Commands ---

# cd
# Change directory: move from one folder to another
# Example: cd homework1.py

# ls
# list: list out everything in a directory
# ls homework1

# ls -a
# list all: list all files in a directory, including hidden files
# ls -a homework1

# mkdir
# make a new directry: create a new folder in a diretory
# mkdir homework1

# cat
# concatenate: print out all the contents in a file
# ~ cat

# pwd
# print working directory: see which directory you are currently in
# pwd homework1

# cd..
# Change directory to the parent directory
# cd.. homework1

# cd.
# Change directory to the current directory
# cd. homework1

# cd ~
# Change directory to the root directory
# cd ~

# cp
# Copy file or directory
# cp homework 1

# mv
# move files or directories to other directories
# mv homework1 ~/documents

# rm
# remove: delete files or directories
# rm homework1

# clear
# wipes all text from current terminal screen
# clear

# grep
# Global regular expression print: Used to search for specific words, phrases, or patterns inside files
# grep "hello" homework1

# 1.

# touch
# creates a new empty file
# touch newfile.txt

# man
# opens the manual page for a command if you need help or documentation
# man ls

# echo
# prints text to the terminal
# echo "Hello, world!"

# 2. ls -a show hidden files, while ls shows only visible ones

# 3. files that start with a ".", usually system or configuation files

# 4. 

# ls -l
# lists files in "long format": includes sizes, dates, etc
# ls -l

# rm -r
# removes a folder and its contents recursively
# rm -r homework1

# cp -r
# copies a folder and its contents recursively
# cp -r homework1 homework2




