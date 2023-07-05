# parametros=> argumentos 


'''
def boas_vindas_usuario1():
    print('ola usuario 1');
    print('Temos 5 laptops em estoque')
    
    
def boas_vindas_usuario2():
    print('ola usuario 2');
    print('Temos 4 laptops em estoque')
    
def boas_vindas_usuario3():
    print('ola usuario 3');
    print('Temos 3 laptops em estoque')    
    
boas_vindas_usuario1()
boas_vindas_usuario2()
boas_vindas_usuario3()

'''



def boas_vindas(nome, quantidade):
    
    print(f'Ola {nome}.');
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Usuario 1' , 5)
boas_vindas('Usuario 2' , 4)
boas_vindas('Usuario 3' , 3)
