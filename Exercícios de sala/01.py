import random
#01. Fazer um programa que gere uma lista com n elementos aleatórios e salve em um arquivo com o nome: lista-nao-ordenada.txt

lista = []
elem = int(input('Quantos elementos a lista terá? '))
g = 0
arqui = open('lista-nao-ordenada.txt','a')

while g <= elem:
    números = random.randint(1,1000)
    lista.append(números)
    g += 1
arqui.write(str(f'\n{lista}'))
print(lista)