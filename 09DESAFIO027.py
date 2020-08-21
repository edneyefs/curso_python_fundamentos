name = str(input('Type your name: ')).strip()
n = name.split()
print('Your first name is: {}'.format(n[0].upper()))
print('Your last name is: {}'.format(n[len(n)-1].upper()))
