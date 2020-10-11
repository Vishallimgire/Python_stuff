# n = int(input())
# phone_dir = set()
# #import pdb;pdb.set_trace()
# for i in range(n):
#     name_phone = tuple(map(str,input().strip().split()))
#     phone_dir.add(name_phone)
# print(phone_dir)
# for i in range(n):
#     name = str(input())
#     if name in phone_dir(0)
n = int(input())
phone_book = {}

for i in range(n):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = phone

for j in range(n):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")






