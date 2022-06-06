# How many numbers III?

# def check_sun(sum_dig, number) -> bool:
#     str_number = str(number)
#     return sum(map(int, str_number)) == sum_dig and list(str_number) == sorted(str_number)


def first_number(sum_dig, digs):
    # formation: number = 11...111
    number = int("1" * digs)
    sum_dig -= digs
    # formation min_number
    # (25, 3): 111+ 8*10**0 = 119 -> 119 + 8*10**1 = 199 -> 199 + 6*10**2 = 799

    if sum_dig // digs >= 1:
        for i in range(digs):
            if sum_dig >= 8:
                number += 8 * 10 ** i
                sum_dig -= 8
            else:
                number += sum_dig * 10 ** i
                sum_dig = 0
    else:
        # if min_number = 99...999, but sum digs != 0
        number = None

    return number


def last_number(sum_dig, digs):
    # formation: number = 11...111
    lst_number = list(map(int, "1" * digs))

    sum_dig -= digs
    i = 0

    # formation max_number
    # (10, 3): 111 -> 112 -> 122 -> 222 -> 223 -> ... -> 334
    while sum_dig > 0:
        sum_dig -= 1
        lst_number[i] += 1
        if i < digs - 1:
            i += 1
        else:
            i = 0

    # converting array to int by "gluing"
    return int("".join(map(str, lst_number[::-1])))


def other_number(current_number: list, digs, end_number):
    count = 0
    end_lst = list(map(int, str(end_number)))
    while current_number != end_lst:
        for i in range(digs - 1, 0, -1):
            if current_number[i - 1] + 1 < current_number[i]:
                count += 1
                current_number[i] -= 1
                current_number[i - 1] += 1
                print(current_number)
            elif current_number[i - 1] + 1 == current_number[i]:
                j = i - 1
                while j > 0:
                    if current_number[j] + 2 != current_number[i]:
                        current_number[j] += 1
                        current_number[i] -= 1
                        count += 1
                        j -= 1

    return count


def find_all(sum_dig, digs) -> list:
    # TODO special comment Lol :)

    start_number = first_number(sum_dig, digs)
    end_number = last_number(sum_dig, digs)

    print(f"start = {start_number}, end = {end_number}")

    count = other_number(list(map(int, str(start_number))), digs, end_number)

    # When start_number == end_number we twice count number
    if start_number == end_number:
        count -= 1

    # return lst
    return [count + 2, start_number, end_number]


res = find_all(35, 6)
print(res)
