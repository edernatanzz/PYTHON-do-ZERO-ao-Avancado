# while loops
# exelente para loops dependentes de uma condição
#criar uma promoção para um produto no valor de R$100 com custo de 20 

valor = 100
dia = 0


while valor > 20 :
    dia += 1
    print(f'no dia {dia} o produto vai ser vendido por R${valor}')
    valor -=5
    