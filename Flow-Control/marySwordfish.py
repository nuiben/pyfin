print('Name: ')
name = input()  # 'Mary'
print('Password: ')
password = input()  # 'swordfish'

if name == 'Mary':
    print('Hello, Marry')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
