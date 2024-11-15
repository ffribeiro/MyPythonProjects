'''
Python: check if number is Even or Odd
'''

# number = int(input('Type a number: '))

# ## Junior DEV
# # if number % 2 == 0:
# #     print('EVEN')
# # else:
# #     print('ODD')

# ## Senior DEV
# print(f'EVEN' if number % 2 == 0 else 'ODD')

'''
Remove www from a list of domains
'''

# links = [
#     'www.b001.io',
#     'www.youtube.com',
#     'www.google.com',
#     'www.wikipedia.org'   
# ]

# for link in links:
#     print(link.removeprefix('www.'))

'''
While method
'''

# balance = 945.70

# while True:
#     try:
#         num = float(input('Deposit: '))
#         break
#     except ValueError:
#         print('Must be a valid quantity.')

# balance += num
# print(f'balance: {balance}')

'''
Swapping two varibles without a temporary variable
'''

# a = 5 
# b = 10

# # swapping without a temporary variable
# a, b = b, a

# print('After swapping')
# print('a =', a)
# print('b =', b)



# balance = 945.70

# while True:
#     try:
#         num = float(input('Deposit: '))
#         break
#     except ValueError:
#         print('Must be a valid quantity.')

# balance += num
# print(f'balance: {balance}')

'''
function
'''

# def add (x,y):
#     return x+y
# print(add(1,2))

'''
lambda function
'''
# print((lambda x,y: x+y) (1,2))

'''
From a list of numbers, move zero to the end of the list
'''
# list = [1, 0, 2, 0, 4, 6]

# for item in list:
#     if item == 0:
#         list.remove(item)
#         list.append(item)
# print(list)

'''
Access list sample
'''
# name = "Pedro"
# if name in['João', 'Paulo', 'Marcus']:
#     print("Access granted")
# else:
#     print("Acess denied")

'''
Function to create a tree
'''
# # height = 6
# # 6 * 2 = 12 - 1 = 11

# def tree(height):
#     # your code goes here
#     lenght = height * 2 - 1
#     stars = 1
#     for i in range(1, height + 1):
#         print(("*" * stars).center(lenght))
#         stars += 2
#     print("*".center(lenght))

# tree(6)

'''
Types of collections
'''

# # Lista é uma coleção ordenada e mutável. Permite membros duplicados
# # index    0        1   2   3
# lista = ['carro', True, 2, 3.5]
# print(lista)
# print(type(lista))
# print(lista[0])
# print('-' * 30)

# # Tupla é uma coleção ordenada e imutável ou seja eu não posso alterar ou remover items da coleção. Permite membros duplicados
# # index     0      1    2   3
# tupla = ('carro', True, 2, 3.5)
# print(tupla)
# print(type(tupla))
# print(tupla[3])
# print('-' * 30)

# # O dicionário é uma coleção ordenada e multável, Nehnum membro duplicado
#               #Chave   Valor
# dicionario = {'nome': 'carro', 'logica': True, 'numero': 2, 'outroNumero': 3.5}
# print(dicionario)
# print(type(dicionario))
# print(dicionario['logica'])
# print('-' * 30)

# # Set é uma coleção não ordenada e não indexada. Nehum membro duplicado
# conjuto = {'carro', True, 2, 3.5}
# print(conjuto)
# print(type(conjuto))

'''
5 Useful f Strings Tricks
https://docs.python.org/3/library/string.html#formatspec
'''
##### TRICK 1 ####
# name = "Alice"
# age = 30

# # Using the old format method
# old_format = "Hello, my name is {} and I am {} years old".format(name, age)
# print("Using format method:", old_format)

# # Using f-strings
# f_string = f"Hello, my name is {name} and I am {age} years old."
# print("Using f-strings:", f_string)

##### TRICK 2 ####
# from datetime import datetime

# price = 1234.56789
# print(f"The price is ${price:.2f}")

# large_number = 1000000
# print(f"{large_number:,}")

# now = datetime.now()
# print(f"Today's date is {now:%y-%m-%d}")

##### TRICK 2 ####
'''Text alignment'''

# name = "Alice"
# name2 = "Bob"

# print(f"{name:<10}")    # Left-align within 10 charcters
# print(f"{name2:<10}")
# print("-----------")

# print(f"{name:>10}")    # Right-align within 10 charcters
# print(f"{name2:>10}")
# print("-----------")

# print(f"{name:^10}")    # Center-align within 10 charcters
# print(f"{name2:^10}")
# print("-----------")

##### TRICK 3 ####
'''Format a table'''

data = [
    {"Name": "Alice", "Age": 30, "Occupation": "Engineer"},
    {"Name": "Bob", "Age": 24, "Occupation": "Designer"},
    {"Name": "Charlie", "Age": 29, "Occupation": "Doctor"},
    {"Name": "David","Age": 35, "Occupation": "Teacher"}
]

print(f"{'Name':<10} {'Age':<5} {'Occupation':<15}")
print("-" * 30)

for person in data:
    print(f"{person['Name']:<10} {person['Age']:<5} {person['Occupation']:<15}")