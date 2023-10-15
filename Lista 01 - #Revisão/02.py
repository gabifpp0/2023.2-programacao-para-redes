import sys, os
import funcoes

try:
    arquivo = input('arquivo: ')
except:
    print("\nHouve um erro")
    sys.exit()
if not os.path.exists(arquivo):
    print("\n O arquivo não existe")
    sys.exit()
else:
    print("\nO arquivo existe! Iniciando...")
    lendo = funcoes.ler_arquivo(arquivo)
    print(lendo)
    ordenar = str(input('Qual tipo de ordenação deseja usar? '))
    ordenando = funcoes.ordena_lista(lendo[1], ordenar)
    print(ordenando)
