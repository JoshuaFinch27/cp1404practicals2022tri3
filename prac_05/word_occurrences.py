"""
CP1404 - Practical 5
Program that: Counts the occurrences of words in a string. The program should ask the user for a string,
then print the counts of how many of each word are in the string.
"""

word_to_be_counted = {}

text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_to_be_counted.get(word, 0)
    word_to_be_counted[word] = frequency + 1


words = list(word_to_be_counted.keys())
words.sort()

if words:
    max_length = max((len(word) for word in words))
    for word in words:
        print(f"{word:{max_length}} : {word_to_be_counted[word]}")
else:
    print("No string was entered")
