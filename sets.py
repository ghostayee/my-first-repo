#they are unordered collections of unique items and they mutable
# in sets value 1 and True are considered the same soo one will be ignored
# same  apply to false and 0

# all to note about sets
# No duplicates: Automatically removes repeated elements.
# Unordered: The order of elements is not guaranteed.
# Mutable: You can add or remove elements.
# Heterogeneous: Can contain elements of different data types (but all must be hashable).

numbers = {100,34,56,78,90,34,23,100,56,"twenty", 78.44}
print(numbers)
print(type(numbers))
print(100 in numbers)# tha attribute of unordered hence cannot use index to find.
print(len(numbers)) #find length

# .add() used to add items.
# to add sets int another set use.update()
num1 = {"green", "blue", "yellow"}
numbers.update(num1)
print(numbers)

# you can also add any iterable
my_list = [1, 2, 3]
numbers.update(my_list)
print(numbers)


# under remove items we  will have 2
# 1. remove  if the item does not exist it will bring error.

# 2. Discard this will not if the item does not exist

juice = {"apple", "banana", "cherry"}
juice.remove("apple")
print(juice)
juice.discard("cherry")
print(juice)


# senior tr.
numbers = {100,34,34,67,78,"twenty"}
print(numbers)
print(type(numbers))

print(100 in numbers)
#add()
numbers.add("five")
print(numbers)

#update()
numbers.update([1000,2000])
print(numbers)

#remove()
numbers.remove(100)
print(numbers)

#discard()
numbers.discard(1000)
print(numbers)

numbers.discard(10000)
print(numbers)

#clear
numbers.clear()
print(numbers)

fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
new_fruits = set(fruits)
print(new_fruits)

tuple_fruits = tuple(new_fruits)
print(tuple_fruits)





