'''
criar loop que imprima os numeros de 1 a 10, mas parar de imprimir assim que
chegar a 5 usando o comando break . Em seguida , crie um segundo loop que imprima
os numeros de 1 a 10 , mas pule impressao do numero 5 usando o comando continue

'''
print('loop com o break: ')
for x in range (1,11):
    if x > 5 :
        break
print(x)

print('loop com o continue:')

for x in range(1,11):
    if x == 5 : 
        continue
    print(x)

