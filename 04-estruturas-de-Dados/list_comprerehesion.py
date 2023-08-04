# List compresehension  

#mais simples de se escrever
#ultilizado quando você prescisa criar uma nova lista a partir de uma existente 
#Expressao for item in itens

frutas1 = ['abacate', 'banana' , 'morango', 'kiwi', 'abacaxi']
frutas2 = []

#for busca in frutas1:
 #   if 'a' in busca:
  #      frutas2.append(busca)


frutas2 = [busca for busca in frutas1 if 'n' in busca ]
print(frutas2)






