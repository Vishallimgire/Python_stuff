class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self)

    # def __str__(self):
    #     return f'{self.name} {self.age} year old'

    # def __repr__(self):
    #     return f'<Person("{self.name}", {self.age})>'

person = Person('Bob', 23)
print(person)
# print(person.__repr__())
