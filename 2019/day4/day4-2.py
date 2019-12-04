# Today's challenge:
# Make the code as short as possible

import re; code = '145852-616942'; amount, end, start, regex = 0, int(code.split('-')[1]), int(code.split('-')[0]), re.compile(r'(.)\1+')
for index in range(start, end):
    if any([len(f) <= 2 for f in [item.group(0) for item in list(regex.finditer(str(index)))]]) and not any([i + 1 < len(str(index)) and int(str(index)[i+1]) < int(char) for i, char in enumerate(str(index))]): amount += 1
print(f'Amount: {amount}')

# Guess it worked out pretty well, the code is 4 lines long
