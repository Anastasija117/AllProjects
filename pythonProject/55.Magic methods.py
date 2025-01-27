# Magic methods = Dunder methods (Double underscore) __init__,__str__,__eq__
#                 They are automatically called by many Python's built-in operators
#                 They allow developers to define or customize the behavior of objects


class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): #returnable string
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title

    def __getitem__(self, item):
        if item == 'title':
            return self.title
        elif item == 'author':
            return self.author
        elif item == 'num_pages':
            return self.num_pages
        else:
            return f"Key {item} was not found"

#Book("Harry Potter","J.K Rowling",223)

book1 = Book("The Hobit","J.R.R Tolkien",310)
book2 = Book("Harry Potter","J.K Rowling",223)
book3 = Book("The Lion King","C.S Lewis",172)

print(book3 < book2)
print(book2)
print(book3)

print("Apple" in book3)
print()
print(book2['title'])
print(book1['author'])
print(book3['num_pages'])
print(book2['audio'])