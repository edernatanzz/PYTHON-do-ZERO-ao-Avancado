
cor_cliente = input('digite a cor desejada : ')
cores= ['amarelo','verde','azul', 'vermelho']

if cor_cliente.lower() in cores: #lower = padrao de letra minuscula 
    print(f'a cor {cor_cliente} esta disponivel em estoque')
else:
    print(f'a cor {cor_cliente} não disponivel  em estoque')