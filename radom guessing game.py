import random

n = int(input('enter a num betwwen 1 and: '))
number = random.randint(1, n)
guess = int(input('enter a number between 1 and {}: '.format(n)))

while guess != number:
    if guess < number:
        print('your guess was low')
        guess = int(input('enter a number between 1 and {}: '.format(n)))

    if guess > number:
        print('your guess was high')
        guess = int(input('enter a number between 1 and {}: '.format(n)))

print('you guessed it')
