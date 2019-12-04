
def read_file(path):
    with open(path) as file:
        lines = file.readlines()
        file.close()

        return [line.strip() for line in lines]

def is_nice(string):
    has_pairs = False
    has_between = False

    for i, char in enumerate(string):
        if i + 1 < len(string):
            pair = char + string[i + 1]
            if string.count(pair) > 1:
                has_pairs = True

            if i + 2 < len(string):
                third = string[i + 2]
                if third == char:
                    has_between = True

    return has_pairs and has_between

nice_strings = 0
strings = read_file('input.txt')

for string in strings:
    if is_nice(string):
        nice_strings += 1

print(f'Input contains {nice_strings} nice strings.')