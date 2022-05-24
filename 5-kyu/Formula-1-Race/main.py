# Formula 1 Race
import re


def champion_rank(pilot: int, events: str) -> int:
    cars_id = {i: i for i in range(1, 21)}
    match = re.findall(r"(\d+) (\w)?", events)

    for number, event in match:
        number = int(number)
        if number == pilot and event == "I":
            return -1
        elif event == "O":
            for key in cars_id:
                if cars_id[key] == cars_id[number] - 1: cars_id[key] += 1
            cars_id[number] -= 1
        elif event == "I":
            i_number = cars_id[number]
            for key in cars_id:
                if cars_id[key] > i_number:
                    cars_id[key] -= 1
            cars_id[number] += 21

    return cars_id[pilot]

#
# res = champion_rank(17, "2 O 17 I")
# print(res)

# Solution from site:
# import re
#
# def champion_rank(pilot: int, events: str) -> int:
#     arr = [i for i in range(1, 21)]
#     for x in re.findall("\d+ [IO]", events):
#         r, t = x.split()
#         if t == 'I':
#             arr.remove(int(r))
#         else:
#             j = arr.index(int(r))
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#     return arr.index(pilot) + 1 if pilot in arr else -1