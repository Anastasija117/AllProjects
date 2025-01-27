# *args = allowas you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple key-arguments
#           *unpacking operator
#           1.positional 2.default 3.keyword 4.ARBITRARY
from turtledemo.penrose import start


#def add(*nums):
 #   total = 0
 #   for arg in nums:
#       total += arg
 #   return total

#print(add(1,2,3,4,5,6))

#def display_name(*args):
 #   for arg in args:
#        print(arg,end=" ")

#display_name("Anastasija")

#def print_address(**kwargs):
 #   for key,value in kwargs.items():
 #       print(f"{key}:{value}")

#print_address(street="3MUB.",city="Kumanovo",state="Grad",zip="4315")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')},{kwargs.get('zip')}")

shipping_label("Dr.","Spongebob","Squarepants","III",
               street="123 Fake St.",
               pobox="PO box 1001",
               city="Detroit",
               state="MI",
               zip="54321")