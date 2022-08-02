import random as rand
import os

dict = {
    '1': 'Rock',
    '2': 'Paper',
    '3': 'Scissor'
}

list1 = [1, 2, 3]


def evaluate(user, comp):
    if(user == comp):
        print("There was a Draw! Computer's Choice is " + comp)
    elif((user == 'Rock' and comp == 'Paper') or (user == 'Scissor' and comp == 'Rock') or (user == 'Paper' and comp == 'Scissor')):
        print("Computer Wins! Computer's Choice is " + comp)
    else:
        print("You Win! Computer's Choice is " + comp)


again = 1

while(again):
    os.system('CLS')
    compChoice = dict[str(rand.choice(list1))]
    print("Enter 1 for Rock\nEnter 2 for Paper\nEnter 3 for Scissor")
    userInp = input("Enter your choice: ")
    userChoice = dict[userInp]
    evaluate(userChoice, compChoice)
    print('Do you want to play again? Enter 1 for Yes, Enter 0 for No')
    again = int(input('Enter your choice: '))
