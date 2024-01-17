#Instruções do projeto
#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#Imprimindo os números utilizando for:

numero = 0
for i in range(20):
    numero = numero + 1
    if(numero == 13):
        continue
    else:
        print(numero)

#Imprimindo os números utilizando while:

numero = 1
while(numero <= 20):
    if(numero == 13):
        numero = numero + 1
        continue
    else:
        print(numero)
        numero = numero + 1

#Imprimindo os números em ordem decrescente:

numero = 21
for i in range(20, 0, -1):
    numero = numero - 1
    if(numero == 13):
        continue
    print(numero)
