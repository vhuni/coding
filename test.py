
n = 5
i = 1
f = 1

while i <= n:
    f = f*i
    i += 1

print(f)

shopping_list = ['bread', 'pears', 'grapes', 'cheese']


new_list = ' '.join(x for x in shopping_list if x.startswith(('b','c')))
print(new_list)


# Consider the following dictionary:

ages = {'Tom': 32,
        'James': 23,
        'George': 37
        }
        
check = ['Alex', 'Adam', 'Tom', 'James', 'George']
        
# Iterate through the check list and print the ages of the people in the check list. 
# If the name doesn't exist in the ages dict then print 'No age record found'

for x in check:
    if x in ages:
        print(x,':', ages[x])
    else:
        print(x,':','No age record found')