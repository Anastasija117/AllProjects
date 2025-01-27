# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself


class Student:

    count = 0
    gpa_t = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.gpa_t += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa is {cls.gpa_t/cls.count:.2f}"

student1 = Student("Ane",5.2)
student2 = Student("Suze",4.5)
student3 = Student("Baki",7.6)



print(Student.get_count())
print(Student.get_avg_gpa())