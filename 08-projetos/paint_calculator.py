'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
o usuario deverá fornecer as seguintes informações:
Rendimento, altura e largura.
O programa devera mostrar na tela a mensagem você necessita de x latas de tinta


'''
redimento= int(input("qual e o redimento da lata : "))
altura = int(input('qual e a altura da parede :'))
largura = int(input('qual e a largura da parede :'))

def calculo_tinta ():
   area =  altura * largura / redimento  
   print(f'Voce prescisa de {area} latas de tinta.')

calculo_tinta()
