# if = Do some code only IF some condition is TRUE
# Else do something else

age = int(input("How old are you?: "))

if age > 100:
    print("You are too old to sign up")
elif age < 0:
    print("You haven't been born yet")
elif age >= 18:
    print("You are now signed up")
else:
    print("You are NOT old enough to sign up")







response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you")
else:
    print("Error")





name = input("Enter your name: ")

if name == "":
    print("YOU DIDN'T ENTER ANYTHING!!")
elif name == "Anastasija":
    print("The same name as me,awasome!")
else:
    print(f"What a nice name!Hello {name}!")







for_sale = False

if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")