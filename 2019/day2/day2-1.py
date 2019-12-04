# Today's challenge:
# -

program = [1,95,7,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]

current_index = 0
block_size = 4


def process(opcode, val1, val2, index):
    global program

    value = 0
    if opcode == 1:
        value = program[val1] + program[val2]
    elif opcode == 2:
        value = program[val1] * program[val2]
    program[index] = value

    global current_index
    current_index += 1

    return value


while program[current_index * block_size] != 99:
    total_index = current_index * block_size

    process(program[total_index], program[total_index + 1], program[total_index + 2], program[total_index + 3])

print('Program finished with opcode 99')
print(program)
