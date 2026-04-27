# ============================================
# Módulo: Notas.py
# Autor: [Pablo Diaz]
# Descripción: Funciones para gestionar notas de estudiantes
# ============================================

# ============================================
# Notas.py - Solo ingresa y devuelve notas
# ============================================

def ingresar_notas():
    """
    Pedir la cantidad de notas y luego cada nota.
    Valida que la nota esté entre 0 y 20.
    Devuelve una lista con las notas.
    """
    cantidad = int(input("¿Cuántas notas va a tener el alumno? "))
    # Crear una lista del tamaño exacto, llena de ceros
    notas = [0.0] * cantidad
    
    i = 0
    while i < cantidad:
        nota = float(input(f"Nota {i+1}: "))
        if 0 <= nota <= 20:
            notas[i] = nota   # asignar directamente en la posición i
            i += 1
        else:
            print("La nota debe estar entre 0 y 20.")
    return notas

