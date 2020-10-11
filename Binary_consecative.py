n = int(input())
binary_n = "{0:b}".format(n)
for i in range(len(binary_n)-1):
    if binary_n[i] == 1 and binary_n[i] == binary_n[i+1]:
        c = c + 1

print(c)
        