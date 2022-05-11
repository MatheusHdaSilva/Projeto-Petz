from select import select

print('''GASTO ANUAL COM SEU PET!
[ 1 ] Gato 
[ 2 ] Cachorro''')
select = int(input('Qual o seu Pet?: '))
if select == 1:
    gatos = int(input('Qauntos gatos você tem?: '))
    ração = float(input('Qual o valor da Ração: '))
    rkg = int(input('Quantos KG é o pacote da Ração?: '))