# TASK 15 upto 20
# QUIZ 15:


basic_salary = float(input("Enter basic salary (KES): "))
benefits     = float(input("Enter benefits (KES): "))

gross_salary = basic_salary + benefits
print("Gross salary is: KES", gross_salary)

contribution = gross_salary * 2.75 / 100
if contribution < 300:
    contribution = 300
    
print("Health insurance contribution (SHIF) is: KES", round(contribution, 2))
