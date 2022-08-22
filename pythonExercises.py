def sum_or_product(x, y):
    sum = x + y
    product = x * y

    if product >= 1000:
        print(product)
    else:
        print(sum)


sum_or_product(20, 30)
sum_or_product(40, 30)

i = 0
for j in range(10):
    sum = j + i
    i = j
    print(f'i: {i}, j: {j}, sum: {sum}')

user_input = input('What is your first name: ')

size = len(user_input)

for i in range(0, size, 2):
    print(f'even index: {i}, letter: {user_input[i]}')


def remove_char(str, n):
    new_str = str[n:]
    return new_str


x = remove_char('Tolulope', 3)
print(x)

def same_number(x_list):
    first_num = x_list[0]
    second_num = x_list[-1]
    if first_num == second_num:
        return True
    else:
        return False


output = same_number([10, 20, 30, 40, 10])
print(output)

x_list = [10, 20, 33, 46, 55]

for n in x_list:
    if n%5 == 0:
        print(n)

str = 'Emma is a good developer. Emma is a writer'
sub_str = 'Emma'

no_times = str.count(sub_str)
print(no_times)


for n in range(10):
    for i in range(n):
        print(n, end='')
    print('\n')

pyramid_nos = ['1', '2', '3', '4', '5']

def make_pyramid():
    for index in range(0, 5):
        n = pyramid_nos[index]
        for i in range(1, 5):
            print(n * i)


output = make_pyramid()
print(output)

def create_new_list():
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]
    new_list = []
    for n in list1:
        if n % 2 != 0:
            new_list.append(n)
    for i in list2:
        if i % 2 == 0:
            new_list.append(i)
    print(new_list)


create_new_list()

number = int(input('Input an integer: '))

while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end='')


def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


palindrome(121)
palindrome(125)

def get_income_tax():
    income = int(input('Input your income: '))
    tax = 0.1 * 10000
    if income <= 10000:
        print('Income is not taxable')
    elif income <= 20000:
        print(tax)
    else:
        remainder = income - 20000
        tax += (0.2 * remainder)
        print(tax)

get_income_tax()

def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print()

multiplication_table()

str = '* '

for i in range(5, 0, -1):
    print(str * i)


for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)



pizzas = ['pepperoni', 'pineapple', 'chicken bbq']
for item in pizzas:
    print(f'I love {item} pizza')

print('I just really love pizza')

animals = ['puppies', 'dogs', 'bitches']
for item in animals:
    print(f'I love {item}')

for i in range(1, 21):
    print(i)
million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

odd_numbers = list(range(1, 20, 2))
for i in odd_numbers:
    print(i)

multiples = list(range(3, 31, 3))
for i in multiples:
    print(i)

for value in list(range(1, 11)):
    cubes = value ** 3
    print(cubes)

animals = ['tiger', 'cheetah', 'leopard']

for cat in animals:
    print(f'A {cat} would make a great pet!')
print('Any of these animals would make a great pet!')

cubes = [values **3 for values in range(1,11)]
print(cubes)

fruits = ['apple', 'cucumber', 'orange', 'watermelon', 'pineapple', 'orange']
print(f'The first three items in the list are: {fruits[:3]}')
print(f'Three items from the middle of the list are:{fruits[2:4]}')


pizzas = ['pepperoni', 'pineapple', 'chicken bbq']
friend_pizzas = pizzas[:]
pizzas.append('beef')
print('my favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('my favorite foods are:')
for new_pizzas in friend_pizzas:
    print(new_pizzas)

menu = ('jollof rice', 'fried rice', 'ofada rice', 'burger', 'kebab')
for food in menu:
    print(food)
#menu[3] = 'shawarma'
#print(menu)
revised_menu = ('jollof rice', 'kebab', 'fried rice', 'shawarma', 'amala')
for meal in revised_menu:
    print(meal)

usernames = []
if usernames:
    for user in usernames:
        if user == 'Admin':
            print('Hello admin, would you like to see a special report?')
else:
    #print(f'Hello {user}, thank you for logging in again')
    print('We need to find some users')

current_users = ['Tannie', 'Jamin', 'Sofia', 'Simi', 'Janet', 'Simeon', 'David']
new_users = ['Teeto', 'Jamin', 'Anna', 'Janet', 'Ebony', 'Shawn']

for user in new_users:
    if user in current_users:
        print('Username already exists. Enter another Username')
    else:
        print('Username is available')

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

person = {'first_name': 'Jamin',
          'last_name': 'Galadima',
          'Age': 25,
          'City': 'Lagos'
}
print(person['first_name'])
print(person['last_name'])
print(person['Age'])
print(person['City'])

favorite_numbers ={'Taylor': 13,
                   'Tolu': 27,
                   'Tems': 19,
                   'Missy': 23,
                   'Simeon': 36
}
for names, numbers in favorite_numbers.items():
    print(f'{names}: {numbers}')

glossary = {'string': 'words made up of characters',
                     'integer': 'whole number values',
                     'float': 'decimal numbers',
                     'variable': 'name given to an object',
                     'directory': 'folder where files are kept',
}

for word, meaning in glossary.items():
    print(f'{word}: {meaning}\n')

rivers = {'nile': 'egypt',
          'niger': 'nigeria',
          'mississippi': 'usa'}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}\n')

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

