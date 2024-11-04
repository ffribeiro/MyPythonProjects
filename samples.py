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