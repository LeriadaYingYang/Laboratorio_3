lista = []

def insertar():
    valor = int(input("Ingrese un numero: "))
    lista.append(valor)

def eliminar():
    if len(lista) == 0:
        print("La lista está vacía.")
        return
    pos = int(input("Ingrese la posición: "))
    if 0 <= pos < len(lista):
        lista.pop(pos)
    else:
        print("Posición inválida.")

def buscar():
    valor = int(input("Ingrese el valor a buscar: "))
    if valor in lista:
        print("Encontrado.")
    else:
        print("No encontrado.")
    
def mostrar():
    print("Lista:", lista)

def menu():
    while True:
        print("\n··········LISTA DINAMICA··········")
        print("1. Insertar")
        print("2. Eliminar")
        print("3. Buscar")
        print("4. Mostrar")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar()
        elif opcion == "2":
            eliminar() 
        elif opcion == "3":
            buscar()
        elif opcion == "4":
            mostrar()
        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
