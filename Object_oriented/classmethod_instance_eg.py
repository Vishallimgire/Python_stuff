class Book:
    TYPE = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name} {self.book_type}  {self.weight}g>'

    @classmethod
    def hardcover(cls, name, weight_book):
        return cls(name, cls.TYPE[0], weight_book + 100)

    @classmethod
    def paperback(cls, name, weight_book):
        return cls(name, cls.TYPE[1], weight_book)
        
hard_cover = Book.hardcover('c++', 1500)
paper_back = Book.paperback('python 101', 300)

print(hard_cover)
print(paper_back)
# print(book)