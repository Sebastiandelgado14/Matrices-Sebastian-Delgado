
def sumar_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])

    resultado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)

    return resultado


def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])

    resultado = []

    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)

    return resultado


def hadamard_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])

    resultado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] * B[i][j])
        resultado.append(fila)

    return resultado


def kronecker(A, B):
    resultado = []

    for fila_A in A:
        for fila_B in B:
            fila_resultado = []

            for elemento_A in fila_A:
                for elemento_B in fila_B:
                    fila_resultado.append(elemento_A * elemento_B)

            resultado.append(fila_resultado)

    return resultado
