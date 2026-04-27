# =======================================
# Módulo: validacion.py
# Autor: [Fabrizio]
# Descripción: Función para validar promedios de estudiantes
# =======================================

# =======================================
# Validación.py - Devuelve una letra y un estado
# =======================================

def validar_promedio(promedio):

#Verificar si el promedio existe
    if promedio is None:
        return None, "Sin datos"
    
    #Rango más alto (18 a 20)
    if 18 <= promedio <= 20:
        return "AD", ": Sobresaliente"
    
    #Rango aprobado (15 a 17)
    elif 15 <= promedio <= 17:
        return "A", ": Aprobado"
    
    #Rango regular (11 a 14)
    elif 11 <= promedio <= 14:
        return "B",": Regular"
    
    #Rango Desaprobado (0 a 10)
    elif 0 <= promedio <= 10:
        return "C",": Desaprobado"
    else:
        return None, "Promedio inválido"
