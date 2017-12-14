import hashlib
import string
import math
import time

symbols = [str(i) for i in range(0, 10)]
symbols += [l for l in string.ascii_letters]
#print(''.join(symbols))

# search hash: d52387880e1ea22817a72d3759213819 -> Java
#              a7f5f35426b927411fc9231b56382173 -> Python
#password_hash = 'd52387880e1ea22817a72d3759213819'
password_hash = 'a7f5f35426b927411fc9231b56382173'

count = 0
password_max_length = 6
max_count = len(symbols)**password_max_length
print(max_count)
def password_generator(password, num = 0, password_hash = None):
    global count
    if password_hash is None:
        return False
    for s in symbols:
        count += 1
        password[num] = s
        if count % int(max_count/10) == 0:
            print(math.ceil(count/max_count*100), '%')
        if num < len(password) - 1:
            if password_generator(password, num + 1, password_hash):
                return True
        else:
            #print(password)
            new_password = ''.join(password).encode()
            current_hash = hashlib.md5(new_password).hexdigest()
            if password_hash == current_hash:
                print('\nFound: {} {}'.format(new_password, current_hash))
                return True

password = ['0' for i in range(password_max_length)]
t1 = time.time()
password_generator(password, password_hash = password_hash)
t2 = time.time()
print('time span {} s'.format(t2 - t1))
