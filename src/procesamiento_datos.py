def filtar_por_participante(id, lista):
    '''
    A partir de un ID suministrado previamente,
    esta función se encarga de buscar un diccionario
    en una lista de dicc que tenga esa clave. Despues,
    la función devuelve ese mismo dicc.

    Parametros:
    id: str
    Es el id suministrado por el usuario.
    lista: list
    es la lista de diccionarios de cada participante

    Returns:
    dicc: dict
    Es el diccionario que contiene el ID suministrado
    None: NoneType
    En caso de que el ID no se encuentre en la lista,
    devuelve un None.
    '''
    for dicc in lista:
        if id == dicc["ID"]:
            return dicc

    return None

