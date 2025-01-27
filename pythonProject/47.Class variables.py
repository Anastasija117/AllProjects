# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Anastasija Gelevska", 22)
student2 = Student("Ivana Stojanovska", 31)
student3 = Student("Simona Ilievska", 27)

print(student1.name)
print(student1.age)
print(Student.class_year)
print()
print(student2.name)
print(student2.age)
print(Student.class_year)

print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

print(f"They are:{student1.name},{student2.name},{student3.name}")