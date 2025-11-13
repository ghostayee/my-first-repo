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


# # # Prompt the user for a number either on a form input or the terminal.
# # #  Depending on whether the number is even or odd, display  either
# # # “odd” or “even” to the user.
# # #  Hint: how does an even / odd number react differently when
# # # divided by 2?

# num = int(input("Enter a number to determine if its Odd or Even: "))

# def OddEven_checker(num):
#     if num % 4 == 0:
#         return "divisible by 4 and Even"
#     elif num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# outcome = OddEven_checker(num)
# print(f"The number: {num} is {outcome}")



# # Write a program which gets a phone number from a form input or
# # terminal. Validates the phone number by checking if it starts
# # with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the
# # number to start with +254…
# # e.g if a user enters “0712345678”, the program should display “+254712345678”
# # e.g if a user enters “0112345678”, the program should display “+254112345678”
# # e.g if a user enters “712345678”, the program should display “+254712345678”

user_input = input("Enter your phone number: ")


def phone_number(user_input):
    phone = user_input.strip()

    if user_input.startswith("+254"):
        return phone
    elif phone.startswith("254"):
        return "+" + phone
    elif phone.startswith("07"):
        return "+254" + phone[1:]
    elif phone.startswith("7"):
        return "+254" + phone
    elif phone.startswith("01"):
        return "+254" + phone[1:]
    elif phone.startswith("1"):
        return "+254" + phone
    elif len(phone) < 9:
        return "Incomplete number"
    else:
        return "Invalid phone number format"



formatted = phone_number(user_input)
print("Formatted phone number:", formatted)
