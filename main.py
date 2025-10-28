x = 3
num = 45
email = "mayeeayee@outlook.com"
full_name = "ken aye"

#this are the data types encountered al along the way
number1 = 15
number2 = 81.01
message = "Hello World!!"
password_correct = False


print(number1)
print(type(number1))
print(type(number2))
print(type(message))
print(type(password_correct))

#python input and user inputs
value = input("enter any number of hours and will convert to minutes:")
outcome = int(value) * 60
print(f"Awesome ! This will be equals to {outcome} minutes")

#another example of output
weight = 20
y = input("Enter your age: ")
print(f"now weight will be: {weight + int(y)}")

#casting conversion.
x = 200
print(x)
print(type(x))

y = str(x) 
print(y)
print(type(y))

z = float(x)
print(z)

value1 = 1
bool_value1 = bool(value1)

value2 = 0
bool_value2 = bool(value2)

print(bool_value1)
print(bool_value2)

num = 23.56
num2 = int(num)
print(num2)

text = "1005"
number = int(text)
print(number)
print(type(number))




