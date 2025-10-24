temp = 56.8926
result = round(temp)
print(result)

#task 2
result2 = round(temp, 2)
print(result2)

#task 3 
result3 = round(temp, 3)
print(result3)

#task 4
temp_str = str(temp)
sliced = temp_str[2:]
print(sliced)

new_str = "8" + sliced
print(new_str)
result = float(new_str)
print(result)

result = round(float(new_str), 3)
#print(result)
