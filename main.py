from alumno import ingresar_estudiante, mostrar_estudiantes
from notas import ingresar_notas
from validacion import validar_promedio
from Promedios import calcular_promedio, obtener_estado
from reporte import generar_reporte
lista_notas_global = []
lista_estudiantes_global = []

def opcion_1():
    global lista_estudiantes_global

    print("=== Ingreso de alumnos ===")
    estudiante = ingresar_estudiante()
    lista_estudiantes_global.append(estudiante)

    print("Alumno registrado correctamente.")
    mostrar_estudiantes(lista_estudiantes_global)
    input()
def opcion_2():
    global lista_notas_global
    print("=== Ingreso de notas ===")
    lista_notas_global = ingresar_notas()
    print("Notas registradas:", lista_notas_global)
    input()

def opcion_3():
    global lista_notas_global
    print("=== Validación ===")

    if not lista_notas_global:
        print("Primero debes ingresar notas.")
        return
    promedio = calcular_promedio(lista_notas_global)
    letra, estado = validar_promedio(promedio)
    print(f"Resultado: {letra} {estado}")
    input()

def opcion_4():
    global lista_notas_global
    print("Promedio")
    if not lista_notas_global:
        print("Primero debes ingresar notas.")
        return
    promedio = calcular_promedio(lista_notas_global)
    estado = obtener_estado(promedio)
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")
    input()

def opcion_5():
    print(" Reporte ")
    generar_reporte(lista_estudiantes_global, lista_notas_global)
    input()


def mostrar_menu():
    print("\n MENÚ PRINCIPAL")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            opcion_4()
        elif opcion == "5":
            opcion_5()
        elif opcion == "0":
            print("Saliendo del sistema")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

main()