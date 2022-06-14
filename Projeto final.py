from time import sleep

print('''!!!GASTO ANUAL COM SEU PET!!!
!!!Selecione uma das Opções abaixo!!!
[ 1 ] Gato 
[ 2 ] Cachorro''')
select = int(input('Qual o seu Pet?: '))
if select == 1:
    if select == 1:
        gatos = int(input('Quantos gatos você tem?: '))
        valor = float(input('Qual o valor da Ração?: '))
        kg = float(input('Quantos KG é o pacote da Ração?: '))
        print('''Selecione uma das Opções a baixo!!!
        [ 1 ] Você compra varios pacotes ao mês?
        [ 2 ] você estoca um número de pacotes para comprar a cada 2 ou mais?''')
        select = int(input('Escolha!!: '))
        if select == 1:
            quantidade = int(input('Quantos pacotes você compra no mês?: '))
            c = (quantidade * valor) * 12
            print('Gastando R$:{:.2f} no pacote de {}Kg se anual com Ração é...'.format(valor, kg))
            print('CARREGANDO...')
            sleep(3)
            print('Gasto Anual de R$:{:.2f}'.format(c))
        else:
            ração = int(input('Quantos pacotes de Ração você estoca no Mês: '))
            raçãomeses = int(input('Você reestoca o número de {} pacotes de Ração a cada quantos meses?: '.format(ração)))
            raçãoc = (ração * valor)
            raçãomesesc = (12 / raçãomeses) * raçãoc
            print('Gastando R$:{:.2f} em Ração de {} kg a cada {} meses o seu gasto anual é de...'.format(valor, kg, raçãomeses))
            print('CARREGANDO...')
            sleep(3)
            print('Você tem o gasto anual de {:.2f}'.format(raçãomesesc))
    print('=' * 90)
    print('''COMO VOCÊ CUIDA DA HIGIÊNE DO SEU GATO?    
    [ 1 ] Areia simples
    [ 2 ] Granulado higiênico
    [ 3 ] As duas opções''')
    higiene = int(input('Escolha!!: '))
    if higiene == 1:
        valor = float(input('Qual o preço do pacote da areia?: '))
        kg = float(input('Quantos Kg tem o pacote?: '))
        print('''Selecione uma das opções abaixo!!!
        [ 1 ] Você compra varios pacotes ao mês?
        [ 2 ] Você estoca um número de pacotes para comprar a cada 2 ou mais?''')
        select = int(input('Escolha!!:'))
        if select == 1:
            quantidade = int(input('Quantos pacotes você compra no mês?: '))
            c = (quantidade * valor) * 12
            print('Gastando R$:{:.2f} no pacote de {}Kg seu gasto anual com Areia é!'.format(valor, kg))
            print('CARREGANDO...')
            sleep(3)
            print('Gasto anual de R$:{:.2f}'.format(c))
        else:
            areia = int(input('Quantos pacotes de areia você estoca?: '))
            areiameses = int(input('Você reestoca o número de {} pacotes de Areia a cada quantos meses?: '.format(areia)))
            areiac = (areia * valor)
            areiamesesc = (12 / areiameses) * areiac
            print('Gastando R$:{:.2f} em Areia cada {} meses.'.format(valor, areiameses))
            print('CARREGANDO...')
            sleep(3)
            print('Você tem o gasto anual de {:.2f}'.format(areiamesesc))
    elif higiene == 2:
        valor = float(input('Qual o preço do saco de Granulado Higiênico?: '))
        kg =  float(input('Quantos Kg tem o pacote?: '))
        print('''Selecione uma das opções abaixo!!!
        [ 1 ] Você compra varios pacotes ao mês?
        [ 2 ] Você estoca um número de pacotes para comprar a cada 2 ou mais?''')
        select = int(input('Escolha!!:'))
        if select == 1:
            quantidade = int(input('Quantos pacotes você compra no mês?: '))
            c = (quantidade * valor) * 12
            print('Gastando R$:{:.2f} no pacote de {}Kg seu gasto anual com Granulado higiênico é!'.format(valor, kg))
            print('CARREGANDO...')
            sleep(3)
            print('Gasto anual de R$:{:.2f}'.format(c))
        else:
            granulado = int(input('Quantos pacotes de Granulado higiênico você estoca no mês?:'))
            granuladomeses = int(input('Você reestoca o número de {} pacotes de Granulado a cada quantos meses?: '.format(granulado)))
            granuladoc = (granulado * valor)
            granuladomesesc = (12 / granuladomeses) * granuladoc
            print('Gastando R$:{:.2f} em Granulado Higiênico de {}Kg a cada {} meses.'.format(valor, kg, granuladomeses))
            print('CARREGANDO...')
            sleep(3)
            print('Você tem o gasto anual de {:.2f}'.format(granuladomesesc))
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
            print('Gastando {:.2f} em areia de Tantos Kg{} e {:.2f} em granulado higiênico de {}Kg.'.format(valor1, kg1, valor2, kg2))
            print('CARREGANDO...')
            sleep(3)
            print('Você tem o gasto anual de {:.2f}'.format(c))
        else:
            areia = int(input('Quantos pacotes você estoca de Areia?: '))
            areiameses = int(input('Você precisa reestocar o número de {} pacotes de areia a cada quantos meses?: '.format(areia)))
            granulado = int(input('Quantos pacotes você estoca de Granulado Higiênico?: '))
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
else:    
    if select == 2:
        cachorro = int(input('Quantos cachorros você tem?: '))
        valor = float(input('Qual o valor da Ração?: '))
        kg = float(input('Quantos KG é o pacote da Ração?: '))
        print('''Selecione uma das Opções a baixo!!!
        [ 1 ] Você compra varios pacotes ao mês?
        [ 2 ] você estoca um número de pacotes para comprar a cada 2 ou mais?''')
        select = int(input('Escolha!!: '))
        if select == 1:
            quantidade = int(input('Quantos pacotes você compra no mês?: '))
            c = (quantidade * valor) * 12
            print('Gastando R$:{:.2f} no pacote de {}Kg se anual com Ração é...'.format(valor, kg))
            print('CARREGANDO...')
            sleep(3)
            print('Gasto Anual de R$:{:.2f}'.format(c))
        else:
            ração = int(input('Quantos pacotes de Ração você estoca no Mês: '))
            raçãomeses = int(input('Você reestoca o número de {} pacotes de Ração a cada quantos meses?: '.format(ração)))
            raçãoc = (ração * valor)
            raçãomesesc = (12 / raçãomeses) * raçãoc
            print('Gastando R$:{:.2f} em Ração de {} kg a cada {} meses o seu gasto anual é de...'.format(valor, kg, raçãomeses))
            print('CARREGANDO...')
            sleep(3)
            print('Você tem o gasto anual de {:.2f}'.format(raçãomesesc))
    print('=' * 90)
    print('''COMO VOCÊ CUIDA DA HIGIÊNE DO SEU CACHORRO?    
    [ 1 ] Jornal
    [ 2 ] Tapete Higiênico
    [ 3 ] As duas opções''')
    higiene = int(input('Escolha!!: '))
    if higiene == 1:
        valor = float(input('Qual o preço do pacote da Jornal?: '))
        folhas = float(input('Quantos Folhas de Jornal vem?: '))
        print('''Selecione uma das opções abaixo!!!
        [ 1 ] Você compra varios pacotes de folha ao mês?
        [ 2 ] Você estoca um número de pacotes para comprar a cada 2 ou mais?''')
        select = int(input('Selecione uma das opção!:'))
        if select == 1:
            quantidade = int(input('Quantos pacotes você compra no mês?: '))
            c = (quantidade * valor) * 12
            print('Gastando R$:{:.2f} no pacote de {}folhas seu gasto anual com jornal é!'.format(valor, folhas))
            print('CARREGANDO...')
            sleep(3)
            print('Gasto anual de R$:{:.2f}'.format(c))
        else:
            folhas = int(input('Quantos pacotes de areia você estoca?: '))
            folhasmeses = int(input('Você reestoca o número de {} pacotes de Areia a cada quantos meses?: '.format(folhas)))
            folhasc = (folhas * valor)
            folhasmesesc = (12 / folhasmeses) * folhasc
            print('Gastando R$:{:.2f} em folhas de jornal a cada {} meses.'.format(valor, folhasmeses))
            print('CARREGANDO...')
            sleep(3)
            print('Você tem o gasto anual de {:.2f}'.format(folhasmesesc))
    elif higiene == 2:
        valor = float(input('Qual o preço do saco de Tapete Higiênico?: '))
        unidades =  float(input('Quantas unidades tem o pacote?: '))
        print('''Selecione uma das opções abaixo!!!
        [ 1 ] Você compra varios pacotes ao mês?
        [ 2 ] Você estoca um número de pacotes para comprar a cada 2 ou mais?''')
        select = int(input('Escolha!: '))
        if select == 1:
            quantidade = int(input('Quantos pacotes você compra no mês?: '))
            c = (quantidade * valor) * 12
            print('Gastando R$:{:.2f} no pacote de {} Unidades seu gasto anual com Tapete higiênico é!'.format(valor, unidades))
            print('CARREGANDO...')
            sleep(3)
            print('Gasto anual de R$:{:.2f}'.format(c))
        else:
            tapete = int(input('Quantos pacotes de Tapete higiênico você estoca no mês?:'))
            tapetemeses = int(input('Você reestoca o número de {} pacotes de tapete a cada quantos meses?: '.format(tapete)))
            tapetec = (tapete * valor)
            tapetemesesc = (12 / tapetemeses) * tapetec
            print('Gastando R$:{:.2f} em tapete Higiênico de {} unidades a cada {} meses.'.format(valor, unidades, tapetemeses))
            print('CARREGANDO...')
            sleep(3)
            print('Você tem o gasto anual de {:.2f}'.format(tapetemesesc))
    else:
        valor1 = float(input('Qual o valor da Jornal?: '))
        folhas1 = float(input('Quantas folhas vem no Pacote?: '))
        valor2 = float(input('Qual o valor do Tapete Higiênico?:'))
        tapetes2 = float(input('Quantas Unidades tem o pacote?: '))
        print('''Selecione uma das opções abaixo!!
        [ 1 ] Você compra varios pacotes ao mês?
        [ 2 ] você estoca um número de pacotes para comprar a cada 2 meses ou mais?''')
        select = int(input('Escolha!: '))
        if select == 1:
            folhas = int(input('Quantos pacotes de Jornal você compra?: '))
            tapetes = int(input('Quantos pacotes de Tapete Higiênico você compra?: '))
            c =  (folhas* valor1) * 12 + (tapetes * valor2) * 12
            print('Gastando {:.2f} em Jonal de {} folhas e {:.2f} em Tapete higiênico de {}Kg.'.format(valor1, folhas, valor2, tapetes))
            print('CARREGANDO...')
            sleep(3)
            print('Você tem o gasto anual de {:.2f}'.format(c))
        else:
            folhas = int(input('Quantos pacotes você estoca de jornal?: '))
            folhasmeses = int(input('Você precisa reestocar o número de {} pacotes de jornal a cada quantos meses?: '.format(folhas)))
            tapete = int(input('Quantos pacotes você estoca de Tapete Higiênico?: '))
            tapetemeses = int(input('Voce precisa reestocar o número de {} pacotes de tapete a cada quantos meses?: '.format(tapete)))
            folhasc =  (folhas * valor1) 
            folhasmesesc = (12 / folhasmeses) * folhasc
            tapetec = (folhas * valor2)
            tapetemesesc = (12 / tapetemeses) * tapetec
            total = folhasmesesc + tapetemesesc
            print('Gastando R$:{:.2f} em Folhas de jornal a cada {} meses, e gastando R$:{:.2f} em Tapete Higiênico a cada {} meses.'.format(folhasc, folhasmeses, tapetec, tapetemeses))
            print('CARREGANDO...')
            sleep(3)
            print('Seu gasto Anual é de R$:{:.2f}'.format(total))
