valor_compra = float(input('Informe o valor da compra: R$ '))
cadastro_de_fidelidade = input('Cliente possui cadastro de Fidelidade ? [s/n]: ')

if valor_compra > 100 or cadastro_de_fidelidade == 's':
    print('Você acabou de ganhar um BRINDE!!!')

else:
    print('Infelizmente você não ganhará o seu brinde, que tal fazermos um cadastro para o Programa de Fidelidade?')
