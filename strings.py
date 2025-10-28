#str concatenating
first_name = "John"
second_name = "Ghost"
full_name = first_name + " " + second_name
print(full_name)

#another type of it using f format
full_name2 = f"{first_name} {second_name}"
print(full_name2)

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
paragraph = "This is a random string i want to know its length"
length = len(paragraph)
print(length)


exam = "Jesus is lord"
length = len(exam)
sliced = exam[9:]
start_name = exam[9]
print(sliced.upper())
print(sliced.lower())
print(start_name.upper())

#TASK ON STRING METHODS

#strip - remove whitespaces at the start and at the end 
string = "     random string.    "
fruit = ".....,,,,,grt,,grt,,banana,,,,,,,"
print(string)
print(string.strip())
print(fruit.strip(".,grt"))

#rstrip & lstrip
print(string.rstrip())
print(string.lstrip())

#split 
sentence = "this is a dog; of brand; German Shepherd"
print(sentence.split(';'))

#title
print(sentence.title())

#replace 
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

