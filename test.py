'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado. peça a digitação novamente até ter um valor correto.
'''

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()

print(f'Sexo {sexo} registrado com sucesso!')