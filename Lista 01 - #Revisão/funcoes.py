import random, os, sys

DIRATUAL = os.path.dirname(__file__)

# ----------------------------------------------------------------------
#Questão 01
def gerar_lista(quantidade:int, valor_minimo:int=1, valor_maximo:int=1000000):
    boolSucesso = False
    lstRetorno  = None

    lista = [random.randint(valor_minimo,valor_maximo) for _ in range(quantidade)]
    if len(lista) == quantidade:
        boolSucesso = True
        lstRetorno = lista
    return boolSucesso, lstRetorno

# ----------------------------------------------------------------------
#Questão 01
def salvar_lista(nome_lista: list, nome_arquivo: str):
    boolSucesso  = False
    nome_arquivo = DIRATUAL + '\\' + nome_arquivo
    
    arquvo = (open(f'{nome_arquivo}','w')) 
    dirarq = os.path.dirname(nome_arquivo)
    for i in range(1,len(nome_lista)):
         arquvo.write(str(f"\n{nome_lista[i]}"))
    if dirarq == DIRATUAL:
        boolSucesso = True

    return boolSucesso

# ----------------------------------------------------------------------
#Questão 02
def ler_arquivo (nome_arquivo:str):
    boolSucesso = False
    retorno = None

    lendo = open(f'{nome_arquivo}')
    linha = open(f'{nome_arquivo}')
    
    lido = lendo.read()
    linhas = len(linha.readlines())
    tamanho = os.path.getsize(nome_arquivo)
    contador = 0
    sem_esp = lido.split('\n')
    
    for i in sem_esp:
        if i:
            contador += 1
    
    if not (tamanho == 0) or not (linhas == 0):
        if (contador + 1) == linhas:
            boolSucesso = True
            retorno = sem_esp[1:linhas]
    else:
        boolSucesso = False
        retorno = None

    return boolSucesso, retorno

# ----------------------------------------------------------------------
#Questão 02
def ordena_lista (nome_lista:str,metodo_ordena:str):
    boolSucesso = False
    retorno = None

    if metodo_ordena == 'Bubble':
        deu = ordena_bubble(nome_lista)
        print('Bubble')
    elif metodo_ordena == 'Insertion':
        print('Insertion')
    elif metodo_ordena == 'Selection':
        print('Selection')
    elif metodo_ordena == 'Quick':
        print('Quick')
    else:
        print('sela')
    return boolSucesso, retorno, deu

def ordena_bubble(lista:list):
    boolSucesso = False
    retorno = None

    tamanho = len(lista)

    for contagem in range(tamanho -1):
        for elementos in range(tamanho -1):
            if (lista[elementos] > lista[elementos + 1]):
                lista[elementos], lista[elementos + 1] = lista[elementos + 1], lista[elementos]

            if lista[elementos] > lista[tamanho]:
                boolsucesso = False
                retorno = None
            else: 
                boolsucesso = True
                retorno = lista

    return boolsucesso, retorno
