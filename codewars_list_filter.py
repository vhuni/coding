def filter_list(l):
    'return a new list with the strings filtered out'
    new_list = []
    for item in l:
        if (type(item) == type(1)):
            new_list.append(item)
    return new_list

print(filter_list([1,2,'aasf','1','123',123]))