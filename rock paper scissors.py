import random

player_score = 0
cpu_score = 0

while (True):
    player_choice = int(
        input('enter 1 for rock 2 for paper and 3 for scissors: '))
    cpu_choice = random.randint(1, 3)

    if player_choice == cpu_choice:
        print('its a tie no points will be awarded')

    elif player_choice == 1:
        if cpu_choice == 2:
            print(' cpu chose paper and won this round')
            cpu_score += 1
            print('cpu score: ' + str(cpu_score) + '\n' +
                  'your score: ' + str(player_score))

        if cpu_choice == 3:
            print(' cpu chose scissors and lost this round')
            player_score += 1
            print('cpu score: ' + str(cpu_score) + '\n' +
                  'your score: ' + str(player_score))

    elif player_choice == 2:
        if cpu_choice == 1:
            print(' cpu chose rock and lost this round')
            player_score += 1
            print('cpu score: ' + str(cpu_score) + '\n' +
                  'your score: ' + str(player_score))

        if cpu_choice == 3:
            print(' cpu chose scissors and won this round')
            cpu_score += 1
            print('cpu score: ' + str(cpu_score) + '\n' +
                  'your score: ' + str(player_score))

    else:
        if cpu_choice == 1:
            print(' cpu chose rock and won this round')
            cpu_score += 1
            print('cpu score: ' + str(cpu_score) + '\n' +
                  'your score: ' + str(player_score))

        if cpu_choice == 2:
            print(' cpu chose paper and lost this round')
            player_score += 1
            print('cpu score: ' + str(cpu_score) + '\n' +
                  'your score: ' + str(player_score))

    if player_score == 2:
        print('you won! Best two of 3! ')
        break

    if cpu_score == 2:
        print('cpu won! sorry but have lost! ')
        break

"""
# This program the rolling of dice.
import random

# Constants for the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    # Create a variable to control the loop.
    again = 'y'

    # Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice . . .')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

    # Do another roll of the dice?
        again = input('Roll them again? (y = yes): ')

# Call the main function.
main()
"""
