try:
    x = int(input("Please enter a number: "))
    y = 10/x
    print('The results is: ', y)
except ValueError:
    print('Invalid input. Please enter a number')
except ZeroDivisionError:
    print('You cannot divide by zero')