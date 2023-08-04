#filer function 
 #muito ultilizado com listas
 #aplicar uma função a um interable, filtrando os itens. (list , turple, dic etc.)

valores = [ 10, 12 , 34 , 44 , 57]


def remove20 (x):
    return x > 20 


print(list(map(remove20, valores)))




print(list(filter(remove20, valores)))
print(list(filter(lambda x: x > 20 , valores)))