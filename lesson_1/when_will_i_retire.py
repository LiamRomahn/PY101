import datetime

today = datetime.date.today()
year = int(today.year)

age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))

retire_year = int(year + (retire_age - age))

print(f'It\'s {year}. You will retire in {retire_year}.')
print(f'You have only {retire_year - year} years of work to go.')
