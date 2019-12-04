import hashlib 

key = 'bgvyzdsv'
running = True
current_number = 0
while running:
    to_hash = str(key + str(current_number)).encode('utf8')
    hashed = hashlib.md5(to_hash).hexdigest()
    if hashed[:6] == "000000":
        print(f'The first number is: {current_number}')
        running = False
        break

    current_number += 1
