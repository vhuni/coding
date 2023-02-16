# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge. Don't forget the space after the closing parentheses!

# def create_phone_number(n):
#     '''This function will create a phone number'''
#     phone_number = ''
#     for x in n:
#         phone_number += str(x)
#     return f'({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:]}'

def phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# if __name__ == '__main__':
#     '''This is will run the program in an order'''
#     print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#     print(phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
