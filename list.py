items = ["Mango","Apple","Banana",1,2,3]
print(items)
print(items[5])

items[0] = "Pear"
print(items)

print(items[1][2])

values = [1,2,3,[4,5,6,["x","y"]],[7,8,9],10]
print(values[3][3][0])

print(len(values))

#append
items = ["Mango","Apple","Banana",1,2,3]
items.append("Orange")
items.append(100)
items.append([80,90])
print(items)

#extend
items.extend([200,300,"peach"])
print(items)

#insert
items.insert(3,"One")
print(items)

#remove
items.remove("Mango")
print(items)

#pop
items.pop()
items.pop()
print(items)

items.pop(3)
print(items)


#clear
items.clear()
print(items)

#count() returns how many times an item occurs in a list
numbers = [1,2,3,4,5,1,2,1,1,1,1]
print(numbers.count(1))


#index() returns the position (index) of the first occurrence of a specified value.
print(numbers.index(4))
print(numbers.index(1))

#sort() sorts the list ascending by default
#quiz can it be saved in variable?.
numbers_keep = [5,3,8,1,4,2]
numbers_keep.sort()
print(numbers_keep)

#max() returns the largest item in a list
halo = [23,45,67,89,12,90,34]
print(max(halo))
print(min(halo)) #for min.

#copy() creates a copy of the list
new_numbers = numbers.copy()
print(new_numbers)

# methods of joining lists.
# 1) using + operator
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

#2) using extend()
list_a = [1,2,3]
list_b = [4,5,6]
list_a.extend(list_b)
print(list_a)
