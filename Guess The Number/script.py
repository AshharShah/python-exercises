import random as rand
import os
print('Welcome to Number Guessing Game!\n')
print('Rules: ')
print('1) The number to be guessed is between 1 and 25')
print('2) You have 5 tries to guess the number \n')

again = 1
while(again == 1):
    num = rand.randint(1, 25)
    tries = 5
    print(num)

    while(tries != 0):
        guess = int(input('Enter your guess: '))
        if(guess > num):
            print('Go Lesser')
        elif(guess < num):
            print('Go Higher')
        else:
            print('Well Done! You Guessed The Number')
            break
        tries = tries - 1

    if(tries == 0):
        print('You Lost! The Number Was:', num)
    again = int(input('Enter 1 to play again! '))
    if(again == 1):
        os.system('CLS')
