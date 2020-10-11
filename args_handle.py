v = (4,3,6)
print(*v)
x, *z = v 
print(x, z)

def fun(*args):
    print('args', args)

fun(*v)

def sum(**kwargs):
    print(kwargs)
    return kwargs['x'] + kwargs['y']
    # return x + y

num = {'x':1, 'y':2}
print(sum(**num))
