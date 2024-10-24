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

balance = 945.70

while True:
    try:
        num = float(input('Deposit: '))
        break
    except ValueError:
        print('Must be a valid quantity.')

balance += num
print(f'balance: {balance}')