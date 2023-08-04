
from sys import getsizeof 
#uma forma mais rapida para Listas , dicionarios e etc 
#menos memoria 
#valores em bytes

numeros = [x * 10 for x in range(100)] 
print(type(numeros))
#print(numeros)

print(getsizeof(numeros))


print('-----------------------')



numeros = (x * 10 for x in range(100))
print(type(numeros))
#print(list(numeros))
print(getsizeof(numeros))
