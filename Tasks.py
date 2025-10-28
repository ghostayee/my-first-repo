# TASK 1 on slide 27 -strings.
# create a python file and name it string tasks.py

#task 1: name = “  JOHn  .“ to “john”
name = "JOHn . "
clean_name = name[0].upper() + name[1:].lower().strip().replace(".", "")
print(clean_name)


# Tak 2: Slice the below string to get you the resulting sentence:
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

#Task 3: Split the below sentence using a semicolon i.e ; And display length of the
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





# #TASK 3 on slide 35: lists.
# #quiz:1
# trainees = ["John", [2, ["James","Mary"]]]
# print(trainees[1][0])

# #quiz:2 output james from the list
# print(trainees[1][1][0])

# # quiz: 3 Using a method add 56 at the end of the list.
# trainees.append(56)
# print(trainees)

# # quiz: 4 Using a method add the name Mike between James and Mary.
# trainees[1][1].insert(1,"Mike")
# print(trainees)

# # quiz: 5 Using a method remove John from the list.
# trainees.remove("John")
# print(trainees)

# # quiz: 6 Using a method determine length of list.
# trainers = ["John", [2, ["James","Mary"]]]
# length = (len(trainers))
# print(length)
