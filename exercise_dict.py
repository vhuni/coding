
def funct1(num_items):
    list = {}

    for i in range (num_items):
        name = input('Enter product name: ')
        price = input('Enter product price: ')

        list[name] = price

    print(list)

def funct2():
    x = int(input('Enter a number as x: '))
    y = int(input('Enter a number as y: '))

    abs_value = abs(x-y)/(x+y)
    print('answer is :', abs_value)


# funct1(2)
funct2()