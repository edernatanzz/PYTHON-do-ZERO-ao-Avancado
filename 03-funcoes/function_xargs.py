# varios numeros

def soma(*numeros):
    resultado = 0
    
    for num in numeros :
        resultado += num 
    return (resultado)  # retorna o valor da variavel global "resultado" que foi


x= soma(2,3,4,7)
print(x)