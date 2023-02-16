list = []

while True:
    input_int = int(input('Enter random numbers... to STOP press \'99\' : '))
    list.append(input_int)
    if input_int == 99:
        list.remove(99)
        break

print('number of integers: ', len(list))
print('last integer on list: ', list[-1])
print('entered integers in reverse order: ', list[::-1])

less_5 = []
for item in list:
    if item == 5:
        print('Yes, list contains a 5')
    if item < 5:
        less_5.append(item)

print('integers less than 5: ', len(less_5))
print(less_5)


