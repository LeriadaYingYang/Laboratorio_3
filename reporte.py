
from Promedios import calcular_promedio, obtener_estado
from validacion import validar_promedio


def generar_reporte(lista_estudiantes, lista_notas):
    print("\n REPORTE GENERAL ")

    print("\n DATOS DEL ALUMNO ")
    if len(lista_estudiantes) == 0:
        print("No hay alumnos registrados.")
    else:
        for estudiante in lista_estudiantes:
            print("------------------------------------")
            print(f"Código   : {estudiante['Codigo']}")
            print(f"Nombre   : {estudiante['Nombre']}")
            print(f"Apellido : {estudiante['Apellido']}")
            print(f"Carrera  : {estudiante['Carrera']}")

    print("\n NOTAS REGISTRADAS ")
    if len(lista_notas) == 0:
        print("No hay notas registradas.")
        print("------------------------------------")
        return

    for i, nota in enumerate(lista_notas, start=1):
        print(f"Nota {i}: {nota}")

    promedio = calcular_promedio(lista_notas)
    estado = obtener_estado(promedio)
    letra, descripcion = validar_promedio(promedio)

    print("\nRESULTADO FINAL ")
    print(f"Promedio : {promedio:.2f}")
    print(f"Estado   : {estado}")
    print(f"Nivel    : {letra} {descripcion}")

    print("------------------------------------")