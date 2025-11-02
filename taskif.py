# # QUIZ 1 slide 56
# # Take three inputs from a user, separately. Print the largest of the numbers.
#     # Hint: Determine what type of data is taken in as input.


# weight = float(input("Enter your weight:"))
# age = float(input("Enter your age:"))
# height = float(input("Enter your height:"))

# the_max = max(weight, age, height)
# print(the_max)

# # Quiz 2:
# # 2.Take as input from a user the temperature if the temperature
# #  is above 30°C display “The temperature is too high”,if the 
# # temperature is above 15 display “Normal temperature” otherwise
# #  display “Cold temperature”
# temp = input("Enter the temperature:")
# temperature = int(temp)
# if temperature > 30:
#     print("Temperature is too high")
#     if temperature > 15:
#         print("temperature is normal")

# # QUIZ 3
# # Write a Python program that checks if a variable x is between 10 and 20 
# # (inclusive)
# # and if another variable y is greater than 100. If both conditions 
# # are true, print "Conditions met", otherwise print "Conditions not met"

# x = int(input("Enter a number x:"))
# y = int(input("Enter a int y:"))

# if 10 < x < 20 and y > 100:
#     print("Conditions met")
# else:
#     print("condition not met")

# # QUIZ 4:
# # 4. Write a Python program that checks if a variable password is
# #  equal to the string "secret123". If it is, print "Access   
# # granted", otherwise print "Access denied"
# password = str(input("Enter your password"))

# if password == "secret123":
#     print("Access Granted")
# else:
#     print("Access denied")

# # QUIZ 5
# # 5. Write a Python program that checks if a variable student_score
# #  is greater than 90. If true, check if the attendance is greater than 80. 
# # If both conditions are true, print "Excellent student", otherwise 
# # print "Good score, but attendance needs improvement"

# score = int(input("Enter your score"))
# attendance = int(input("Enter your attendance"))

# if score > 90 and attendance > 80:
#     print("Excellent student")
# elif score < 90:
#     print("Your score is below average low")
# else:
#     print("Good score but attendance need improvement")

# # SLIDE 56:
# # NESTED IF STATEMENT:
# # Takes a transaction amount and account
# # type ("Standard" or "Premium") as input.
# # If the account type is "Standard":
# # Check if the amount is above 500:
# # If it is, print "Transaction exceeds the limit for
# # Standard accounts."
# # If not, print "Transaction approved."
# # If the account type is "Premium":
# # Check if the amount is above 1,000:
# # If it is, print "Transaction exceeds the limit for
# # Premium accounts."
# # If not, print "Transaction approved."

# transaction_amount = float(input("Enter the transaction amount: "))
# account_type = input("Enter account type: ")

# if account_type == "standard":
#     if transaction_amount > 500:
#         print("Transaction exceeds the limit for standard account")
#     else:
#         print("Transaction approved")
# elif account_type == "premium":
#     if transaction_amount > 1000:
#         print("The transaction exceeds the limit for premium account.")
#     else:
#         print("Transaction approved")
# else:
#     print("Invalid account entered.")





# # SLIDE 58:
# # 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'.
# # Write a conditional statement that checks:
# # If start_date comes before end_date, print "Valid period",
# # If start_date is after end_date, print "Invalid period".
# # If both dates are the same, print "One-day period"..

# start_date = '2024-01-01'
# end_date = '2024-12-31'

# if start_date < end_date:
#     print("Valid period")
# elif start_date > end_date:
#     print("Invalid period")
# else:
#     print("one-day period")


# # b)
# # 2.Given two strings str1 and str2, write a conditional statement that checks:
# # If str1 is longer than str2, print "str1 is longer".
# # If str2 is longer than str1, print "str2 is longer".
# # If both have equal length, print "Both are of equal length"

str1 = input("Enter statement: ")
str2 = input("Put the second statement: ")

if len(str1) > len(str2):
    print("str1 is longer")
elif len(str1) < len(str2):
    print("str2 is longer")
else:
    print("both are of equal length")