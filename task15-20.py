# TASK 15 upto 20
# QUIZ 15:
# Write a program that takes input of someone's basic salary
# and benefits, adds them to find the gross salary then uses
# the gross salary to find the NH-if.
# To find the Kenya NH-if Rate using THIS LINK:

basic_salary = float(input("Enter basic salary (KES): "))
benefits     = float(input("Enter benefits (KES): "))

gross_salary = basic_salary + benefits


if gross_salary <= 5999:
    n_hif = 150
elif gross_salary <= 7999:
    n_hif = 300
elif gross_salary <= 11999:
    n_hif = 400
elif gross_salary <= 14999:
    n_hif = 500
elif gross_salary <= 19999:
    n_hif = 600
elif gross_salary <= 24999:
    n_hif = 750
elif gross_salary <= 29999:
    n_hif = 850
elif gross_salary <= 34999:
    n_hif = 900
elif gross_salary <= 39999:
    n_hif = 950
elif gross_salary <= 44999:
    n_hif = 1000
elif gross_salary <= 49999:
    n_hif = 1100
elif gross_salary <= 59999:
    n_hif = 1200
elif gross_salary <= 69999:
    n_hif = 1300
elif gross_salary <= 79999:
    n_hif = 1400
elif gross_salary <= 89999:
    n_hif = 1500
elif gross_salary <= 99999:
    n_hif = 1600
else:
    n_hif = 1700
print(f"gross_salary: {gross_salary:.2f} KES")
print(f"N-HIF deduction is: {n_hif:.2f} KES")


# QUIZ 16
# Continue with the program above, then use  the gross
# salary to find the N-SSF.
# To find the Kenya N-SSF Rate
# using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000
# Gross Salary CAN BE USED IN N-SSF.

if gross_salary >= 18000:
    n_ssf = gross_salary * 0.06
    print(f"N-SSF deduction is : {n_ssf:.2f} KES")
else:
    print("N-SSF cannot be calculated the gross salary is below 18,000 KES")

# QUIZ 17
# Continue with the same program and calculate an individual’s N_HDF using:
#  i.e N_HDF = gross_salary *  0.015
N_HDF = gross_salary *0.015
print(f"N-HDF deduction is : {N_HDF:.2F} KES")

# QUIZ 18
# Calculate the taxable income.
# i.e taxable_income = gross salary - (N_SSF + N_HDF + N_HIF)

taxable_income = gross_salary - (n_ssf + N_HDF + n_hif)
print(f"Taxable income is : {taxable_income:.2f} KES")


# QUIZ 19:
# Continue with the same program and find the person's 
# PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK

if taxable_income <= 24000:
    payee = taxable_income * 0.1
elif taxable_income  <= 32333:
    payee = taxable_income * 0.25
elif taxable_income <= 500000:
    payee = taxable_income * 0.3
elif taxable_income <= 800000:
    payee = taxable_income * 0.325
else:
    payee = taxable_income * 0.35

print(f"payee deduction is: {payee:.2f} KES")

# QUIZ 10: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (n_hif + n_hdf +  n_ssf + payee)

net_salary = gross_salary - (n_hif + N_HDF + n_ssf + payee)
print(f"Net salary is: {net_salary:.2f} KES")