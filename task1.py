# Write a program that prompts the user to enter the
#  base and height of a triangle and returns its area
units = "cm"
base = float(input("Enter the base of triangle: "))
print(f"Base = {base} {units}")
height = float(input("Enter the height of the triangle: "))
print(f"Height = {height} {units}")

area = 0.5 * base * height
print(f"The area is: {area} cm²")
