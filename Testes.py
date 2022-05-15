
valor1 = float(input('Qual o valor da areia?: '))
kg1 = float(input('Quantos Kg tem a areia?: '))
valor2 = float(input('Qual o valor do Granulado Higiênico?:'))
kg2 = float(input('Quantos Kg tem o Granulado?: '))
print('''Selecione uma das opções abaixo!!
[ 1 ] Você compra varios pacotes ao mês?
[ 2 ] você estoca um número de pacotes para comprar a cada 2 meses ou mais?''')
select = int(input('Sua escolha: '))
if select == 1:
    areia = int(input('Quantos pacotes de areia você compra?: '))
    granulado = int(input('Quantos pacotes de granulado você compra?: '))
    c =  (areia * valor1) * 12 + (granulado * valor2) * 12
    print(c)