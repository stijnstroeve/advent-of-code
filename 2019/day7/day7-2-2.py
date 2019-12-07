import itertools

code = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#
# code = [103, 1, 4, 1, 103, 1, 4, 1, 99]

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

class Program:
    code = [99]
    pointer = 0
    opcode = -1

    given_inputs = []
    input_pointer = 0

    outputs = []
    outputs_pointer = 0

    def __init__(self, code):
        self.code = code

    def get_current_opcode_with_modes(self):
        opcode_string = str(self.code[self.pointer])
        return solve_opcode(opcode_string)

    def get_parameters(self, opcode):
        parameters = []
        block_size = opcode_block_sizes[opcode]
        for i in range(block_size - 1):
            parameters.append(self.code[self.pointer + (i+1)])
        return parameters

    def get_value_with_mode(self, parameter, mode):
        value = 0
        if mode == 0:  # Position mode
            value = self.code[parameter]
        elif mode == 1:  # Immediate mode(write instruction will never be in this mode)
            value = parameter

        return value

    def process_step(self, opcode, parameters, modes):
        pointer_changed = False

        if opcode == 1:
            value = self.get_value_with_mode(parameters[0], modes[0]) + self.get_value_with_mode(parameters[1], modes[1])
            self.code[parameters[2]] = value
        elif opcode == 2:
            value = self.get_value_with_mode(parameters[0], modes[0]) * self.get_value_with_mode(parameters[1], modes[1])
            self.code[parameters[2]] = value
        elif opcode == 3:
            try:
                value = self.given_inputs[self.input_pointer]
                self.input_pointer += 1
                self.code[parameters[0]] = value
            except:
                try:
                    return
                    # value = int(input('Enter a number > '))
                    # self.code[parameters[0]] = value
                except:
                    self.process_step(opcode, parameters, modes)
        elif opcode == 4:
            value = self.get_value_with_mode(parameters[0], modes[0])
            self.outputs.append(value)
            # print(f'Output: {value}')
        elif opcode == 5:
            if self.get_value_with_mode(parameters[0], modes[0]) != 0:
                self.pointer = self.get_value_with_mode(parameters[1], modes[1])
                pointer_changed = True
        elif opcode == 6:
            if self.get_value_with_mode(parameters[0], modes[0]) == 0:
                self.pointer = self.get_value_with_mode(parameters[1], modes[1])
                pointer_changed = True
        elif opcode == 7:
            self.code[parameters[2]] = 1 if self.get_value_with_mode(parameters[0], modes[0]) < self.get_value_with_mode(
                parameters[1], modes[1]) else 0
        elif opcode == 8:
            self.code[parameters[2]] = 1 if self.get_value_with_mode(parameters[0], modes[0]) == self.get_value_with_mode(
                parameters[1], modes[1]) else 0

        if not pointer_changed:
            self.pointer += opcode_block_sizes[opcode]

    def step(self):
        opcode, c, b, a = self.get_current_opcode_with_modes()
        self.opcode = opcode
        if opcode == 0:
            self.pointer += 1
            return
        if opcode == 99: return

        parameters = self.get_parameters(opcode)
        self.process_step(opcode, parameters, [c, b, a])

    def input(self, inp):
        self.given_inputs.append(inp)

    def run_till_output(self):
        while True:
            try:
                output = self.outputs[self.outputs_pointer]
                self.outputs_pointer += 1
                return output
            except:
                self.step()

    def read_output(self):
        try:
            output = self.outputs[self.outputs_pointer]
            self.outputs_pointer += 1
            return output
        except:
            return None


programs = []
sequences = [''.join(p) for p in itertools.permutations('56789')]

for sequence in sequences:
    programs.clear()

    starting_signal = 0

    int_sequence = [int(p) for p in list(sequence)]
    for amplifier in int_sequence:
        program = Program(code.copy())
        program.input(starting_signal)
        programs.append(program)



program = Program(code)


program.input(0)
program.input(5)
program.input(6)
program.input(7)
program.input(8)
program.input(9)

while program.opcode != 99:
    program.step()

print(f'Read output: {program.read_output()}')
print(f'Read output: {program.read_output()}')
print(f'Read output: {program.read_output()}')
print(f'Read output: {program.read_output()}')
print(f'Read output: {program.read_output()}')

# program.step()
# print(f'Read output: {program.read_output()}')

# program.input(10)
# program.step()
# program.step()
# print(f'Read output: {program.read_output()}')

# program.input(10)
# program.step()
# print(f'Read output: {program.read_output()}')

print(program.outputs, program.outputs_pointer)
print(program.code)
