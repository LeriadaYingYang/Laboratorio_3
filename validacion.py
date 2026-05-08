# =======================================
# Módulo: validacion.py
# Autor: [Fabrizio]
# Descripción: Función para validar promedios de estudiantes
# =======================================


lista_promedios = []

tabla_estudiantes = []


# =========================
# VALIDAR PROMEDIO
# =========================

def validar_promedio(promedio):

    if promedio >= 18:
        return "A", "Excelente"
    elif promedio >= 14:
        return "B", "Aprobado"
    elif promedio >= 11:
        return "C", "Regular"
    else:
        return "D", "Desaprobado"


# =========================
# INSERTAR
# =========================

def insertar():

    promedio = float(input("Ingrese promedio: "))
    lista_promedios.append(promedio)
    letra, estado = validar_promedio(promedio)
    print("Promedio insertado.")
    print("Clasificación:", letra, estado)


# =========================
# MOSTRAR
# =========================

def mostrar():

    print("\nLISTA DE PROMEDIOS")
    for i in range(len(lista_promedios)):
        print(i + 1, "->", lista_promedios[i])


# =========================
# BUSCAR
# =========================

def buscar():

    valor = float(input("Ingrese promedio a buscar: "))
    encontrado = False
    for i in range(len(lista_promedios)):
        if lista_promedios[i] == valor:
            print("Encontrado en posición:", i)
            encontrado = True
    if not encontrado:
        print("No encontrado.")


# =========================
# MODIFICAR
# =========================

def modificar():

    valor = float(input("Valor a modificar: "))
    nuevo = float(input("Nuevo valor: "))
    for i in range(len(lista_promedios)):
        if lista_promedios[i] == valor:
            lista_promedios[i] = nuevo
            print("Dato modificado.")
            return
    print("Dato no encontrado.")


# =========================
# ELIMINAR
# =========================

def eliminar():

    valor = float(input("Valor a eliminar: "))
    for i in range(len(lista_promedios)):
        if lista_promedios[i] == valor:
            lista_promedios.pop(i)
            print("Dato eliminado.")
            return
    print("Dato no encontrado.")


# =========================
# BURBUJA
# =========================

def ordenar_burbuja():

    n = len(lista_promedios)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_promedios[j] > lista_promedios[j + 1]:
                temp = lista_promedios[j]
                lista_promedios[j] = lista_promedios[j + 1]
                lista_promedios[j + 1] = temp
    print("Ordenado con burbuja.")


# =========================
# SELECCIÓN
# =========================

def ordenar_seleccion():

    n = len(lista_promedios)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista_promedios[j] < lista_promedios[minimo]:
                minimo = j
        temp = lista_promedios[i]
        lista_promedios[i] = lista_promedios[minimo]
        lista_promedios[minimo] = temp
    print("Ordenado con selección.")


# =========================
# TABLA BIDIMENSIONAL
# =========================

def agregar_tabla():

    nombre = input("Nombre: ")
    promedio = float(input("Promedio: "))
    letra, estado = validar_promedio(promedio)
    fila = [nombre, promedio, estado]
    tabla_estudiantes.append(fila)
    print("Fila agregada.")


# =========================
# MOSTRAR TABLA
# =========================

def mostrar_tabla():

    print("\n===== TABLA =====")
    print("{:<20} {:<10} {:<15}".format(
        "Nombre",
        "Promedio",
        "Estado"
    ))
    print("-" * 45)
    for fila in tabla_estudiantes:
        print("{:<20} {:<10} {:<15}".format(
            fila[0],
            fila[1],
            fila[2]
        ))


# =========================
# MENÚ
# =========================

def menu():

    while True:
        print("\n===== MENÚ VALIDACIÓN =====")
        print("1. Insertar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Ordenar Burbuja")
        print("7. Ordenar Selección")
        print("8. Agregar Tabla")
        print("9. Mostrar Tabla")
        print("0. Salir")
        opcion = input("Seleccione: ")
        if opcion == "1":
            insertar()
        elif opcion == "2":
            mostrar()
        elif opcion == "3":
            buscar()
        elif opcion == "4":
            modificar()
        elif opcion == "5":
            eliminar()
        elif opcion == "6":
            ordenar_burbuja()
        elif opcion == "7":
            ordenar_seleccion()
        elif opcion == "8":
            agregar_tabla()
        elif opcion == "9":
            mostrar_tabla()
        elif opcion == "0":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida.")
