# CRIA LISTA COM 1000 PRIMEIROS NUMEROS
numeros = list(range(1, 1001))

# CRIA LISTAS DE PARES E IMPARES
impar = []
par = []

#PERCORRE A PRIMEIRA LISTA SEPARANDO NAS DE PARES E IMPARES
for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

#RETORNA LISTA DE PARES E IMPARES
print("IMPARES: ", impar)
print("PARES: ", par)

#IMPORTA FUNÇÃO QUE DETERMINA SE UM NUMERO É PRIMO OU NÃO
from sympy import isprime

somaPrimos = 0 #DECLARA VARIÁVEL QUE ARMAZENA A SOMA DE PRIMOS

#PERCORRE A LISTA ENCONTRANDO PRIMOS E SOMANDO ELES
for i in numeros:
    if isprime(i):
        somaPrimos += i

#RETORNA A SOMA DOS PRIMOS
print("\nA soma dos primos nos 1000 primeiros numeros é ",somaPrimos)






