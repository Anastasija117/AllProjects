# variable scope = where a varible is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

#GLOBAL - OUTSIDE OF ANY FUNCTIONS
#x = 3
from math import e #BUILT IN VERSION OF E

#def func1():
#    x = 1 #ENCLOSED
#    def func2(): # ONLY SEEN IN OWN FUNCTIONS
#       x = 2
#       print(x)
#   func2()


def func1(): # VARIABLES WITHIN A FUNCTION HAVE A LOCAL SCOPE
    x = 1 # ONLY SEEN IN OWN FUNCTIONS
    print(x)

def func2(): # ONLY SEEN IN OWN FUNCTIONS
    x = 2 #LOCAL
    print(x)

func1()
func2()
