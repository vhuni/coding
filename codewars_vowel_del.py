def disemvowel(string_):
    # vowels = ["A","a","E","e","I","i","O","o","U","u"]
    # text = [letter for letter in string_ if letter not in vowels]
    # new_str = ''.join(text)
    # return new_str

    #### Best answer!!!!!!!!!
    new_str = ''.join([letter for letter in string_ if letter.lower() not in 'aeiou'])
    return new_str

print(disemvowel("hEllo WOrldu!"))


def is_isogram(string):
    # new_str = list(dict.fromkeys(''.join(string.lower())))
    # if len(new_str) != len(string):
    #     return False
    # else:
    #     return True

    ### Best answer!!!!!!!!!!!!!!!
     return len(string) == len(set(string.lower()))
    
print(is_isogram("aba"))

def disemvowel(string):
    vowels = "aeiouAEIOU"
    return "".join(char for char in string if char not in vowels)

# Test the function
input_string = "Hello, Codewars!"
result = disemvowel(input_string)
print(result)  # Output: "Hll, Cdwr!"