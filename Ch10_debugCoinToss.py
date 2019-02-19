import random

guess = ''


while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = raw_input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if guess == 'tails':
    guess = 0
else:
    guess = 1

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')

    guess = raw_input()
    if guess == 'tails':
        guess = 0
    else:
        guess = 1
        
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
