# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone,cup,book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object
from car import Car

car1 = Car("Peugeot", 2024, "turquoise", False)
car2 = Car("BMW", 2009,"red",True)


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print()
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print()

car1.drive()
car1.stop()

car2.drive()
car2.stop()

car1.describe()
car2.describe()