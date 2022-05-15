print('''COMO VOCÊ CUIDA DA HIGIÊNE DO SEU GATO?    
[ 1 ] Areia simples
[ 2 ] Granulado higiênico
[ 3 ] As duas opções''')
higiene = int(input('Selecione uma das opções?: '))
if higiene == 1:
    valor = float(input('Qual o preço do pacote da areia?: '))
    kg = float(input('Quantos Kg tem o pacote?: '))
    if kg <= 10:
        quantidade = int(input('Quantos você compra por mês?: '))
        c = (kg * quantidade) * 12
        c1 = c * valor
        print('Gastando R${:.2f} no pacote de {}Kg, comprando {} por mês. você tem um gasto anual de R$:{:.2f}'.format(valor, kg, quantidade, c1))
    else:
        quantidade = int(input('Compra a cada quantos mese?: '))
        c =  (12 / quantidade) * valor
        print('Gastando R$:{:.2f} a cada {} meses, o seu gasto anual com areia é de {:.2f}'.format(valor, quantidade, c))
elif higiene == 2:
    valor = float(input('Qual o preço Do saco de Granulado Higiênico?: '))
    kg =  float(input('Quantos Kg tem o pacote?: '))
    if kg <= 15:
        quantidade = int(input('Quantos você compra por mês?: '))
        c = (kg * quantidade) * 12
        c1 =  c * valor
        print('Gastando R$: {:.2f} no pacote de {}Kg, comprando {} por mês. Você tem um gasto anual de {:.2f}'.format(valor, kg, quantidade, c1))
    else: 
       quantidade = int(input('Compra a cada quantos meses?: '))
       c = (12 / quantidade) * valor
       print('Gastando R$:{:.2f} a cada {} meses, o seu gasto anual com Granulado Higiênico é de {:.2f}'.format(valor, quantidade, c))
else:
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
        print('Gastando {:.2f} em areia de Tantos Kg{} e {:.2f} em granulado higiênico de {}Kg. Você tem o gasto anual de {:.2f}'.format(valor1, kg1, valor2, kg2, c))
        