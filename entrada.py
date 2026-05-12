
def ingresar_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número válido.")


def ingresar_matriz():
    filas = int(ingresar_numero("Ingrese el número de filas: "))
    columnas = int(ingresar_numero("Ingrese el número de columnas: "))

    matriz = []

    print("Ingrese los elementos de la matriz:")

    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = ingresar_numero(f"Elemento [{i}][{j}]: ")
            fila.append(numero)
        matriz.append(fila)

    return matriz


def mostrar_matriz(A):
    print("\nMatriz:")

    for fila in A:
        for elemento in fila:
            print(f"{elemento:.2f}", end="\t")
        print()
