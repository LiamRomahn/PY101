import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
SHORTENED_CHOICES = ['r', 'p', 's', 'sp', 'l']

def prompt(message):
    print(f"==> {message}")

player_wins = 0
computer_wins = 0

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while (choice not in VALID_CHOICES) and (choice not in SHORTENED_CHOICES):
        prompt("That's not a valid choice")
        choice = input()

    if choice in SHORTENED_CHOICES:
        choice = VALID_CHOICES[SHORTENED_CHOICES.index(choice)]

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')

    if ((choice == 'rock' and computer_choice == 'scissors') or
        (choice == 'rock' and computer_choice == 'lizard') or
        (choice == 'spock' and computer_choice == 'scissors') or
        (choice == 'spock' and computer_choice == 'rock') or
        (choice == 'lizard' and computer_choice == 'spock') or
        (choice == 'lizard' and computer_choice == 'paper') or
        (choice == 'paper' and computer_choice == 'spock') or
        (choice == 'paper' and computer_choice == 'rock') or
        (choice == 'scissors' and computer_choice == 'lizard') or
        (choice == 'scissors' and computer_choice == 'paper')):
        prompt("You win!")
        player_wins += 1
        prompt(f'The current score is {player_wins} to {computer_wins}.')
    elif ((choice == 'rock' and computer_choice == 'paper') or
        (choice == 'rock' and computer_choice == 'spock') or
        (choice == 'spock' and computer_choice == 'paper') or
        (choice == 'spock' and computer_choice == 'lizard') or
        (choice == 'lizard' and computer_choice == 'rock') or
        (choice == 'lizard' and computer_choice == 'scissors') or
        (choice == 'paper' and computer_choice == 'scissors') or
        (choice == 'paper' and computer_choice == 'lizard') or
        (choice == 'scissors' and computer_choice == 'spock') or
        (choice == 'scissors' and computer_choice == 'rock')):
        prompt('Computer wins!')
        computer_wins += 1
        prompt(f'The current score is {player_wins} to {computer_wins}.')
    else:
        prompt('It\'s a tie!')
        prompt(f'The current score is {player_wins} to {computer_wins}.')

    if (player_wins == 3) or (computer_wins == 3):
        if player_wins == 3:
            prompt('You are the grand winner!')
        else:
            prompt('The computer is the grand winner!')
        break

    prompt('Do you want to play again? (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break