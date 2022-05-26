# A Simple Music Encoder

def difference(arr, i, size):
    if i < size - 2:
        return (arr[i] - arr[i + 1] == arr[i + 1] - arr[i + 2], arr[i + 1] - arr[i])
    else:
        return (False, -1)


def compress(arr):
    """A sequence of 2 or more identical numbers is shortened as number*count
    A sequence of 3 or more consecutive numbers is shortened as first-last. This is true for both ascending and descending order
    A sequence of 3 or more numbers with the same interval is shortened as first-last/interval. Note that the interval does NOT need a sign
    Compression happens left to right
    """
    size = len(arr)
    lst_text = []
    i = 0

    while i < size:

        # A sequence of 2 or more identical numbers is shortened as number*count
        if i < size - 1 and arr[i] == arr[i + 1]:
            j = i + 1
            while j < size - 1:
                if arr[j] == arr[j + 1]:
                    j += 1
                else:
                    break

            lst_text.append(f"{arr[i]}*{j - i + 1}")
            i = j+1

        # A sequence of 3 or more consecutive numbers is shortened as first-last. This is true for both ascending and descending order
        elif difference(arr, i, size) in ((True, -1), (True, 1)):
            j = i + 1
            while difference(arr, j, size) in ((True, -1), (True, 1)):
                j += 1

            lst_text.append(f"{arr[i]}-{arr[j + 1]}")
            i = j + 2

        # A sequence of 3 or more numbers with the same interval is shortened as first-last/interval. Note that the interval does NOT need a sign
        elif difference(arr, i, size)[0]:
            interval = difference(arr, i, size)[1]
            j = i + 1
            while difference(arr, j, size)[0]:
                j += 1
            lst_text.append(f"{arr[i]}-{arr[j + 1]}/{abs(interval)}")
            i = j + 2

        else:
            lst_text.append(f"{arr[i]}")
            i += 1

    return ",".join(lst_text)


res=compress([1, 2, 2, 3])
print(res)
