# function = a block of reusable code
# place () after the function name to invoke it

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("anastasija","gelevska")
print(full_name)
print()

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due:{due_date}")

display_invoice("Bro", 42.50, 10.12 )


print()
print()
def happy_birthday(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age}!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("Bro",20)

# return = statement used to end a function
# and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(divide(1,2))