def validate_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

print('Welcome to the loan calculator....')

while True:

    loan = float(input('Enter the loan amount: '))
    while validate_number(loan) or float(loan) <= 0:
        loan = float(input('Please enter a valid number greater than 0: '))

    apr = input('Enter the Annual Percentage Rate (APR). e.g. 2.5 for 2.5%: ')
    while validate_number(apr) or float(apr) < 0:
        apr = input('Please enter a valid number greater than or equal to 0: ')

    duration = float(input('Enter the loan duration in months: '))
    while validate_number(duration) or float(duration) <= 0:
        duration = float(input('Please enter a valid number greater than 0: '))

    rate = float(apr) / 1200

    if apr == '0':
        payment = loan / duration
    else:
        payment = loan * (rate / (1 - (1 + rate) ** (-duration)))

    print(f'Your monthly payment is ${payment:.2f}')

    print('Would you like to calculate another loan? (y/n) ')
    answer = input()
    if answer and answer[0].lower() != 'y':
        break