# Homework 5


# 3.1
"""
1. Git vs. GitHub:
Git is a version control system on your computer that tracks file changes
GitHub is where Git repositories are stored online, allowing for collaboration and remote storage.

2. Terminal vs. Command Line:
Command line is the interface where you type text commands
The terminal is the application that runs the command line

3. Local vs. Remote Repository:
A local repository is the version of your project stored on your own computer
A remote repository is the version of your project stored on a server, typically on GitHub

4. Version Control:
A system that records changes to a file and lets you recall specific versions later

5. Staging Area:
An intermediate area in Git where you place files you want to include in your next commit

6. git add:
The command to move changes from the working directory to the staging area.

7. git commit:
The command to save the staged changes to your local repository

8. git push:
The command to upload your committed changes from your local repository to a remote repository

9. git status:
The command to display the state of the working directory and the staging area

10. git pull:
The command to fetch and download content from a remote repository and immediately update the local repository

11. pwd:
"Print Working Directory" shows the full path of your current directory

12. ls:
"List" lists the files and directories in the current directory

13. cd:
"Change Directory" moves to a different directory

14. nano:
creates and moves to a file you can edit

15. touch:
creates a new, empty file

16. mv:
"Move" moves or renames files and directories

17. rm:
"Remove" deletes files and directories

18. cat:
"Concatenate" displays the contents of a file in the terminal

"""

# 3.2
"""
1.  pwd

2.  ls

3.  cd ../brianna_repo
    git pull

4.  mv homework.py ~/python_decal/judy_decal/homework

5.  cd ~/python_decal/judy_decal/homework

6.  cat homework.py

7.  git add
    git commit -m "done with homework #"
    git push origin main

8.  git pull
    git push

9.  cd ~/Recent

"""

# 4

# 4.1 Data Types

def CheckDataType(data):
    return type(data)
print(CheckDataType(3.14))
print(CheckDataType(True))

# 4.2 Conditionals

def even_or_odd(data):
    if data % 2 > 0:
        return 'Odd'
    else:
        return 'Even'
print(even_or_odd(7))
print(even_or_odd(10))

# 5 Loops

numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    counter = 0
    for i in numbers:
        counter += i
    return counter
print(sumWithLoop(numbers))

# 6.1 Lists

list1 = ['a', 'b', 'c']
def duplicateList(list1):
    newList = []
    for i in list1:
        newList.append(i)
        newList.append(i)
    return(newList)
print(duplicateList(list1))

# 6.2 Debugging

def square(num):
    return num * num
print(square(5))

