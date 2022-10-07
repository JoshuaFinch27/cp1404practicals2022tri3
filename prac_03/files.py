"""
CP1404 - Practical 3
Task: Complete the 4 separate tasks
1. Write code that asks the user for their name, then opens a file
called "name.txt" and writes that name to it. Remember to close your file.

2. (In the same file, but as if it were a separate program) Write code that
opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).

3. Create a text file called numbers.txt and save it in your prac directory.
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds
them together then prints the result, which should be... 59.

4. Now write a fourth block of code that prints the total for all
lines in numbers.txt or a file with any number of numbers.
"""

# Task 1
# name = input("Enter name: ")
# out_file = open('name.txt', 'w')
# print(name, file=out_file)
# out_file.close()

# Task 2
# in_file = open('name.txt', 'r')
# name = in_file.read().strip()
# print(f"You're name is {name}")
# in_file.close()

# Task 3
# in_file = open("numbers.txt", "r")
# total = int(in_file.readline()) + int(in_file.readline())
# print(total)
# in_file.close()

# Task 4
# in_file = open("numbers.txt", "r")
# total = 0
# for line in in_file:
#     number = int(line)
#     total += number
# print(total)
# in_file.close()
