# Simple assembler interpreter


def simple_assembler(program):
    dct_variables = {}
    lst_program = [i.split(" ") for i in program.split("\n")]
    i = 0

    while i != len(lst_program):
        if lst_program[i][0] == "mov":
            if lst_program[i][1] not in dct_variables:
                dct_variables[lst_program[i][1]] = None

            if lst_program[i][2] not in dct_variables:
                dct_variables[lst_program[i][1]] = int(lst_program[i][2])
            else:
                dct_variables[lst_program[i][1]] = dct_variables[lst_program[i][2]]

        elif lst_program[i][0] == "inc":
            dct_variables[lst_program[i][1]] += 1

        elif lst_program[i][0] == "dec":
            dct_variables[lst_program[i][1]] -= 1

        else:  # jnz
            if lst_program[i][1] not in dct_variables and lst_program[i][1] != "0":
                i += int(lst_program[i][2]) - 1

            elif dct_variables[lst_program[i][1]] != 0:
                i += int(lst_program[i][2]) - 1

        i += 1

    return dct_variables


text = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''

res = simple_assembler(text)
print(res)
