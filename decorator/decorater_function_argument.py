import functools
user = {'username':'vishal', 'access_level':'admin'}



def make_secure_fun(access_level):
    print(f'access_level {access_level}')
    def decorator(func):
        print('first_call decoraror', func)
        @functools.wraps(func)
        def secure_fun(*args, **kwargs):
            # import pdb;pdb.set_trace()
            print('last')
            if user['access_level'] == access_level:
                # print(func)
                return func(*args, **kwargs)
            else:
                print('No you cannot access')
        print('return secure_fun')
        return secure_fun
    print('return decorator')
    return decorator

# usng at decorator
@make_secure_fun('admin')
def get_admin_password():
    return 'admin:12345'

@make_secure_fun('guest')
def get_guest_password():
    return 'guest:6789'


#Normal function call
# get_admin_password = make_secure_fun(get_admin_password)
# print(get_admin)
# # user = {'username':'vishal', 'access_level':'admin'}

# print('admin function namess', get_admin_password.__name__)
# print(get_admin_password())

# print(get_guest_password())
print(get_admin_password())