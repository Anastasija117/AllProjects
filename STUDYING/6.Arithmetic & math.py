import math
from ctypes.wintypes import RECTL
from math import remainder

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -=2
# friends = friends * 3
# friends *=3
# friends = friends / 2
# friends /= 2
# friends = friends **2
# remainder = friends % 3 // print(remainder) // 1
# print(remainder)

x = 16.1
y = 4
z = 5

# result=round(x) # DA ZAOKRUZIS BROJ
# result = abs(y) # absolute value from -4 to 4
# result=pow(4, 3)(4 na stepen 3)
# result = max(x,y,z)
# result = min(x,y,z)
# print(result)

# print(math.pi)
# print(math.e)
# result = math.sqrt(x) for x=9 result=3
# result = math.ceil(x) ROUNDING UP
# result = math.floor(x) ROUNDING DOWN
# print(result)




import math


# C = 2pir

radius = float(input("What is the radius?: "))
print(radius)

C = 2 * math.pi * radius

print(f"The circumference is: {round(C, 4)}cm")




import math

# A = pi rSQR

radius = float(input("Enter the radius: "))
print(radius)
A = math.pi * pow(radius, 2)
print(f"The area is {round(A, 2)}")