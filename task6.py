# Write a program that lets the user input a password.
# Give them only 4 attempts to check the passwords entered
#  against “admin@123”. If the password is correct access is
#  granted. After you show them a message ,
# the account is blocked.

# Password check (no functions)
correct = "admin@123"
attempts = 4

for attempt in range(1, attempts + 1):
    if attempt == 1:
        pass1 = input(f"Attempt {attempt}/{attempts} - Enter password: ")
    else:
        pass1 = input(f"(Attempt {attempt}/{attempts}) Incorrect, enter correct password : ")

    if pass1 == correct:
        print("Access granted.")
        break
else:
    print("Account blocked.")


