

def to_camel_case(text):
    if len(text) == 0:
        return ''
    elif '_' or '-' in text:
        new_text = text.replace('_',' ').replace('-',' ')
        split_text = new_text.split()
        final_text = split_text[0] + ''.join( word[0].upper() + word[1:] for word in split_text[1:])
        return final_text
    return str(text)

text = ''
print(to_camel_case(text))

