#TASK 13
#  Write a program that takes the email and password as input
#  from a user and checks if they are equal to “admin@mail.com”
#  and password is “Admin@123” , if so then print  “Login is
# Successful” and if not print “Invalid username or password”.
# ONLY accept 3 tries after which it notifies you that you
# have been blocked.

attempts = 3
correct_mail = "admin@mail.com"
correct_pass = "Admin@123"

remaining_attempts = attempts

while remaining_attempts > 0:
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == correct_mail and password == correct_pass:
        print("Login is Successful")
        break
    else:
        remaining_attempts -= 1
        print("Invalid username or password")
        if remaining_attempts > 0:
            print("You have", remaining_attempts, "attempt(s) left.")
        else:
            print("You have been blocked.")

