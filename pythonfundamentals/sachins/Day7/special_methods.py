#
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'"{self.title}", from {self.author}'

#
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages

book = Book("title", "sachin", 4)
print(len(book))

#
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __del__(self):
        print(f'Book deleted')

my_book = Book("title", "Sachin", 8)
del my_book