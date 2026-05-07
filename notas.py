# ============================================================
# ETAPA 1: Lista unidimensional de 10 notas
# ============================================================
def etapa1_unidimensional():
    print("\n--- ETAPA 1: Lista de 10 notas ---")
    # 1. Crear lista con 10 notas fijas (entre 0 y 20)
    notas = [15, 8, 12, 19, 5, 20, 3, 14, 10, 7]
    print("Lista original:", notas)

    # 2. Recorrer e imprimir cada nota con su posición
    print("Recorrido completo:")
    for i in range(len(notas)):
        print(f"Posición {i}: {notas[i]}")

    # 3. Modificar la tercera nota (índice 2)
    nueva = int(input("Ingrese una nueva nota (0-20) para la tercera posición: "))
    while nueva < 0 or nueva > 20:
        nueva = int(input("Nota inválida. Debe estar entre 0 y 20: "))
    notas[2] = nueva
    print("Lista luego de modificar:", notas)

    # 4. Buscar una nota ingresada por el usuario
    buscar = int(input("Ingrese una nota a buscar (0-20): "))
    # Si la nota está en la lista, mostrar mensaje
    if buscar in notas:
        print(f"La nota {buscar} SÍ está en la lista.")
    else:
        print(f"La nota {buscar} NO está en la lista.")

# ============================================================
# ETAPA 2: Matriz 3x3 (notas)
# ============================================================
def etapa2_matriz():
    print("\n--- ETAPA 2: Matriz 3x3 de notas ---")
    # 1. Crear matriz 3x3 llena de ceros
    matriz = [[0,0,0], [0,0,0], [0,0,0]]

    # 2. Llenar la matriz con notas ingresadas por el usuario (0-20)
    print("Ingrese 9 notas (0-20) para la matriz:")
    for f in range(3):
        for c in range(3):
            nota = int(input(f"Nota en fila {f}, columna {c}: "))
            while nota < 0 or nota > 20:
                nota = int(input("Nota inválida. Debe ser entre 0 y 20: "))
            matriz[f][c] = nota

    # 3. Mostrar la matriz en forma de tabla
    print("\nMatriz de notas:")
    for f in range(3):
        for c in range(3):
            print(f"{matriz[f][c]:4}", end=" ")
        print()  # salta a la siguiente fila

    # 4. Sumar todos los elementos
    suma = 0
    for f in range(3):
        for c in range(3):
            suma += matriz[f][c]
    print(f"Suma total de todas las notas: {suma}")

# ============================================================
# ETAPA 3: Menú para lista dinámica (insertar, eliminar, buscar, mostrar)
# ============================================================
def etapa3_menu():
    print("\n--- ETAPA 3: Menú interactivo ---")
    lista = []  # lista vacía al inicio

    while True:
        print("\n=== MENÚ DE OPERACIONES ===")
        print("1. Insertar nota al final")
        print("2. Eliminar nota por posición")
        print("3. Buscar nota y mostrar su posición")
        print("4. Mostrar lista completa")
        print("5. Salir de este menú")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nota = int(input("Nota a insertar (0-20): "))
            while nota < 0 or nota > 20:
                nota = int(input("Nota inválida. Debe estar entre 0 y 20: "))
            lista.append(nota)
            print(f"Nota {nota} añadida. Lista actual: {lista}")

        elif opcion == "2":
            if len(lista) == 0:
                print("La lista está vacía, no se puede eliminar.")
                continue
            print(f"Lista actual: {lista}")
            pos = int(input(f"Posición a eliminar (0 a {len(lista)-1}): "))
            if 0 <= pos < len(lista):
                eliminada = lista.pop(pos)
                print(f"Se eliminó la nota {eliminada}. Lista nueva: {lista}")
            else:
                print("Posición no válida.")

        elif opcion == "3":
            if len(lista) == 0:
                print("Lista vacía, no se puede buscar.")
                continue
            buscar = int(input("Nota a buscar: "))
            encontrada = False
            for i in range(len(lista)):
                if lista[i] == buscar:
                    print(f"La nota {buscar} está en la posición {i}")
                    encontrada = True
            if not encontrada:
                print(f"La nota {buscar} no existe en la lista.")

        elif opcion == "4":
            if len(lista) == 0:
                print("La lista está vacía.")
            else:
                print("Lista actual:", lista)

        elif opcion == "5":
            break

        else:
            print("Opción no válida, intenta de nuevo.")

# ============================================================
# ETAPA 4: Algoritmos de ordenamiento (burbuja y selección)
# ============================================================
def etapa4_ordenamiento():
    print("\n--- ETAPA 4: Ordenamiento de notas ---")
    # Lista desordenada de ejemplo (notas entre 0 y 20)
    notas_desordenadas = [14, 5, 19, 2, 8, 11, 20, 3, 16]
    print("Lista original desordenada:", notas_desordenadas)

    # --- ORDENAMIENTO BURBUJA ---
    burbuja = notas_desordenadas.copy()
    n = len(burbuja)
    for i in range(n-1):
        for j in range(n-1-i):
            if burbuja[j] > burbuja[j+1]:
                # Intercambiar
                burbuja[j], burbuja[j+1] = burbuja[j+1], burbuja[j]
    print("Después de Burbuja (ascendente):", burbuja)

    # --- ORDENAMIENTO POR SELECCIÓN ---
    seleccion = notas_desordenadas.copy()
    n = len(seleccion)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if seleccion[j] < seleccion[minimo]:
                minimo = j
        # Intercambiar el mínimo con la posición i
        seleccion[i], seleccion[minimo] = seleccion[minimo], seleccion[i]
    print("Después de Selección (ascendente):", seleccion)

    # Comparación
    if burbuja == seleccion:
        print("Ambos algoritmos dieron el mismo resultado.")
    else:
        print("Los resultados son diferentes. (No debería pasar si están bien implementados)")

# ============================================================
# MENÚ PRINCIPAL
# ============================================================
def main():
    while True:
        print("\n" + "="*40)
        print("LABORATORIO DE PROGRAMACIÓN - NOTAS (0-20)")
        print("="*40)
        print("1. Etapa 1: Lista de 10 notas")
        print("2. Etapa 2: Matriz 3x3 de notas")
        print("3. Etapa 3: Menú para lista dinámica")
        print("4. Etapa 4: Ordenamiento burbuja y selección")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            etapa1_unidimensional()
        elif opcion == "2":
            etapa2_matriz()
        elif opcion == "3":
            etapa3_menu()
        elif opcion == "4":
            etapa4_ordenamiento()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción incorrecta. Elige 1, 2, 3, 4 o 5.")

        input("\nPresiona Enter para continuar...")

# ============================================================
# Punto de entrada del programa
# ============================================================
if __name__ == "__main__":
    main()