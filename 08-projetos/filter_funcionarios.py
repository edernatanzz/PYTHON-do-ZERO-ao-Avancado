'''
criar um programa que gera 3 listas de acordo com a nacessidade logo abaxo :

1-lista1= funcionarios que tem carro 
lista2= funcionarios que tem carro e trabalha durante o dia 
lista 3= funcionarios que nao tem carro
'''

funcionarios=['Ana','Marcos', 'Alice','Pedro', 'Sophia', 'Bruno', 'Melissa' ]
turno_dia = ['Ana','Marcos', 'Alice', 'Melissa' ]
turno_noite= ['Pedro', 'Sophia', 'Bruno ']
tem_carro=['Marcos', 'Alice','Bruno', 'Melissa']



lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2=(set(tem_carro).intersection(turno_dia))
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)