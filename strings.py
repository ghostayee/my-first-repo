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

#title it capitalize the first letter in a word and the rest in
#in small letters.
print(sentence.title())

#replace. if you want to be only two first occurrence then add , 2 in the code.
student = "HELLO world"
print(student.replace("l","k"))
# print(student.index("x"))
print(student.find("x")) #finds the index of a character

print(student.count('H'))#Returns the number of times a specified
#value occurs in a string

print(student.startswith("HELLO")) #its always case sensitive
print(student.endswith("d", 6))
print(student.isupper())
print(student.islower())
print(student.istitle())

#join
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

first_name = "Ken"
last_name = "Mummy"
value = f"{first_name} {last_name} is a student"
print(value)
print("This is a statement from Ken Mummy ")
print(f"This is a statement from {first_name} {last_name}")

#chapati f format method of str.
price = 25
Total_no_chapati = input("Enter number of chapati you want to buy:")
value_cost = int(Total_no_chapati)
Total_cost = value_cost * price
outcomes = f"For this number of chapatis it will cost you {Total_cost:.2f}KES "
print(outcomes)

