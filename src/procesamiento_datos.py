def filtar_por_participante(id_participante, lista):
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
    
    Raises:
    ValueError: Exception 
    Si el ID es erroneo.
    '''

    for dicc in lista:        
        if dicc["ID"]==id_participante:
            return dicc
    
    raise ValueError("Id erroneo")

