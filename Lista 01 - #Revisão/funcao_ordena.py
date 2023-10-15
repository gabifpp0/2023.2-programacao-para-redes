
def ordena_lista (nome_lista:str,metodo_ordena:str):
    boolSucesso = False
    retorno = None


    if metodo_ordena == 'Bubble':
        bubble = ordena_bubble(nome_lista)
        resposta = bubble
    elif metodo_ordena == 'Insertion':
        insertion = ordena_insertion(nome_lista)
        resposta = insertion
    elif metodo_ordena == 'Selection':
        selection = ordena_selection(nome_lista)
        resposta = selection
    elif metodo_ordena == 'Quick':
        quick = ordena_quick(nome_lista)
        resposta = quick
    else:
        print('sela')
    
    if resposta[0] == True:
        boolSucesso = True
        retorno = resposta[1]
    else:
        boolSucesso = False
        retorno = None
    return boolSucesso, retorno
# ----------------------------------------------------------------------
#Questão 02
#Bubble
def ordena_bubble (lista:list):
    boolsucesso = False
    retorno = None

    tamanho = len(lista)

    for contagem in range(tamanho -1):
        for elementos in range(tamanho -1):
            if (lista[elementos] > lista[elementos + 1]):
                lista[elementos], lista[elementos + 1] = lista[elementos + 1], lista[elementos]
    
        if (lista[0] > lista[tamanho - 1]):
            boolsucesso = False
            retorno = None
        else: 
            boolsucesso = True
            retorno = lista

    return boolsucesso, retorno, lista
# ----------------------------------------------------------------------
#Questão 02
def ordena_insertion (lista:list):
    boolsucesso = False
    retorno = None

    tamanho = len(lista)

    for contagem in range(tamanho):
        posicao = lista[contagem]
        elemento = contagem - 1
        while elemento >= 0 and lista[elemento] >= posicao:
            lista[elemento + 1] = lista[elemento]
            elemento -= 1
        lista[elemento + 1] = posicao
     
    for elementos in range(tamanho):
        if lista[elementos] > lista[tamanho - 1]:
            boolsucesso = False
            retorno = None
        else:
            boolsucesso = True
            retorno = lista

    return boolsucesso, retorno
# ----------------------------------------------------------------------
#Questão 02
def ordena_selection (lista:list):
    boolsucesso = False
    retorno = None

    tamanho = len(lista)

    for contagem in range(tamanho):
        começo = contagem
        for elementos in range(contagem + 1, tamanho):
            if lista[começo] > lista[elementos]:
                começo = elementos
        lista[contagem], lista[começo] = lista[começo] , lista[contagem]

    for elem in range(tamanho):
        if lista[elem] > lista[tamanho - 1]:
                boolsucesso = False
                retorno = None
        else:
                boolsucesso = True
                retorno = lista
            

    return boolsucesso, retorno
# ----------------------------------------------------------------------
#Questão 02
def ordena_quick ():
    boolsucesso = False
    retorno = None

    ...

    return boolsucesso, retorno