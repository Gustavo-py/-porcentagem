print('=-='*20)
print('PROMOÇÂO DO DIA:')
print('=-='*20)
print('Álcool: até 20 litros, desconto de 3% por litro e acima de 20 litros, desconto de 5% por litro. \nGasolina: até 20 litros, desconto de 4% por litro e acima de 20 litros, desconto de 6% por litro.')
print('=-='*20)
print('''SEJA BEM-VINDO AO POSTO PAKETÁ:

        [ 1 ] :A-alcool
        [ 2 ] :G-gasolina
        ''')
print('=-='*20)

pessoa = float(input('Quantos litros voce deseja por? '))

while True:
    gasosa = int(input('QUAL COMBUSTIVEL VOCE DESEJA? '))
    if gasosa == 1:
        if pessoa <=20:
            result = pessoa * 2.19
            resulta = result - ( result * (3 / 100 ))
            print(f'Deu um total de R${resulta:.2f} Obrigado pela preferencia volte sempre.')

        else:
            result = pessoa * 2.19
            resulta = result - ( result * (5 / 100))
            print(f'Deu um total de R${resulta:.2f} Obrigado pela preferencia volte sempre.')
        break
    elif gasosa == 2:
        if pessoa <=20:
            result = pessoa * 2.99
            resultado = result - ( result * (4 / 100 ))
            print(f'Deu um total de R${resultado:.2f} Obrigado pela preferencia volte sempre.')

        else:
            result = pessoa * 2.99
            resultado = result - (result * (6 / 100))
            print(f'Deu um total de R${resultado:.2f} Obrigado pela preferencia volte sempre.')
        break
    else:
        print('COMANDO INVALIDO... POR FAVOR DIGITE UM NUMERO VALIDO')