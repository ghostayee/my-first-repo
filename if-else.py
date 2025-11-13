x = 100
y = 20

if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is lesser than {y}")


number = 4
if number%2 == 0:
    print("Number is even")
else:
    print("Number is odd")


value = float(input("Enter a number: "))
if value%2 == 0:
    print('Number is even')
else:
    print("Number is odd")


grade = float(input("Enter grade: "))
if 70 <= grade <= 100:
    print("Grade is A")
elif 60 >= grade <= 69:
    print("Grade is B")
elif 50 >= grade <= 59:
    print("Grade is C")
elif 40 >= grade <= 49:
    print("Grade is D")
elif  0 >= grade <= 39:
    print("Grade is E")
else:
    print("Invalid grade-Enter a no between 0 and 100")


password = input("Enter password: ")

correct_password = "123456"

if len(password) == 6:
    if password == correct_password:
        print("Correct Password")
    else:
        print("Wrong Password")
else:
    print("Password too short or too long")




# program divisibility test

n = int(input("Enter and a number to check its visibility of 2 and 3: "))
if n % 2 == 0:
    print("Number is divisible by 2")
elif n % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is neither divisible by 2 nor three")
print("Done!")
# summery