# Write that prompts the user to input student marks.
#  The input should be between 0 and 100.
# Then output the correct grade:
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - l
# ess 40

# this means


# A: greater than 79
# B: 60 to 79
# C: 50 to 59
# D: 40 to 49
# E: less than 40

student_score = float(input("Enter your score: "))
if student_score < 0 or student_score > 100:
    print("Marks should be between 0 and 100")
else:
    if student_score > 79:
        grade = "A"
    elif student_score >= 60:
        grade = "B"
    elif student_score >= 50:
        grade = "C"
    elif student_score >= 40:
        grade = "D"
    else:
        grade = "E"
    print(f"the grade is: {grade}")
