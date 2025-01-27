# Membership operators = used to test whether a value or variable is found in a
#                       sequence(string,list,tuple,set,or dictionary)
#                       1.in     2.not in


#word = "APPLE"
#letter = input("Guess a letter in the secret word: ")
#if letter not in word:
#    print(f"{letter} was not found!")
#else:
#    print(f"There is a {letter}.")

#students = {"spongebob","patrick","sandy"}
#student = input("Enter the name of a student: ")
#if student in students:
#    print(f"{student} is a student")
#else:
#    print(f"{student} was not found")

grades = {"Sandy":"A","Wendy":"F","Sarah":"B"}
student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")