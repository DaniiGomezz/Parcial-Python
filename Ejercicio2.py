#creamos la funcion eliminar_duplicados y le pasamos como parametro una lista
def eliminar_duplicados(lista):
    # Convierte la lista a un conjunto para eliminar los duplicados
    conjunto_sin_repetidos = set(lista)
    # Convierte el conjunto de nuevo a una lista
    lista_sin_repetidos = list(conjunto_sin_repetidos)
    
    #retorna la lista sin los numeros repetidos
    return lista_sin_repetidos

# creamos dicha lista para luego pasarla como parametro a la funcion eliminar_duplicados
lista_original = [1, 2, 3, 4, 4, 5, 6, 6, 7]
lista_sin_repetidos = eliminar_duplicados(lista_original)
print("Lista original:", lista_original)
print("Lista sin repetidos:", lista_sin_repetidos)

