print('''!!!GASTO ANUAL COM SEU PET!!!
!!!Selecione uma das Opções abaixo!!!
[ 1 ] Gato 
[ 2 ] Cachorro''')
select = int(input('Qual o seu Pet?: '))
if select == 1:
    gatos = int(input('Quantos gatos você tem?: '))
    ração = float(input('Qual o valor da Ração?: '))
    rkg = float(input('Quantos KG é o pacote da Ração?: '))
    if rkg <= 5:
        quantidade = int(input('Quantos pacotes você compra por mês?: '))
        c = (rkg * quantidade) * 12
        c1 = c * ração
        print('Gastando R$: {:.2f} em um pacote de ração de {}KG, você tem um gasto anual de R$: {:.2f}'.format(ração, rkg, c1))
    elif rkg >=10:
        meses = int(input('Você compra esse pacote de {}KG a cada quantos meses?: '.format(rkg)))
        c = (12 / meses) * ração
        print('Gastando R$: {:.2f} em um pacote de ração de {}KG, Você tem o gasto anual de R$: {:.2f}'.format(ração, rkg, c))




        if kg <= 15:
            quantidade = int(input('Quantos você compra por mês?: '))
        c = (kg * quantidade) * 12
        c1 =  c * valor
        print('Gastando R$: {:.2f} no pacote de {}Kg, comprando {} por mês. Você tem um gasto anual de {:.2f}'.format(valor, kg, quantidade, c1))
    else: 
       quantidade = int(input('Compra a cada quantos meses?: '))
       c = (12 / quantidade) * valor
       print('Gastando R$:{:.2f} a cada {} meses, o seu gasto anual com Granulado Higiênico é de {:.2f}'.format(valor, quantidade, c))
    