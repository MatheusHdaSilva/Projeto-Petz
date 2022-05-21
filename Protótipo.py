from time import sleep

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
print('$%$ * 30')
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
    print('''Selecione uma das opções abaixo!!
    [ 1 ] Você compra varios pacotes ao mês?
    [ 2 ] Você estoca um número de pacotes para comprar a cada 2 ou mais?''')
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
    else:
        areia = int(input('Quantos pacotes você estoca?: '))
        areiameses = int(input('Você precisa reestocar o número de {} pacotes de areia a cada quantos meses?: '.format(areia)))
        granulado = int(input('Quantos pacotes você estoca?: '))
        granuladomeses = int(input('Voce precisa reestocar o número de {} pacotes de granulado a cada quantos meses?: '.format(granulado)))
        areiac =  (areia * valor1) 
        areiamesesc = (12 / areiameses) * areiac
        granuladoc = (granulado * valor2)
        granuladomesesc = (12 / granuladomeses) * granuladoc
        total = areiamesesc + granuladomesesc
        print('Gastando R$:{:.2f} em Areia a cada {} meses, e gastando R$:{:.2f} em Granulado Higiênico a cada {} meses.'.format(areiac, areiameses, granuladoc, granuladomeses))
        print('CARREGANDO...')
        sleep(3)
        print('Seu gasto Anual é de R$:{:.2f}'.format(total))

        