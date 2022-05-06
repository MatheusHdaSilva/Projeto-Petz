print('Gasto Anual com seu Pet')
g = int(input('Quantos gastos você tem?: '))
r = float(input('qual o valor da Ração: '))
r1 = int(input('Quantos Kg?: '))
if r1 <+ 5 and 1:
   r2 = int(input('Quantos você compra por mês?: '))
   c = (r1 * r2) * 12
   c1 = c * r
   print('Gastando R$:{:.2f} em uma ração de {} KG, você tem um gasto anual de R${:.2f}'.format(r, r1, c1))
elif r1 >= 10:
   r3 = int(input('Compra a cada quantos meses?: ')) 
   c = 12 / r3
   c1 = c * r
   print('Gastando R$:{:.2f} a cada {} meses você tem um gasto anual de R${:.2f}'.format(r, r3, c1))
print('*-' * 30)
a = float(input('Qual o valor da areia?: '))
a1 = int(input('Quantos KG?: '))
if a <= 12 and 4:
   a2 = int(input('Compra quantas por mês?: '))
   c = (a1 * a2) * 12
   c1 = c * a
   print('Gastando R${:.2f} em cada areia e comprando {} por mês você tem um gasto anual de {:.2f}'.format(a, a2, c1))
elif a >= 20:
   a3 = int(input('Compra a cada quantos meses?: '))
   c = 12 * a3
   c1 = c * a 
   print('Gastando R$:{:.2f} a cada {} meses seu gasto anual com areia é {:.2f}'.format(a1, a3, c1))