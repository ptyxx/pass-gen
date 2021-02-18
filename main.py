
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("lenght", default=False,  help="how long should be your password?")
args = parser.parse_args()
lenght = int(args.lenght)



x = r'!@#$%^&*()_-+=[]{}|\":;><.,/?'
y = '1234567890'
z = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

choice = [x, y, z]
password = ''
n = ''
previous = ''
for i in range(lenght):
    o = random.choice(choice)
    n = random.choice(o)
    if n == previous:
        n = ''
        while True:
            o = random.choice(choice)
            n += random.choice(o)
            if previous != n:
                break
            else:
                pass

    password += n
    previous = ''
    previous = n


print(f'your password: {password}')
password_file = open('password.txt', 'w')
password.encode()
password_file.write(password)
password_file.close()









