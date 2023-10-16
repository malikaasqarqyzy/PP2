#1 A recipe you are reading states how many grams you need for the ingredient. 
# Unfortunately, your store only sells items in ounces. 
# Create a function to convert grams to ounces. (ounces = 28.3495231 * grams)
grams = int(input())

def gram_to_oz(grams):
    return grams * 0.0283495231

print(gram_to_oz(grams))
#2 Read in a Fahrenheit temperature. 
# Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
F = int(input())

def F_to_C(F):
    return (5 / 9) * (F - 32)

print(F_to_C(F))

#3 Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if 2 * c + 4 * r == numlegs:
            return c, r
    return None

#4 You are given list of numbers separated by spaces. 
# Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return [num for num in numbers if is_prime(num)]

#5 Write a function that accepts string from user and print all permutations of that string.

def display_permutations(input_str):
    def generate_permutations(current, remaining):
        if not remaining:
            print(current)
        else:
            for i in range(len(remaining)):
                next_char = remaining[i]
                rest = remaining[:i] + remaining[i + 1:]
                generate_permutations(current + next_char, rest)

    generate_permutations('', input_str)

#6 Write a function that accepts string from user, 
# return a sentence with the words reversed. We are ready -> ready are We

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8 Write a function that takes in a list of integers and returns True if it contains 007 in order

def contains_007(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

#9 Write a function that computes the volume of a sphere given its radius.

def sphere_volume(radius):
    return (4/3) * 3.14 * (radius**3)

#10 Write a Python function that takes a list and 
# returns a new list with unique elements of the first list. Note: don't use collection set.

def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

#11 Write a Python function that checks whether a word or phrase is palindrome or not. 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(word):
    clean_word = ''
    for char in word:
        if char.isalpha() or char.isdigit():
            clean_word += char.lower()
    
    reversed_word = clean_word[::-1]
    
    return clean_word == reversed_word

#12 Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

# ****
# *********
# *******

def histogram(numbers):
    for num in numbers:
        print('*' * num)

#13 Write a program able to play the "Guess the number" - game, 
# where the number to be guessed is randomly chosen between 1 and 20.
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            break

#14 Create a python file and import some of the functions from the above 13 tasks and try to use them.

# my_functions.py

def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return [num for num in numbers if is_prime(num)]

def print_permutations(input_str):
    def generate_permutations(current, remaining):
        if not remaining:
            print(current)
        else:
            for i in range(len(remaining)):
                next_char = remaining[i]
                rest = remaining[:i] + remaining[i + 1:]
                generate_permutations(current + next_char, rest)

    generate_permutations('', input_str)

# my_functions.py

import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            break

# main.py
from my_functions import guess_the_number
guess_the_number()
