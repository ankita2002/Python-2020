from getpass import getpass
from hashlib import sha1

password = getpass('ENTER PASSWORD: ')
repeat = getpass('Repeat PASSWORD: ')

if(password != repeat):
    print('PASSWORD DID NOT MATCHED')
    exit(0)

a = sha1(password.encode('utf-8'))
print("SHA-1: " +a.hexdigest())