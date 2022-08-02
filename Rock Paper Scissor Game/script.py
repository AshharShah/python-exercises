import random as rand

dict = {
    '1': 'Rock',
    '2': 'Paper',
    '3': 'Scissor'
}

list1 = [1, 2, 3]
print(dict[str(rand.choice(list1))])
