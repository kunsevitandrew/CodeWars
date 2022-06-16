# Range Extraction



def solution(args):
    res_text = ""
    i = 0
    size = len(args)

    while i <= size - 1:
        if i <= size - 3 and ((args[i] - args[i + 1]) == (args[i + 1] - args[i + 2]) == 1 or (args[i] - args[i + 1]) == (args[i + 1] - args[i + 2]) == -1):
            dr = args[i] - args[i + 1]
            j = i
            while i <= size - 2 and (args[i] - args[i + 1]) == dr:
                i += 1
            if i == size - 2:
                i += 1
            res_text += str(args[j]) + "-" + str(args[i]) + ","
        else:
            res_text += str(args[i]) + ","

        i += 1

    return res_text[:-1]


# test = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
# test_res = '-6,-3-1,3-5,7-11,14,15,17-20'

# test = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]
# test_res = '-3--1,2,10,15,16,18-20'
#
# res = solution(test)
#
# print(res)

# other variants
# def solution(arr):
#     ranges = []
#     a = b = arr[0]
#     for n in arr[1:] + [None]:
#         if n != b+1:
#             ranges.append(str(a) if a == b else "{}{}{}".format(a, "," if a+1 == b else "-", b))
#             a = n
#         b = n
#     return ",".join(ranges)