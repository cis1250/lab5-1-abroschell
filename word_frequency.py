#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# new added code with functions

# to get and validate the user input
def get_sentence():
    while True:
        sentence = input("Enter a sentence: ")
        if is_sentence(sentence):
            return sentence
        print("This does not meet the criteria for a sentence.")

# to calculate  the word frequencies
def calculate_frequencies(sentence):
    split_sentence = sentence.split()
    words = []
    frequency = []

    for word in split_sentence:
        word = word.strip(".,!?").lower()
        if word in words:
            index = words.index(word)
            frequency[index] += 1
        else:
            words.append(word)
            frequency.append(1)
    
    return words, frequency

# to print the word frequencies
def print_frequencies(words, frequency):
    for i in range(len(words)):
        print(f"{words[i]}: {frequency[i]}")


sentence = get_sentence() # gets the sentence from the user input
words, frequency = calculate_frequencies(sentence)
print_frequencies(words, frequency) # prints the word and the frequency

