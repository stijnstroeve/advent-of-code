# test = input('Mass > ')
file = open('masses.txt', 'r')

lines = file.readlines()
added = 0

test = 0
def calc(num):
    global test
    calculated = int(num) // 3 - 2
    # print(calculated)
    if calculated < 0:
        return test
    else:
        test += calculated
        return calc(calculated)

i = 0
for line in lines:
    test = 0
    i += 1

    added += calc(int(line.strip()))


file.close()
print(added)

