scale = input('Enter \'m\' for meters and \'ft\' for feet: ')
length = float(input('Enter the length of the room: '))
width = float(input('Enter the width of the room: '))

if scale == 'm':
    print(f'The area of the room is {length * width} meters squared ({length * width * 10.7639} feet squared).')
else:
    print(f'The area of the room is {length * width} feet squared ({(length * width) / 10.7639} meters squared).')
