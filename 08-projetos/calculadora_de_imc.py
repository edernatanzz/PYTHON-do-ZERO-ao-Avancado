#calculo de IMC - Indice de Massa Corporal 

'''
qual sua altura em cm:
qual e o seu peso em kg:
'''

altura = float(input('Qual sua altura em cm :'))
peso= float(input( 'Qual e o seu peso em Kg :'))

imc= peso / (altura/100)**2  



if imc < 18.5:
    print('MAGREZA')
elif imc >= 18.5 and imc < 24.9:
    print('NORMAL')
elif imc >= 25.0 and imc < 29.9:
    print('SOBREPESO')
elif imc >= 30.0 and imc < 39.9:
    print('OBESIDADE')
else : 
    print('OBESIDADE GRAVE')


 