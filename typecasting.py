#type casting and type conversion of data from one type to another
x = 5
w = "kennie ayee"
print(x)
print(type(x))

y = float(x)
print(y)
print(type(y))

print(w)
print(type(w))
z = str(w)

#float and int conversion
q = 9.9
print(q)
print(type(q))

e = int(q)
print(e)
print(type(e))

#try some output with it with the user input and conversion
value = input("enter any number of hours: ")

try:
    value =  int(value)
except ValueError:
    print("invalid input. please enter a valid number of hours.")
result = value * 60
value = int(value)
print(result)

#conversion to bool
a = 7.8
print(a)
print(type(a))
b= bool(a) 
print(b)
print(type(b))