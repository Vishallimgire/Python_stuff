user = {'username':'vishal', 'access_level':'admin'}



def make_secure_fun(func):
    print('first_call')
    def secure_fun():
        # import pdb;pdb.set_trace()
        print('last')
        if user['access_level'] == 'admin':
            # print(func)
            return func()
        else:
            print('No you cannot access')
    print('second')
    return secure_fun

# usng at decorator
@make_secure_fun
def get_admin_password():
     return '1234'

#Normal function call
# get_admin_password = make_secure_fun(get_admin_password)
# print(get_admin)
# # user = {'username':'vishal', 'access_level':'admin'}

print(get_admin_password.__name__)
print(get_admin_password())
