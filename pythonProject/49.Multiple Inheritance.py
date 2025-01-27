# multiple inheritance = inherit from more than one parent class
#                        C(A,B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal:
    def __init__(self,animal):
        self.animal = animal
    def eat(self):
        print(f"This {self.animal} is eating")
    def sleep(self):
        print(f"This {self.animal} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"This {self.animal} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.animal} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
rabbit.flee()
rabbit.sleep()
