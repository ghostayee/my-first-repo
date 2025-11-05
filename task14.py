# TASK 14
# Write a program that takes input of 2 values and adds them.
# The program should only accept numbers and floats only or
# otherwise display an error “invalid character entered” and
# take the user to re-enter the inputs .

valid = False

while not valid:
    num1_input = input("Enter the first number: ")
    num2_input = input("Enter the second number: ")


    if (num1_input.replace('.', '', 1).isdigit() and num2_input.replace('.', '', 1).isdigit()):
        num1 = float(num1_input)
        num2 = float(num2_input)
        total = num1 + num2
        print("The sum is:", total)
        valid = True
    else:
        print("Invalid character entered. Please enter numbers only.")

