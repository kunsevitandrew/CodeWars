# Number of integer partitions

def task(lst, dct_of_indexes, n, index=0) -> int:
    while lst[index] != 1:
        print(lst)
        if dct_of_indexes[lst[index]] == 0:
            del dct_of_indexes
        lst[index] -= 1

        for i in dct_of_indexes:
            lst[dct_of_indexes[i]]+=1
            # if dct_of_indexes[]
            # task()


def partitions(n):
    """define a function which returns the number of integer partitions of n"""
    lst = [n] + [0] * (n - 1)
    dct_of_indexes = {5: 0, 0: 4}

    count = task(lst, dct_of_indexes, n)
    return count


# test
res = partitions(5)
print(res)
