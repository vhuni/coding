example2 = 1

def fn():
    example = 3
    print(example)

print(example2)

def fn2(*args):
    print(type(args))
    for arg in args:
        print(arg)

fn2('hello', 'world', 'this', 'is', 'a', 'test')


def fn3(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print('%s = %s' % (key, value))

fn3(name='bob', age=30, job='developer')