
score = float(input("Please enter your score: "))
if score >= 90:
    print("Your grade is A!")
elif 80 <= score < 89:
    print("Your grade is B!")
elif 70 <= score < 79:
    print("Your grade is C!")
elif 60<= score < 69:
    print("Your score is D!")
elif score < 60:
    print("You failed!")
