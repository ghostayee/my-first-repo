# TASK 12
# Write a program that prints the largest of 4 inputs
# taken as input from a user.

first_score = int(input("Enter first score: "))
sec_score = int(input("Enter second score: "))
third_score = int(input("Enter third score: "))
fourth_score = int(input("Enter fourth score: "))

largest =  first_score

if sec_score > largest:
    largest = sec_score
if third_score > largest:
    largest = third_score
if fourth_score > largest:
    largest = fourth_score

print(f"The largest number is: {largest}")
