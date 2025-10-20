#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

#Lab 5 Part 1: Fibonacci Sequence

# Fvalidating and returning the user input
def user_input(): 
    while True:
        try:
            user = input("Enter the number of terms: ") # get the user input
            terms = int(user) #covert the user input to an integer so it can be vaidated
            if terms > 0: # check if the user input is positve and valid
                return terms # returns the value back to the function
            print("Please enter a positive integer.")
        except ValueError:
            print("Error! Invalid input, please enter a valid number.")

# generating the fibonacci sequence
def fibonacci(terms):
    a, b = 0, 1 # the starting two values of the fibonacci sequence (initialize the values)
    for i in range(terms): # repeats for the number of terms the user inputed
        print(a, end=' ') #prints the terms 
        a, b = b, a + b


terms = user_input() # gets the input and validates the user input
print("User Input:", terms) 
print("Fibonacci Sequence: ", end='')
fibonacci(terms) #prints the terms of the fibonacci sequence
print("") # adds a new line after the sequence prints

