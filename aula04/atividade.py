valor_compra = float(input('Informe o valor da compra: '))


if valor_compra > 250:
    desconto = valor_compra * 0.16
    valor_a_pagar = valor_compra - desconto 
    print(f'O valor do seu desconto será de R$ {desconto:.2f}')
    print(f'O valor a pagar será R$ {valor_a_pagar:.2f}')

else:
    print(f'O valor a pagar será R$ {valor_compra:.2f}')

    