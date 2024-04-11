name = input('What is your name? ')

if name[-1] == '!':
    capital_name = name[0: len(name) - 1].upper()
    print(f'HELLO {capital_name}! WHY ARE WE YELLING?')
else:
    print(f'Hello, {name}.')


