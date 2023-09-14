import random, os

DIRATUAL = os.path.dirname(os.path.abspath(__file__)) 

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

    nome_arquivo = open(f'{nome_arquivo}','w')
    nome_arquivo.write(str(nome_lista))
    dir_ar = os.path.dirname(nome_arquivo)
    if dir_ar == DIRATUAL:
        boolSucesso = True

    return boolSucesso