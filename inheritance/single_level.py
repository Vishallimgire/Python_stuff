class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self, can_fly):
        if can_fly:
            return f'{self.name} can fly'
        return f'{self.name} can fly'

    def veg_or_nonveg(self, status):
        if  status:
            return f'{self.name} is vegitarian'
        return f'{self.name} is non vegitatian'


class Parrot(Bird):
    def __init__(self, name):
        super().__init__(name)

    def parrotallproperty(self):
        print(self.fly(True))
        print(self.veg_or_nonveg(True))


parrot = Parrot('Egle')
print(parrot.fly(True))
print(parrot.veg_or_nonveg(True))