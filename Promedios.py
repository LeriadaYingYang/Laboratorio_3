def calcular_promedio(notas: list[float]) -> float:
    """
    Calcula el promedio de una lista de notas.
    """
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def obtener_estado(promedio: float) -> str:
    """
    Determina si el alumno aprobó o desaprobó.
    """
    if promedio >= 11:
        return "Aprobado"
    else:
        return "Desaprobado"
