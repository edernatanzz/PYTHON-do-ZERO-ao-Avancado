# criar um script que solicite ao usuario dois numeros.Em seguida , seu script deve imprimir a soma, a subtração, multiplicação,
#a divisao em resultado decimal e exponenciação desses 2

number1=float(input('digite um numero :'))
number2=float(input('digite outro numero :'))

soma=number1+number2
subtracao=number1-number2
multiplicacao= number1 * number2
divisao= float(number1 / number2) 
exponenciacao = number2 ** number1


print(f'soma--->{soma}\nsubtracao--->{subtracao}\nmultiplicacao--->{multiplicacao}\ndivisao --->:{divisao}\nexponenciacao--->{exponenciacao}')