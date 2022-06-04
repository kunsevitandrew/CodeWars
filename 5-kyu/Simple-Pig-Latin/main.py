# Simple Pig Latin

def pig_it(text):
    symbols = "?!@#$\n-.,"
    lst = text.split(" ")
    new_lst=[word[1:]+word[0]+"ay" if word not in symbols else word[:] for word in lst]
    return " ".join(new_lst)


# other solutions:

# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])