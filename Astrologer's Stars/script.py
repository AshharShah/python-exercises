print('Welcome to Astologer\'s Stars Program')
num = int(input('Enter a number to print the pattern: '))

# for the top portion
for x in range(num):
    for y in range(x+1):
        print('*', end=" ")
    print('\n')

# for the bottom portion
for x in range(num, 0, -1):
    for y in range(x):
        print('*', end=" ")
    print('\n')

print('Pattern Printed Sucessfully!')
