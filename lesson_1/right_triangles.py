def triangle(base):
    for i in range(1, base):
        print(f'{(" " * int(base - i)) + ("*" * i)}')
triangle(10)

