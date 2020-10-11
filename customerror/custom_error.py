class ExceedError(Exception):
    pass

class Book:
    def __init__(self, count):
        self.count = count

    def check_capacity(self):
        if self.count > 100: #101>100
            raise ExceedError('Pages exceed form more than 100')

book = Book(99)
try: 
    book.check_capacity()
except ExceedError as e:
    print(e)
else:
    print('else')
finally:
    print('finally')