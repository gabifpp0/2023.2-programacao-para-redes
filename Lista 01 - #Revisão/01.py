import sys
import funcoes

# ----------------------------------------------------------------------
# Gerando uma lista N elementos com valores entre 1 e 1.000.000
try:
    n     = int(input('Informe a quantidade de elementos da lista: '))
    v_min = int(input('Informe o menor valor da lista: '))
    v_max = int(input('Informe o maior valor da lista: '))
except ValueError:
    print('\nERRO: O Valor informado não é um inteiro válido...\n')
    sys.exit()
except:
    print(f'\nERRO DESCONHECIDO: {sys.exc_info()[0]}')
    sys.exit()
else:
    retGerarLista = funcoes.gerar_lista(n, v_min, v_max)
    print(retGerarLista)

# ----------------------------------------------------------------------
# Excrevendo a lista em um arquivo

if retGerarLista[0] == True:
    retSalvarArquivo = funcoes.salvar_lista(retGerarLista[1], 'valores_nao_ordenados.txt')
    print(retSalvarArquivo)
else:
    print('\nNão foi possível salvar o arquivo pois a lista não foi gerada')
if retSalvarArquivo == True:
    print('\nArquivo Salvo com Sucesso...')
else:
<<<<<<< HEAD
    print('\nNão foi possível salvar o arquivo')
=======
    print('\nNão foi possível salvar o arquivo')
>>>>>>> f0a9a7746b3fdec06b8779a8ebf8c2f0fe646c4d
