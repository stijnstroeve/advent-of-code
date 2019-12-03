
def read_file(path):
    with open(path) as file:
        lines = file.readlines()
        file.close()

        return [line.strip() for line in lines]
        
inputs = read_file('inputs.txt')

def calculate_paper(all_dimensions):
    summed = 0
    for dimensions in all_dimensions:
        split = dimensions.split('x')
        l = int(split[0])
        w = int(split[1])
        h = int(split[2])
        calculated = 2*l*w + 2*w*h + 2*h*l
        slack = min([l*w, w*h, h*l])
        total = calculated + slack
        summed += total
    return summed

def calculate_ribbons(all_dimensions):
    summed = 0
    for dimensions in all_dimensions:
        split = dimensions.split('x')
        l = int(split[0])
        w = int(split[1])
        h = int(split[2])

        sorted_dims = sorted((l, w, h))
        smallest = sorted_dims[0]
        smallest2 = sorted_dims[1]

        present = smallest * 2 + smallest2 * 2
        bow = l * w * h
        total = present + bow

        summed += total
    return summed

print(f'The sum of all dimensions of paper is: {calculate_paper(inputs)}')
print(f'The sum of all dimensions of ribbons is: {calculate_ribbons(inputs)}')