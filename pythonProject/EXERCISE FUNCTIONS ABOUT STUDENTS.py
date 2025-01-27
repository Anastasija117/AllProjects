import math

students = {}
def add_student(students,name,score):
    students[name] = score
def remove_student(students,name):
    if name in students:
        del students[name]
    else:
        print(f"Student {name} not found!")
def display_students(students):
    for key,value in students.items():
        print(f"{key}:{value}")
def calculate_average_score(students):
    for key,value in students.items():
        total = sum(students.values())
        total_students = len(students)
        if total_students == 0:
            return 0
        return total / total_students
def check_student(students,name):
    if name in students:
        print(f"The student {name} exists in the list.")
    else:
        print(f"The student {name} doesn't exists in the list.")

running = True
while running:
    print("\nSelect an option: "
          "\n1.Add student"
          "\n2.Remove student"
          "\n3.Display all students"
          "\n4.Check if student exists"
          "\nq.Quit")
    print()
    user_choice = input("Enter your choice: ").lower()
    print()
    if user_choice == "q":
        print("Exiting program.")
        running = False
    elif user_choice == "1":
        name = input("Enter student's name: ")
        score = float(input("Enter student's score: "))
        add_student(students,name,score)
    elif user_choice == "2":
        student_remove = input("Enter student's name to remove: ")
        remove_student(students,student_remove)
    elif user_choice == "3":
        print("Students list: ")
        display_students(students)
    elif user_choice == "4":
        student_check = input("Enter student's name to check: ")
        if check_student(students,student_check):
            print(f"Item {student_check} exists in the inventory.")
        else:
            print(f"Item {student_check} doesn't exist in the inventory.")

    else:
        print("Invalid choice.Please try again!")

input("THE END")