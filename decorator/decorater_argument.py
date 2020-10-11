import functools
user = {'username':'vishal', 'access_level':'admin'}



def make_secure_fun(func):
    print('first_call')
    @functools.wraps(func)
    def secure_fun(*args, **kwargs):
        # import pdb;pdb.set_trace()
        print('last')
        if user['access_level'] == 'admin':
            # print(func)
            return func(*args, **kwargs)
        else:
            print('No you cannot access')
    print('second')
    return secure_fun

# usng at decorator
@make_secure_fun
def get_admin_password(panel):
    if panel == 'management':
        return '1234'
    else:
        return 'secure_password'

#Normal function call
# get_admin_password = make_secure_fun(get_admin_password)
# print(get_admin)
# # user = {'username':'vishal', 'access_level':'admin'}

print(get_admin_password.__name__)
print(get_admin_password('management1'))
