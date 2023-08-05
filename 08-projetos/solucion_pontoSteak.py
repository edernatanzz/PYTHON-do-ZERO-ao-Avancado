

'''Criar um programa que dependendo da temperatura do steak ele retorna o ponto de cozimento em portugues. O usuario devera fornecer a 

Temperaturas - cozimento 
120F ou 48C (rare/selada)
130f ou 54c medium rare (ao ponto para o mal )
140f ou 60c medium(ao ponto)
150f ou 65c medium well (ao ponto para o bem )
60f ou 71c Well done(bem passada )
'''

tem_cell = int(input('qual a temperatura da carne? '))

if tem_cell < 48:
    print(' A carne deverá ficar por alguns minutos')
elif tem_cell in range (48, 53):
    print('Selada')
elif tem_cell in range (54, 59):
    print('ao ponto para o mal')
elif tem_cell in range (60, 64):
    print('Ao ponto')
elif tem_cell in range (65, 70):
    print('ao ponto para o bem')
elif tem_cell >= 71:
    print("Bem passada")