poll_takers = ['janet', 'tara', 'edward', 'sarah', 'riley']

for person in poll_takers:
    if person in favorite_languages.keys():
        print('Thanks for responding!')
    else:
        print('Here is an invite to take a poll on your favorite programming language')

user_0 = {'username': 'tannie',
          'firstname': 'tolulope',
          'lastname': 'animashaun',
}

user_1 = {'username': 'noobnoob',
          'firstname': 'jamin',
          'lastname': 'galadima',
}

user_2 = {'username': 'lara_annie',
          'firstname': 'lara',
          'lastname': 'animashaun'
}

people = [user_0, user_1, user_2]

for user in people:
    for keys, values in user.items():
        print(f'{keys.title()}: {values.title()}')

pet_1 = {'animal': 'dog',
         'owner\'s name': 'dayo',}
pet_2 = {'animal': 'cat',
         'owner\'s name': 'jamin',}
pet_3 = {'animal': 'tiger',
         'owner\'s name': 'tolu'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for keys, values in pet.items():
        print(f'{keys.title()}: {values.title()}')

favorite_places = {'jamin': ['tank and tummy', 'jollof bay buka', 'japan'],
                   'tolu': ['canada', 'caribbean', 'disney land'],
                   'jemima': ['krispy kreme', 'dunkin\' donuts']}

for name, favorite_place in favorite_places.items():
    print(f'My name is {name.title()} and my favorite places to visit are:')
    for place in favorite_place:
        print(f'{place.title()}')

favorite_numbers ={'Taylor': [13,16,19],
                   'Tolu': [27,28,29],
                   'Tems': [19,26],
                   'Missy': [21,23],
                   'Simeon': [34,35,39]
}

for names, numbers in favorite_numbers.items():
    print(f'My name is {names.title()} andd my favorite numbers are:')
    for number in numbers:
        print(number)

cities = {'vancouver': {
    'country': 'canada',
    'population': 2000000,
    'fact': 'Located in British Columbia'
    },
    'los angeles': {
        'country': 'america',
        'population': 6000000,
        'fact': 'Location of Hollywood'
    },
    'lagos': {
        'country': 'nigeria',
        'population': 14000000,
        'fact': 'Divided into the mainland and island'
    }
          }
for city, info in cities.items():
    print(city.title())
    for keys, values in info.items():
        if keys == 'population':
            print(f'{keys.title()}: {values}')
        elif keys == 'fact':
            print(f'{keys.title()}: {values}')
        else:
            print(f'{keys.title()}: {values.title()}')

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f'Hello {name}!')

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
 message = input(prompt)
 if message != 'quit':
     print(message)

prompt = 'Enter the pizza toppings you would like: '
prompt += '\nEnter quit to complete or cancel your order '


while True:
    pizza_toppings = input(prompt)
    if pizza_toppings == 'quit':
        break
    else:
        print(f'{pizza_toppings} will be added to your pizza')


while True:
    user_age = input('How old are you?: ')
    user_age = int(user_age)

    if user_age < 3:
        print('Your ticket is free')
    elif user_age >= 3:
        print('Your ticket costs $10')
    elif user_age > 12:
        print('Your ticket costs $15')
    break

prompt = '\nEnter quit to exit the program'
prompt += '\nEnter your age to get your ticket price: '
user_age = ''
while user_age != 'quit':
    user_age = input(prompt)
    if user_age == 'quit':
        print(user_age)
    elif int(user_age) < 3:
        print('Your ticket is free')
    elif int(user_age) < 12:
        print('Your ticket costs $10')
    else:
        print('Your ticket costs $15')

active = True

prompt = '\nEnter quit to exit the program'
prompt += '\nEnter your age to get your ticket price: '
user_age = ''
while active:
    user_age = input(prompt)
    if user_age == 'quit':
        active = False
    elif int(user_age) < 3:
        print('Your ticket is free')
    elif int(user_age) < 12:
        print('Your ticket costs $10')
    else:
        print('Your ticket costs $15')

#infinite loop
y = 3
while y <= 3:
    print(y)

sandwich_orders = ['grilled cheese', 'pastrami', 'chicken', 'pastrami', 'veggie', 'tuna', 'pastrami', 'turkey']

finished_sandwiches = []

print('Sorry, The Deli has run out of pastrami sandwich')

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    made_sandwich = sandwich_orders.pop()
    print(f"I made your {made_sandwich} sandwich")
    finished_sandwiches.append(made_sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)

responses = {}
polling_active = True
while polling_active:
    name = input('What is your name: ')
    response = input('If you could visit one place in the world, where would you go? ')
    responses[name] = response
    repeat = input('Would you like to let someone else respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False

print('\nPolling Results')
for name, response in responses.items():
    print(f"\n{name.title()} would like to visit {response.title()}")








