print('Welcome to faulty calculator')
print('/ for division')
print('* for multiplication')
print('+ for addition')
print('- for addition')

operation = input('Enter the operation you wish to perform: ')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter Second Number: '))

if (operation == '*'):
    print('Result: ', num1*num2)
elif(operation == '/'):
    print('Result: ', num1/num2)
else:
    print('Result: ', 44)
