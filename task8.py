# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s 
# above the speed limit (70), it should give the driver one
# demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
#  If the driver gets more than 12 points, the function
# should print: “License suspended”.

car_speed = float(input("Enter speed of the car:"))
if car_speed < 70:
    print("Ok")
else:
    points = (car_speed - 70) // 5
    if points > 12:
        print("license suspended")
    else:
        print("points =",  points)