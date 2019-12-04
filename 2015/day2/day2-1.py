
def read_file(path):
    with open(path) as file:
        lines = file.readlines()
        file.close()

        return [line.strip() for line in lines]
        
inputs = read_file('input.txt')
summed = 0

for dimensions in inputs:
    split = dimensions.split('x')
    l = int(split[0])
    w = int(split[1])
    h = int(split[2])
    calculated = 2*l*w + 2*w*h + 2*h*l
    slack = min([l*w, w*h, h*l])
    total = calculated + slack
    summed += total
    print(f'{total} {slack} {calculated}')

print(f'The sum of all dimensions is: {summed}')