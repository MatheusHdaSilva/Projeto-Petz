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
        c =  (12 / quantidade) *valor
        print('Gastando R$:{:.2f} a cada {} meses, o seu gasto anual com areia é de {:.2f}'.format(valor, quantidade, c))
