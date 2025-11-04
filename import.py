# Python, you can import modules (built-in or external) to
# use extra functionality — like math functions, working with
#  dates, random numbers, etc.

# examples maths
import math
x = 25
result = math.sqrt(x)
print(f"The square root of {x} is {result}")


# it can be specific functions
from math import sqrt
print(sqrt(49))

# import date:
import datetime
today = datetime.date.today()
print(today)

# if import only datetime
from datetime import date
now = date.today()
print(now)
