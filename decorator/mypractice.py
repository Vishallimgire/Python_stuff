def myfun(func):
    def execute(a, b):
        print('hello')
        return func(a, b)
    return execute

@myfun
def sample(a, b):
    print(a,b)
    return 'hi'

# sample = myfun(sample)

print(sample(10, 12))