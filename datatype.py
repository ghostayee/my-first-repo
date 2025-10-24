x = 65
y = "john dee"
z = 23.6

# BOOLEAN DATA TYPES
is_active = True
has_permission = True
print(is_active)

#boolean used in comparison 
w = 10
k = 5
result1 = w > k
result2 = w == k
print(result1)
print(result2)
print(10 > 9)
print(10 == 9)
print(10 == 10)

#compare strings
name = "Alice"
print(name == "Alice")
print(name == "alice")

# condition  using  boolean
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
     print("b is not greater than a")

#evaluate values and variables
c= "hello"
j = 15.4
v = ""
is_adult = True
print (bool(c))
print (bool(j))
print (bool(v))
print(type(c))
print(type(is_adult))

user_input = input("pleas enter any value of hours and i will convert to minutes:")
user_input = int(user_input)
calculation_to_minutes = user_input * 60
print("this will be", calculation_to_minutes,"minutes")

