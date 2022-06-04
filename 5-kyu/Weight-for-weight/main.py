# Weight for weight

def sum_of_numbers(text):
    return sum(map(int, text))


def order_weight(strng):
    lst = sorted(strng.split(" "))
    lst = sorted(lst, key=sum_of_numbers)
    return " ".join(lst)


text = "103 123 4444 99 2000"
res = order_weight((text))
print(res)

# other variants:

# def weight_key(s):
#     return (sum(int(c) for c in s), s)
# def order_weight(s):
#     return ' '.join(sorted(s.split(' '), key=weight_key))
