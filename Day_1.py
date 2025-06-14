# Basic Calculator 

# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))

# op = input("Choose the operation you want to perform : + , - , / , * :  ")

# if (op == '+'):
#     print(num_1 + num_2)
# elif (op == '-'):
#     print(num_1 - num_2)
# elif (op == '*'):
#     print(num_1 * num_2)
# elif (op == '/'):
#     if num_2 == 0:
#         print("division by zero is not possible")
#     else:
#         print(num_1 / num_2)
# else:
#     print("Invalid input")


# Number guessing game

# import random 

# x = random.randint(1,10)
# n = None
# while n!= x :
#     n = int(input("Enter a number: "))
#     if (x < n ):
#         print("less")
#     elif(x > n):
#         print("more")
#     elif(x ==n):
#         print("Congrats you guesses it right")


# Write a program that prints a multi-line poem with line numbers.
# poem = """Twinkle twinkle little star,
# How I wonder what you are,
# Up above the world so high,
# Like a diamond in the sky.
# """
# # for i , j in enumerate(poem.strip().split('\n'),start = 1):
# #     print(i,j)

# for i , j in enumerate(poem.split('\n'), start= 1):
#     if j.strip():
#         print(i,j)