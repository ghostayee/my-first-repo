# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s 
# above the speed limit (70), it should give the driver one
# demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
#  If the driver gets more than 12 points, the function
# should print: “License suspended”.

car_speed = float(input("Enter speed of the car:"))
speed_limit = 70

if car_speed < 70:
    print("Ok")
else:
    speed_exceeded = car_speed - speed_limit
    demerits_points = (car_speed - speed_limit) // 5
    if speed_exceeded % 5 != 0:
        demerits_points += 1
    if demerits_points > 12:
        print(f"demerits_points- {demerits_points}")
        print("license suspended")
    else:
        print(f"points = {demerits_points}")