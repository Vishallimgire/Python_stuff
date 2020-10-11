def uppercase_decorator(function):
    print('upercase_funtion', function)
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        print('make_uppercase', make_uppercase)
        return make_uppercase

    return wrapper

def split_string(function):
    print('split_string',function)
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi)
print(say_hi())