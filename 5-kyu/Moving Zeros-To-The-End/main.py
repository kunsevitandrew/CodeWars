# Moving Zeros To The End

def move_zeros(arr):
    return sorted(arr, key=lambda x: x == 0)


lst = [1, 0, 1, 2, 0, 1, 3]
res = move_zeros(lst)
print(res)

# it's optimal solution
