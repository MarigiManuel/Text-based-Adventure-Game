name = input('What is your name? ')

if len(name) < 3:
    print('Name must be more than 3 characters!')
elif len(name) > 50:
    print('Name must be no more than 50 characters!')

else:
    print('Name looks good!')