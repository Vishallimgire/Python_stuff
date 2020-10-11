class A:
    def __init__(self):
        self.__j = 1
        self.k = 5
    
    def display(self):
        print(self.__j, self.k)
    
class B(A):
    def __init__(self):
        super().__init__()
        self.__j = 2
        self.k = 7

c = B()
c.display()