# Author: Salim Mohamed
# GitHub username: salimmohamed
# Date: 01/20/2024
# Description: A program that asks an input for password length, whether or not to use special characters and whether or not there should be numbers, then give out a randomly generated password.

import random
import string
print("Welcome to Password Generator!")
print("Please enter the length of the password you want to generate.")
length = int(input())
print("Do you want to use special characters?")
special = input()
print("Do you want to use numbers?")
numbers = input()
password = ""
if special == "yes" and numbers == "yes":
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    print(password)
elif special == "yes" and numbers == "no":
    for i in range(length):
        password += random.choice(string.ascii_letters + string.punctuation)
    print(password)
elif special == "no" and numbers == "yes":
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)
    print(password)
elif special == "no" and numbers == "no":
    for i in range(length):
        password += random.choice(string.ascii_letters)
    print(password)
else:
    print("Invalid input. Please try again.")