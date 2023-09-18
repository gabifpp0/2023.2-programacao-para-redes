import random, os, sys

DIRATUAL = os.path.dirname(__file__)

# ----------------------------------------------------------------------
def gerar_lista(quantidade:int, valor_minimo:int=1, valor_maximo:int=1000000):
    boolSucesso = False
    lstRetorno  = None

    lista = [random.randint(valor_minimo,valor_maximo) for _ in range(quantidade)]
    if len(lista) == quantidade:
        boolSucesso = True
        lstRetorno = lista
    return boolSucesso, lstRetorno

# ----------------------------------------------------------------------

def salvar_lista(nome_lista: list, nome_arquivo: str):
    boolSucesso  = False
    nome_arquivo = DIRATUAL + '\\' + nome_arquivo
    
    arquvo = (open(f'{nome_arquivo}','w'))
    arquvo.write(str(nome_lista)) 
    dirarq = os.path.dirname(nome_arquivo)
    for i in range(len(nome_lista)):
         arquvo.write(str(f"\n{nome_lista[i]}"))
    if dirarq == DIRATUAL:
        boolSucesso = True

    return boolSucesso

def ler_arquivo (nome_arquivo:str):
    boolSucesso = False
    retorno = None

    ...

    return boolSucesso, retorno

def ordena_lista (nome_lista:str,metodo_ordenna:str):
    boolSucesso = False
    retorno = None

    ...

    return boolSucesso, retorno