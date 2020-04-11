username = input('enter your name')
userpassword = input('enter your password')
passwordlength = len(userpassword)
pattern = '*' * passwordlength
print(f'your password is {pattern}  and contains {passwordlength} characters')
