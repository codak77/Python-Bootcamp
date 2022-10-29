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
