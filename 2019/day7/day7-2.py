# Today's challenge:
# Make the program as fast as possible

import time
import itertools

# My input
# program = [3,8,1001,8,10,8,105,1,0,0,21,38,59,84,93,110,191,272,353,434,99999,3,9,101,5,9,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,102,5,9,9,1001,9,4,9,1002,9,2,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99]
program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

opcode_block_sizes = [
    1, # Opcode 0  doesnt exist
    4, # Opcode 1: add
    4, # Opcode 2: multiply
    2, # Opcode 3: input
    2, # Opcode 4: output
    3, # Opcode 5: jump-if-true
    3, # Opcode 6: jump-if-false
    4, # Opcode 7: less than
    4, # Opcode 8: equals
]
current_total_index = 0
current_input_index = 0
outputs = []

test = -1

def execute(data, inputs):
    global opcode_block_sizes
    global current_total_index
    global current_input_index
    global outputs
    global test

    def solve_opcode(opcode_string):
        if len(opcode_string) <= 2:
            return (int(opcode_string), 0, 0, 0)
        else:
            opcode = int(opcode_string[-2:])
            opcode_string = opcode_string.rjust(5).replace(' ', '0')

            m1 = int(opcode_string[0])
            m2 = int(opcode_string[1])
            m3 = int(opcode_string[2])

            return (opcode, m3, m2, m1)

    def get_value_with_mode(parameter, mode):
        value = 0
        if mode == 0:  # Position mode
            value = data[parameter]
        elif mode == 1:  # Immediate mode(write instruction will never be in this mode)
            value = parameter

        return value

    def process(opcode, parameters, modes):
        global current_total_index, current_input_index, outputs, test
        pointer_changed = False

        if opcode == 1:
            value = get_value_with_mode(parameters[0], modes[0]) + get_value_with_mode(parameters[1], modes[1])
            data[parameters[2]] = value
        elif opcode == 2:
            value = get_value_with_mode(parameters[0], modes[0]) * get_value_with_mode(parameters[1], modes[1])
            data[parameters[2]] = value
        elif opcode == 3:
            try:
                value = inputs[current_input_index]
                current_input_index += 1
                data[parameters[0]] = value
            except:
                try:
                    value = int(input('Enter a number > '))
                    data[parameters[0]] = value
                except:
                    process(opcode, parameters, modes)
        elif opcode == 4:
            value = get_value_with_mode(parameters[0], modes[0])
            outputs.append(value)
            print(f'Output: {value}')
        elif opcode == 5:
            if get_value_with_mode(parameters[0], modes[0]) != 0:
                current_total_index = get_value_with_mode(parameters[1], modes[1])
                pointer_changed = True
        elif opcode == 6:
            if get_value_with_mode(parameters[0], modes[0]) == 0:
                current_total_index = get_value_with_mode(parameters[1], modes[1])
                pointer_changed = True
        elif opcode == 7:
            data[parameters[2]] = 1 if get_value_with_mode(parameters[0], modes[0]) < get_value_with_mode(
                parameters[1], modes[1]) else 0
        elif opcode == 8:
            data[parameters[2]] = 1 if get_value_with_mode(parameters[0], modes[0]) == get_value_with_mode(
                parameters[1], modes[1]) else 0

        if not pointer_changed:
            current_total_index += opcode_block_sizes[opcode]

    while data[current_total_index] != 99:
        opcode_string = str(data[current_total_index])
        opcode, c, b, a = solve_opcode(opcode_string)

        if opcode == 0:
            current_total_index += 1
            continue

        parameters = []

        size = opcode_block_sizes[opcode]
        for i in range(size - 1):
            parameters.append(data[current_total_index + (i+1)])

        process(opcode, parameters, [c, b, a])
    current_total_index = 0
    current_input_index = 0
    return outputs

highest_output = 0

sequences = [''.join(p) for p in itertools.permutations('56789')]
def test_sequence(sequence):
    global outputs
    global highest_output

    prev_output = 0

    running_programs = []

    for amplifier in sequence:
        prev_output = execute(program.copy(), [amplifier, 0])[0]

        # outputs = []
        print(amplifier)

    if prev_output > highest_output:
        highest_output = prev_output

# for sequence in sequences:
#     test_sequence([int(p) for p in list(sequence)])

test_sequence([5,6,7,8,9])

print(f'Highest output signal: {highest_output}')

now = time.time()
# execute(program.copy())
print('Program finished with opcode 99')
print(f'Finished in {time.time() - now} seconds')


# Guess it worked uit pretty good, could do better if I had more time I guess.
