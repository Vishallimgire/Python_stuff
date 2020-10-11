class A:
    def my(self):
        return 1

class B:
    def my(self):
        return 2

class C(A, B):
    pass

c = C()
print(c.my())