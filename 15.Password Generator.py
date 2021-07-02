import random
import string

print('Welcome to Password Generator!')

def code():

    length = int(input('Enter the length of the password: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower+symbols+upper+num

    temp = random.sample(all,length)

    password = "".join(temp)

    print(f'Your password is: {password}')

code()

display= str(input('Do you want to generate another password?(yes/no): '))

if display == 'yes':
    code()
else:
    print('Thank you for using our program!')




