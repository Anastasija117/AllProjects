# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1.positional,2.default,3.KEYWORD,4.arbitrary


#def hello(greeting,title,first,last):
#    print(f"{greeting} {title}{first} {last}")

#hello(first="Spongebob",last="Squarepants",greeting=" Hello",title ="Mr.")

#for x in range(1,11):
#    print(x,end=" ") #end is a keyword argument AND SEP IS ALSO
#print("1","2","3","4","5",sep="-")

def get_phone(country=1,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(area=123,first=456,last=7890)
print(phone_num)