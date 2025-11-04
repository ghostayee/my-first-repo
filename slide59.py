# .Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.


valid_ids = [101, 102, 103]
user_id = 101

if user_id in valid_ids:
    print("access granted")
else:
    print("access denied")

# # QUIZ 4
# # 4.Given a variable value that could be of any type,
# write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.

var = 23
if isinstance(var, str):
    print("string detected")
elif isinstance(var, int):
    print("integer detected")
else:
    print("unknown type")

# # QUIZ 5
# 5.Given x = 7 and y = 14, write nested conditional
# statements that print:
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.

x = 7
y = 7

if x % 2 == 0 and y % 2 == 0:
    if y % 2 == 0:
        print("both x and y are even")
    else:
        print("only y is even")
else:
    if y % 2 == 0:
        print("only y is even")
    else:
        print("neither x nor y are even")
