
def read_file(path):
    with open(path) as file:
        lines = file.readlines()
        file.close()

        return [line.strip() for line in lines]
        
vowels = ['a', 'e', 'i', 'o', 'u']
disallowed = ['ab', 'cd', 'pq', 'xy']

def is_nice(string):
    vowels_amount = 0
    has_double = False
    has_disallowed = bool([test for test in disallowed if test in string])

    for i, char in enumerate(string):
        if char in vowels:
            vowels_amount += 1
        if i + 1 < len(string):
            next_char = string[i + 1]
            if next_char == char:
                has_double = True

    return vowels_amount > 3 and has_double and not has_disallowed

nice_strings = 0
strings = read_file('input.txt')

for string in strings:
    if is_nice(string):
        nice_strings += 1

print(f'Input contains {nice_strings} nice strings.')