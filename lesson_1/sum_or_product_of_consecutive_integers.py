print('This program will determine the sum or product of all numbers between 1 and your number, inclusive.')

start = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, or "p" to compute the product.')
if operation == 's':
    sum = 0
    for number in range(0, start + 1):
        sum += number
    print(f'The sum of the integers between 1 and {start} is {sum}.')
elif operation == 'p':
    product = 1
    for number in range(1, start + 1):
        product *= number
    print(f'The product of the integers between 1 and {start} is {product}.')