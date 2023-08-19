def calculate_grade(score):
    if 90 <= score <= 100:
        return 'Outstanding'
    elif 80 <= score < 90:
        return 'Exceed Expectation'
    elif 70 <= score < 80:
        return 'Acceptable'
    elif 60 <= score < 70:
        return 'Fail'
    else:
        return 'F'

def main():
    # Sample scores for students (you can modify these values)
    student_scores = {
        "Henry":91,
        "Ron":78,
        "Hernione" :99,
        "Draco" : 74,
        "Neville" : 62,
    }

    student_grades = {}  # Dictionary to store student names and their grades

    for name, score in student_scores.items():
        grade = calculate_grade(score)
        student_grades[name] = grade

    print("Student Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

if __name__ == "__main__":
    main()
