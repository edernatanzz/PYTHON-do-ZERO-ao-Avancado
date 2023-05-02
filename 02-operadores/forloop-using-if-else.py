compra_confirmada=True
dados_compra= "Compra realizada no valor de R$12.50 e entrega confirmada "


for enviar in range(3):
    if compra_confirmada:
     print(dados_compra)
     print("detalhes enviados para o seu email ")
    break
else:
  print("erro na compra ")


