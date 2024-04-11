def print_in_box(string):
    dash = '-'
    space = ' '
    
    print(f'+{dash * (len(string) + 2)}+')
    print(f'|{space * (len(string) + 2)}|')
    print(f'| {string} |')
    print(f'|{space * (len(string) + 2)}|')
    print(f'+{dash * (len(string) + 2)}+')

print(print_in_box('To boldly go where no one has gone before.'))



print(len('--------------------------------------------'))
print(len('To boldly go where no one has gone before.'))

