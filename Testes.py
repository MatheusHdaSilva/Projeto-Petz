
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
        
        
