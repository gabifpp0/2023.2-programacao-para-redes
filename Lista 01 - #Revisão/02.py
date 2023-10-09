import sys, os
import funcoes

try:
    arquivo = str(input('arquivo:'))
except:
    print('\nalgum erro aí')
    sys.exit()
if not os.path.exists(arquivo):
    print('\nO arquivo não existe!')
    sys.exit()
else:
    print('\nO arquivo existe!!!')
    lendoarquivo = funcoes.ler_arquivo(arquivo)
