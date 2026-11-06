vendas = int(input('Informe os valor de VENDAS: '))
salario = int(input('Informe o valor de seu salario: '))

if vendas >= 1000:
    bonus = 150
    salario = salario + bonus
    print(f'Seu salário será de R$ {salario:.2f}')

elif vendas >= 500:
    bonus = 75
    salario = salario + bonus
    print(f'Seu salário será de R$ {salario:.2f}')

else:
    print(f'Seu salario será de R$ {salario:.2f}')




