student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Herisone": 99,
    "Draco": 74,
    "Neville": 62,
}

# Dont change the code above

# 1000-1: Create an empty dictionary called student_rades
student_grades = {}
# 1000-2: Write your code below and add the grades

for student, score in student_scores.items():
    if score >= 91:
        grade ='Outstanding'
    elif score >= 81:
        grade ='Excellent'
    elif score >= 71:
        grade ='Awesome'
    elif score >= 61:
        grade ='Fair'
    elif score >= 51:
        grade ='Fail'
    else:
        grade ='Be serious young man'

    student_grades[student] = grade
    
print(student_grades)