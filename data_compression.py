count = 0
complist = [1,1,2,1]
mydata = []
temp = complist[0]
for i, each in enumerate(complist):
    if temp == each:
        count = count + 1
    else:
        # print(f'{temp} and count is {count}')
        mydata.append((temp, count))
        count = 1
    temp = each
    if i == len(complist) - 1:
        # print(f'{temp} and count is {count}')
        mydata.append((temp, count))
print(mydata)
