v = [8,11,6,9]
if v[0] >= v[1]:
    first_max, second_max = v[0], v[1]
else:
    first_max, second_max = v[1], v[0]

for i in v[2:]:
    if i >= first_max:
        second_max, first_max = first_max, i
    elif i >= second_max:
        second_max = i
print(first_max, second_max)
        