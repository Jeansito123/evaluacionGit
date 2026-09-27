def ordenar_burbuja(lista):
    """Ordena una lista de números mediante el método burbuja."""
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


datos = [64, 34, 25, 12, 22, 11, 90]
print("Datos originales:", datos)
print("Datos ordenados:", ordenar_burbuja(datos.copy()))
