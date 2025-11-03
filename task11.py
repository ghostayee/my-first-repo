# TASK 11
# Write a program that takes the date of birth of a person
#  and the program outputs the age in terms of years,months,days
#  TODAY.datetime

birth_day = int(input("Enter birth day: "))
birth_month = int(input("Enter birth month (1-12): "))
birth_year = int(input("Enter your birth year: "))

current_day = int(input("Enter the day today: "))
current_month = int(input("Enter current month (1-12): "))
current_year = int(input("Enter the current year of birth: "))

years = current_year - birth_year
months = current_month - birth_month
days = current_day - birth_day

if days < 0:
    days += 30
    months -= 1

if months < 0:
    months += 12
    years -= 1

print(f"you are: {years} years, {months} months and {days} days old")