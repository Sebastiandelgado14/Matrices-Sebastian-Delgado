
from entrada import ingresar_matriz, mostrar_matriz
from operaciones_matrices import (
    sumar_matrices,
    multiplicar_matrices,
    hadamard_matrices,
    kronecker
)
from menu import mostrar_menu


while True:
    opcion = mostrar_menu()

    if opcion == 5:
        print("Programa finalizado.")
        break

    print("\nIngrese la primera matriz")
    A = ingresar_matriz()

    print("\nIngrese la segunda matriz")
    B = ingresar_matriz()

    try:
        if opcion == 1:
            if len(A) != len(B) or len(A[0]) != len(B[0]):
                print("Error: las matrices deben tener el mismo tamaño.")
            else:
                resultado = sumar_matrices(A, B)
                mostrar_matriz(resultado)

        elif opcion == 2:
            if len(A[0]) != len(B):
                print("Error: no se pueden multiplicar las matrices.")
            else:
                resultado = multiplicar_matrices(A, B)
                mostrar_matriz(resultado)

        elif opcion == 3:
            if len(A) != len(B) or len(A[0]) != len(B[0]):
                print("Error: las matrices deben tener el mismo tamaño.")
            else:
                resultado = hadamard_matrices(A, B)
                mostrar_matriz(resultado)

        elif opcion == 4:
            resultado = kronecker(A, B)
            mostrar_matriz(resultado)

    except Exception as e:
        print("Ocurrió un error:", e)
