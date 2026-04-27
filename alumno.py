#==============================================
#Modulo: alumno.py
#Descripcion: Manejo de datos del alumno
#==============================================


def crear_estudiante(codigo, nombre, apellido, carrera):
    estudiante = { 
        "Codigo":codigo, 
        "Nombre":nombre, 
        "Apellido":apellido, 
        "Carrera":carrera,
        }
    return estudiante  

def ingresar_estudiante():
    print("======INGRESO DE DATOS DEL ESTUDIANTE:======")

    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")

    estudiante = crear_estudiante(codigo, nombre, apellido, carrera) 
    return estudiante

def mostrar_estudiantes(lista_estudiantes):

    print("\n======LISTA DE ESTUDIANTES:======")

    for est in lista_estudiantes:
        print("=================================")
        print(f"Codigo   :  {est['Codigo']}")
        print(f"Nombre   :  {est['Nombre']}")
        print(f"Apellido :  {est['Apellido']}")
        print(f"Carrera  :  {est['Carrera']}")
        