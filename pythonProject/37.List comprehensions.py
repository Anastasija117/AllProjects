# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

#doubles = []
#for x in range(1,11):
#    doubles.append(x * 2)

#print(doubles)

#doubles = [x * 2 for x in range(1,11)]
#triples = [y * 3 for y in range(1,11)]
#squares = [z * z for z in range(1,11)]
#even = [a + 10 for a in range(1,11) if a % 2 == 0]
#print(doubles)
#print(triples)
#print(squares)
#print(even)

#fruits = ["apple","orange","banana","coconut"]
#fruits = [fruit.upper() for fruit in fruits]
#fruitss = [fruit[0] for fruit in fruits]
#print(fruitss)


#numbers = [1,-2,3,-4,5,-6,7,8,9,10]
#positive = [num for num in numbers if num >= 0]
#negative = [num for num in numbers if num <= 0]
#even = [num for num in numbers if num % 2 == 0]
#odd = [num for num in numbers if num % 2 == 1]
#print(positive)
#print(negative)
#print(even)
#print(odd)

grades = [85,42,79,90,56,61,30]
passing = [grade for grade in grades if grade >= 60]
print(passing)








