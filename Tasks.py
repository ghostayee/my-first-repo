# TASK 1 on slide 27 -strings.
# create a python file and name it string tasks.py

#QUIZ 1: name = “  JOHn  .“ to “john”
name = "JOHn . "
clean_name = name[0].upper() + name[1:].lower().strip().replace(".", "")
print(clean_name)


# QUIZ 2: Slice the below string to get you the resulting sentence:
#a) sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
sentence_one = "The dog breed is a german shepherd"
length = len(sentence_one)
print(length, sentence_one[8:25])

#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only
# display “Clinton forces”
sentence_two = "Defeats for the Clinton forces , this was her moment of triumph"
print(sentence_two[16:30])
index = sentence_two.index("s")
print(index)

#QUIZ 3: Split the below sentence using a semicolon i.e ; And display length of the
# result.
# “The lazy dog; ran so fast; it hit the wall.”
content_sentence = "The lazy dog; ran so fast; it hit the wall."
split_sentence = content_sentence.split(";")
print(split_sentence, len(split_sentence))

#first_name="  joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name = " joh.n"
last_name = "Do,e"
clean_name = first_name.lstrip()[0].upper() + first_name[2:].lower().replace(".","") + " " + last_name.replace(",","").capitalize()
print(clean_name)





# #TASK 2 on slide 30: Floats and integers.
#quiz 1: Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57
temp = 56.8926
print(round(temp))


#Quiz 2: Convert the float below to give the results as follows
# temp = 56.8926 to 56.89
result = round(temp, 2)
print(result)

# Quiz 3: Convert the float below to give the results as follows
# temp = 56.8926 to 56.893
round = round(temp, 3)
print(round)

# Quiz 4: Convert the float below to give the results as follows
# temp=56.8926 to 8.926
# NB: Use string  slice & concatenation, but have result as float
# convert to string first
conv = str(temp)
sliced = conv[2:7]
new_conv = sliced[1] + "." + sliced[2:]
print(new_conv)





#TASK 3 on slide 35: lists.
#quiz:1
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])

#quiz:2 output james from the list
print(trainees[1][1][0])

# quiz: 3 Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)

# quiz: 4 Using a method add the name Mike between James and Mary.
trainees[1][1].insert(1,"Mike")
print(trainees)

# quiz: 5 Using a method remove John from the list.
trainees.remove("John")
print(trainees)

# quiz: 6 Using a method determine length of list.
trainers = ["John", [2, ["James","Mary"]]]
length = (len(trainers))
print(length)

# then more questions on this link 
link = "https://realpython.com/quizzes/python-lists-tuples/viewer/"






#TASK 5 on slide 38: lists.
# 1.How to update a tuple? - adding / removing / changing items in a tuple

#Quiz 1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
numbers = (10, 20, 30, 40, 50)
num = list(numbers)
print(type(num))
num.append(60)
num[2] = 35
x = tuple(num)
print(x)

# Quiz 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)
conv = list(values)
conv.sort()
tuple_back = tuple(conv)
print(tuple_back)

#Quiz 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",Remove all occurrences of "banana".
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
fruits = tuple(x for x in fruits if x != "banana")
print(fruits)

fruits_combo = list(fruits)
fruits_combo = [x for x in fruits_combo if x != "banana"]
print(fruits_combo)
converted = tuple(fruits_combo)
print(converted )

#QUIZ 4 :4.
# names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort 
# method.

names = ("Alice", "Bob", "Charlie", "David")
names_reversed = tuple(reversed(names))
print(names_reversed)

# method 2 especially when you want to change list permanently
names2 = list(names)
names2.reverse()
print(names2)

name3 = list(reversed(names2))
print(name3)

names4 = names2[::-1]
print(names4)

# QUIZ 5: 5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with 
# ["purple", "orange"]

# method 1. con
colors = ("red", "blue", "green")
colors = colors[:1] + ("yellow",) + colors[1:]
print(colors)

#now we come and convert the to a tuple
colors = colors + tuple(["purple", "orange"])
print(colors)

# method 2
# convert it into a list first
colors1 = ("red", "blue", "green")
colors2 = list(colors1)
colors2.insert(1,"yellow")
colors2.extend(["purple", "orange"])
print(colors2)

# alternatively i can use +=
colors3 = ("red", "blue", "green")
colors4 = list(colors3)
colors4 += ["purple","orange"]
print(colors4)





