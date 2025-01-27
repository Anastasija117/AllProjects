import math

grades = []
lenght = 5
student_name = "Alice"
for grade in range(lenght):
    grade = int(input("Enter a grade: "))
    grades.append(grade)
student_name = input("Enter your name: ")
def calculate_average(grades):
    return sum(grades) / len(grades)

def determine_grade(average):
    if average > 90:
        return "A"
    elif average >= 80 and average < 90:
        return "B"
    elif average >= 70 and average < 80:
        return "C"
    elif average >= 60 and average < 70:
        return "D"
    else:
        return "F"

def display_student_info(name,grades):
    average = calculate_average(grades)
    print(f"Student: {name}")
    print(f"Grades: {grades}")
    print(f"Average grade: {average:.2f}")
    print(f"Letter grade: {determine_grade(average)}")

display_student_info(student_name,grades)
input("THE END")

