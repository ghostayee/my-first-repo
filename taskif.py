weight = float(input("Enter your weight:"))
age = float(input("Enter your age:"))
height = float(input("Enter your height:"))

the_max = max(weight, age, height)
print(the_max)

# Quiz 2:
temp = input("Enter the temperature:")
temperature = int(temp)
if temperature > 30:
    print("Temperature is too high")
    if temperature > 15:
        print("temperature is normal")
