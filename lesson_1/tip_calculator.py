bill = float(input('What is the bill? '))
tip_percent = float(input('What is the tip percentage? '))
tip_amount = bill * (tip_percent / 100)

print(f'The tip is ${tip_amount}')
print(f'The total is ${tip_amount + bill}')