print("Let's start")
print('Try this')
print("Or with double parentheses")
print('You can do it either way')

# This is a comment.
# You can't print the comments,they are notes for the people
# reading or writing the code.

# Let's start with variables.
# Variables are a container for a value(string,integer,float,boolean)
# A variable behaves as if it was the value it contains

# Strings(series of characters,includes numbers also)
first_name = "Anastasija"
food = "lasagna"
email = "gele123@gmail.com"

print(first_name) # no quotes for this kind of printing
print(f"Hello {first_name}") #f-string for printing within sentences
print(f"You like {food}")
print(f"Your email is {email}")

# Integers(whole numbers)
age = 22 # integer is not within quotes
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float(number that contains a decimal portion)
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

# Boolean is either true or false
is_student = True
for_sale = False
is_online = True

print(f"Are you a student? : {is_student}") # mostly for if statements

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT avalible")

if is_online:
    print("They are online")
else:
    print("They are NOT online")