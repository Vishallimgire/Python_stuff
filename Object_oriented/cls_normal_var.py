class Var:
    myid  = 1
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sample(self):
        print(self.myid)

v = Var(1,2)
x = Var(3,5)
# v.myid = 3
v.sample()
print(f'outside {v.myid}, {x.myid}, {Var.myid}')