# class Fruit:
#     def __init__(self):
#         self.name = 'apple'
#         self.color = 'red'

# #example
# my_fruit = Fruit()
# print(my_fruit.name)
# print(my_fruit.color)


# class Fruit:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#         self.details()
#     def details(self):
#         print('my ' + self.name + ' is ' + self.color)

#example
# apple = Fruit('apple', 'red')
# banana = Fruit('banana', 'yellow')

# apple.details()

# inheritance

# class TropicalFruit(Fruit):
#     pass

# my_fruit = TropicalFruit('apple', 'red')
#results = my apple is red

# class TropicalFruit(Fruit):
#     def taste(self):
#         print('my ' + self.color + ' ' + self.name +' tastes good')
# my_fruit = TropicalFruit('apple', 'red')
# my_fruit.taste()

#results = my red apple tastes good

class Fruit:
    def __init__(self,name = 'apple'):
        self.name = name
        self.color = 'red'
        self.details()
        self.__cost = 10
    def details(self):
        print('my ' + self.name + ' is ' + self.color)


class TropicalFruit(Fruit):
    def __init__(self):
        super().__init__(name='banana')
        # self.name = 'banana'
        self.color ='yellow'
        self.__cost = 50
    def taste(self):
        print('my ' + self.color + ' ' + self.name +' tastes good')
    def __secret(self):
        print('the fruit cost is actually $', self._Fruit__cost)

class NewFruit(Fruit):
    pass
my_fruit = TropicalFruit()
my_fruit.taste()
print('child class fruit: ',my_fruit.name)
print('parent class fruit: ',Fruit().name)
#results
# my apple is red
# my yellow banana tastes good
# child class fruit:  banana
# my apple is red
# parent class fruit:  apple
print(my_fruit._TropicalFruit__cost)
my_fruit._TropicalFruit__secret()
#results
# my apple is red
# my yellow banana tastes good
# child class fruit:  banana
# my apple is red
# parent class fruit:  apple
# 50
# the fruit cost is actually $ 10

print(NewFruit('kiwi').name)
#results
#my kiwi is red

print('tropical fruits is ', my_fruit.name)
#results
# tropical fruit is banana