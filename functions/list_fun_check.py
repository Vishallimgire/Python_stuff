def add(z = []):
    z.append(4)
    return z

s = [1,2,3]
c = add(s)
print('s', s)
print('c', c)
c.append(5)
print('s', s)
print('c', c)


