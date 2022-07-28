import random as rand
print('Welcome to Number Guessing Game!\n')
print('Rules: ')
print('1) The number to be guessed is between 1 and 25')
print('2) You have 5 tries to guess the number \n')


num = rand.randint(1, 25)
tries = 5
print(num)

while(tries != 0):
    guess = input('Enter your guess: ')
    if(guess > num):
        print('Go Lesser')
    elif(guess < num):
        print('Go Higher')
    else:
        print('Well Done! You Guessed The Number')

if(tries == 0):
    print('You Lost! The Number Was:', num)