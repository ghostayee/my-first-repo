my_ds = [23, "jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76, "John")]
# quiz 1: print KES
print(my_ds[3][2]["currency"])


# # Quiz 2: print 560
# print(my_ds[2])

# # Quiz 3: print Maths
# print(my_ds[3][1])

# # Quiz 4
# my_ds[3][2]["amount"] = 90
# # print(my_ds)




# # QUIZ 5
# # Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
# #  Hint: Strings can be reversed using [::]
# res =str(my_ds[4])
# res = res[::-1]
# print(res)

new = list(my_ds[5])
new[1] = "jane"
new = tuple(new)
print(new)


