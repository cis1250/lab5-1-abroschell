#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

#Lab 5 Part 1: Fibonacci Sequence

# Function for validating and returning the user input
def user_input():
while True: # starts the infintie loop
    input = input("Enter the number of terms: ") # getting the user input for the amount of terms
    try: # using try to get any errors from the input and then it goes to either the first if or the except error
        terms = int(input)  # takes the input and puts it into an integer
        if terms > 0: # checks if it is a non-positive integer
            return terms
        else:
            print("Please enter a positive integer")
    except ValueError: # if the user input is not valid prints the error
        print("Error! Invalid input, please enter a valid input.")

# Function for generating the Fibonacci Sequence
def generate_fibonacci_sequence(): #Fibonacci Sequence: 0 1 1 2 3 5 8 13 21 34 55 89 144
  a = 0
  b = 1
  for i in range(terms): 
    print(a, end=' ')
    a, b = b, a + b # the new value of a becomes b's old value, the new value of b is the old a and b added together [ 0, 1 - a becomes 1, b becomes 1, then a is still one, and b becomes 2]
  return terms
# grading comments: entering invalid inptut should not break your code. -1
