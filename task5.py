# Implement a program that takes 3 users  inputs from the terminal
#  or the Browser, and stores them in three variables.
# Return the largest of the three. Do this without using
# the the inbuilt max () function!

height = input("Enter your height: ")
age = input("Enter your age: ")
weight = input("Enter your weight: ")

if height > age and height > weight:
    print(f"{height} is the largest")
elif age > height and age > weight:
    print(f"{age} is the largest")
elif age == weight == height:
    print("the are all equal")
else:
    print(f"{weight} is the largest")