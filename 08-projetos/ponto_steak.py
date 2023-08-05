'''
Criar um programa que dependendo da temperatura do steak ele retorna o ponto de cozimento em portugues. O usuario devera fornecer a temperatura

'''


while True:
    try:
        x = float(input('Digite a temperatura: '))

        if x > 160:
            print('Well done(Bem Passada)')
        elif x > 150:
            print('Medium well(Ao ponto para o bem)')
        elif x > 140:
            print('Medium(Ao ponto )')
        elif x > 130:
            print('Medium rare(Ao ponto para o mal)')
        elif x > 120:
            print('Rare(selada)')
        else:
            print('A temperatura não esta dentro da faixa, deixe por mais alguns minutos.')

        print(x)
        break  # Exit the loop after processing the input
    except ValueError:
        print('valor digitado Invalido. por valor entre com um valor numerico .')
