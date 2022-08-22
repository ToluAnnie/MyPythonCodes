pets = ['cats', 'dogs', 'rabbits', 'hamsters']

for myPets in pets:
    print(myPets)

for index, myPets in enumerate(pets):
    print(index, myPets)

counter = 5

while counter > 0:
    print(f'counter = {counter}')
    counter = counter - 1

j = 0

for i in range(5):
    j = j + 2
    print(f'i = {i}, j = {j}')
    if j == 6:
        break

for i in range(5):
    j = j + 2
    print(f'i = {i}, j = {j}')
    if j == 6:
        continue
    print('I will be skipped if j = 6')

try:
    user_input1 = int(input('Please enter a number: '))
    user_input2 = int(input('Please enter another number: '))
    answer = user_input1/user_input2
    my_file = open('missing.txt', 'r')
except ValueError:
    print('Error: you did not enter a number')
except ZeroDivisionError:
    print('Error: cannot divide by zero')
except Exception as e:
    print(f'Unknown error: {e}')



def checkIfPrime(y):
    for x in range(2, y):
        if y%x == 0:
            return False
        return True


answer = checkIfPrime(20)
print(answer)


message1 = 'global variable'

def myFunction():
    print('inside the function')
    print(message1)
    message2 = 'local variable'
    print(message2)

myFunction()
print('outside the function')
print(message1)
print(message2)



