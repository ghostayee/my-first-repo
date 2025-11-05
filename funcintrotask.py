# # TASK 1
# # Write a program that prompts the user to enter the base and 
# # height of a triangle and returns its area.

# base = float(input("Enter the base of the triangle: "))
# print(f"Base: {base}cm")
# height = float(input("Enter the height of the triangle: "))
# print(f"Height: {height}cm")
# square_units = "cm²"


# def area_calculator(base, height):
#     return 0.5 * base * height


# area = area_calculator(base, height)
# print(f"The area of the triangle is: {area}{square_units}")


# # Prompt the user for a number either on a form input or the terminal.
# #  Depending on whether the number is even or odd, display  either
# # “odd” or “even” to the user.
# #  Hint: how does an even / odd number react differently when
# # divided by 2?

num = int(input("Enter a number to determine if its Odd or Even: "))

def OddEven_checker(num):
    if num % 4 == 0:
        return "divisible by 4 and Even"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"


outcome = OddEven_checker(num)
print(f"the number {num} is {outcome}")
