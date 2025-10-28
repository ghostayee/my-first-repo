#str concatenating
first_name = "Ken"
second_name = "Ghost"
full_name = first_name + " " + second_name
print(full_name)
price = 59

#another type of it using f format
#USED to combine str and numbers in python.
print(f"{first_name} {second_name}")
print(f"The price is ${price:.2f}")

#sales calculation:
value = input("Enter number of calculators you want to buy:")
cost = int(value) * price
print(f"This will cost you: ${cost:.2f}")


#indexing start from 0 always and from right side -1
actor = "Jack Nicholson"
print(actor[7])
print(actor[-2])
print(actor[-5])

#slicing taking a portion of a string
portion = actor[0:8]
print(portion)
print(actor[-4:-1])
#same as above
print(actor[10:13])

print(actor[11:])

#length of a string
paragraph = "This is a random string i want to know its length anyway"
print(len(paragraph))

slogan = "Jesus is lord"
print(len(slogan))
sliced = slogan[9:]
start_name = slogan[9]
print(sliced.upper())
print(sliced.lower())
print(start_name.upper())

#TASK ON STRING METHODS

#strip - remove whitespaces at the start and at the end.
string = "     random string.    "
fruit = ".....,,,,,grt,,grt,,banana,,,,,,,"
print(string.strip())
print(fruit.strip(".,grt"))

#rstrip & lstrip remove whitespace respectively right and left.
print(string.rstrip())
print(string.lstrip())
print(fruit.lstrip(".,grt"))
print(fruit.rstrip(".,grt"))

#split so that each word is a list item.
sentence = "this is a dog; of brand; German Shepherd"
print(sentence.split(';'))

#title
print(sentence.title())

#replace.
student = "Hello world"
print(student.replace("l","k"))
# print(student.index("x"))
print(student.find("x"))
print(student.count('H'))
print(student.startswith("Helo"))
print(student.endswith("s"))
print(student.isupper())
print(student.islower())
print(student.istitle())

first_name = "Ken"
last_name = "Mugambi"
value = f"{first_name} {last_name} is a student"
print(value)
print("This is a statement from Ken Mugambi ")
print(f"This is a statement from {first_name} {last_name}")

x = 5

