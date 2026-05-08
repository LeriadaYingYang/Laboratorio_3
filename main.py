import lista
import validacion
import ordenamiento
import notas


lista_notas_global = []


def mostrar_menu():
    print("\n" + "=" * 45)
    print("      SISTEMA PRINCIPAL DE PROGRAMACIÓN")
    print("=" * 45)
    print("1. Gestión de lista dinámica")
    print("2. Validación de promedios")
    print("3. Ordenamiento de notas")
    print("4. Laboratorio completo de notas")
    print("0. Salir")
    print("=" * 45)


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            lista.menu()

        elif opcion == "2":
            validacion.menu()

        elif opcion == "3":
            ordenamiento.menu_ordenamiento(lista_notas_global)

        elif opcion == "4":
            notas.main()

        elif opcion == "0":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()