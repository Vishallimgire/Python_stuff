users = [
    {'name':'vishal', 'age':25},
    {'name':'suraj', 'age':25},
    {'name':'allen', 'age':25},
    {'name':'mahesh', 'age':25}
]

def look_fun(users,keyword, finder):
    for user in users:
        if finder(user) == keyword:
            return user
    raise RuntimeError('No record found')

def find_name(user):
    return user['name']

print(look_fun(users, 'mahesh', finder = find_name))