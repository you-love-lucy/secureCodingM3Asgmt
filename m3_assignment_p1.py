import hashlib

type = input('Please enter input type\n1: string\n2: file\n')
usrInput = ''

if type == '1':
    usrInput = input('Enter string: ')
elif type == '2':
    file = open(input('File path: '), 'r')
    usrInput = file.read()
else:
    print('Error')

encodedInput = usrInput.encode()
hashedInput = hashlib.sha256(encodedInput)
print('Hashed:', hashedInput.hexdigest())