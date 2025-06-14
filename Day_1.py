# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pyfiglet",
# ]
# ///


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x) #apple

# fruits = ['apple', 'banana', 'cherry']
# indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
# print(indexed_fruits) # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

#Q1. Print a Poem with Line Numbers
# Write a program that prints the “Twinkle Twinkle Little Star” poem, with line numbers beside each line.

poem = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?
In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.
As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star."""

# enumerate(iterable, startIndex)
# lines = poem.split("\n")
# for i,l in enumerate(lines, start = 1):
#     print(i,l)


# Q2: Multiplication Table Generator
# Write a Python program that:

# Asks the user to enter a number

# Prints the multiplication table of that number from 1 to 10

# 🎯 Bonus: Add validation to make sure the input is a number.


# try :
#     x = int(input("Enter a number to print its multiplication table: "))
#     for i in range(1,11):
#         print(f"{x} * {i} = {x*i}")
# except ValueError:
#     print("Please enter a valid number")


# Q3: Use an External Module – ASCII Art Name
# Question:
# Install the external module pyfiglet

# Write a program that asks for your name and prints it as ASCII art

# import pyfiglet 
# your_name = input("Enter your name")
# print(pyfiglet.figlet_format(your_name))

#     _                             _  __                                                                                                                                   
#    / \   _ __ _   _  __ _ _ __   | |/ /   _ _ __ ___   __ _ _ __ 
#   / _ \ | '__| | | |/ _` | '_ \  | ' / | | | '_ ` _ \ / _` | '__|
#  / ___ \| |  | |_| | (_| | | | | | . \ |_| | | | | | | (_| | |   
# /_/   \_\_|   \__, |\__,_|_| |_| |_|\_\__,_|_| |_| |_|\__,_|_|   
#               |___/


