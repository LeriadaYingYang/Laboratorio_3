# ==========================================================
# Módulo: ordenamiento.py
# Autor: Fabrizio (Etapa 4)
# Descripción: Algoritmos de ordenamiento (Burbuja y Selección)
#              con conteo de métricas y menú de la Etapa 4 (T3).
# ==========================================================

def ordenar_burbuja(lista_original):
    """
    Ordena una lista de números de forma ascendente usando Burbuja.
    Retorna la lista ordenada, el número de comparaciones e intercambios.
    """
    # Trabajamos sobre una copia para no alterar la lista original
    lista = lista_original.copy()
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                # Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
                
    return lista, comparaciones, intercambios


def ordenar_seleccion(lista_original):
    """
    Ordena una lista de números de forma ascendente usando Selección.
    Retorna la lista ordenada, el número de comparaciones e intercambios.
    """
    # Trabajamos sobre una copia
    lista = lista_original.copy()
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
                
        # Intercambio de posiciones si se encontró un elemento menor
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            intercambios += 1
            
    return lista, comparaciones, intercambios


def comparar_resultados(lista_notas):
    """
    Ejecuta ambos métodos y muestra un cuadro comparativo de su eficiencia.
    """
    print("\n" + "="*45)
    print("      --- COMPARACIÓN DE RENDIMIENTO ---      ")
    print("="*45)
    print(f"Lista original de notas: {lista_notas}\n")
    
    # Ejecución de algoritmos
    _, comp_b, inter_b = ordenar_burbuja(lista_notas)
    _, comp_s, inter_s = ordenar_seleccion(lista_notas)
    
    # Formateo de la tabla de comparación
    print(f"{'MÉTODO':<18} | {'COMPARACIONES':<13} | {'INTERCAMBIOS':<12}")
    print("-" * 45)
    print(f"{'Burbuja (Bubble)':<18} | {comp_b:<13} | {inter_b:<12}")
    print(f"{'Selección (Selection)':<18} | {comp_s:<13} | {inter_s:<12}")
    print("-" * 45)
    
    # Breve conclusión según la teoría
    if inter_b > inter_s:
        print("\nAnálisis: Selección realizó MENOS intercambios físicos en memoria,")
        print("lo cual suele hacerlo más eficiente en listas desordenadas.")
    elif inter_b == inter_s:
        print("\nAnálisis: Ambos métodos requirieron el mismo número de operaciones.")
    print("="*45)


def menu_ordenamiento(lista_notas):
    """
    Submenú interactivo para la Etapa 4 del sistema de calificaciones.
    Recibe la lista de notas que se quiere ordenar.
    """
    while True:
        print("\n" + "·"*10 + " ORDENAMIENTO (ETAPA 4) " + "·"*10)
        print("1. Ordenar con burbuja")
        print("2. Ordenar con selección")
        print("3. Comparar resultados")
        print("4. Volver")
        print("·"*44)
        
        opcion = input("Seleccione una opción: ")
        
        # Validación: Si no hay notas registradas, el sistema no debe caerse.
        # Le permitimos al profesor o usuario ingresar notas rápidas de prueba.
        if not lista_notas or len(lista_notas) == 0:
            print("\n[!] Alerta: No hay notas registradas actualmente en el sistema.")
            opc_temp = input("¿Deseas ingresar notas de prueba rápidas para evaluar? (S/N): ").strip().upper()
            if opc_temp == 'S':
                entrada = input("Ingresa notas separadas por espacios (ejemplo: 12 18 9 15 11): ")
                try:
                    lista_notas = [float(x) for x in entrada.split()]
                except ValueError:
                    print("Formato incorrecto. Usando notas predeterminadas: [14.0, 11.0, 20.0, 8.5]")
                    lista_notas = [14.0, 11.0, 20.0, 8.5]
            else:
                print("Operación cancelada. Regresando al menú...")
                break
        
        if opcion == "1":
            print("\n>>> ORDENAMIENTO POR BURBUJA <<<")
            print(f"Lista original: {lista_notas}")
            ordenada, comp, inter = ordenar_burbuja(lista_notas)
            print(f"Lista ordenada: {ordenada}")
            print(f"Comparaciones: {comp} | Intercambios: {inter}")
            input("\nPresione Enter para continuar...")
            
        elif opcion == "2":
            print("\n>>> ORDENAMIENTO POR SELECCIÓN <<<")
            print(f"Lista original: {lista_notas}")
            ordenada, comp, inter = ordenar_seleccion(lista_notas)
            print(f"Lista ordenada: {ordenada}")
            print(f"Comparaciones: {comp} | Intercambios: {inter}")
            input("\nPresione Enter para continuar...")
            
        elif opcion == "3":
            comparar_resultados(lista_notas)
            input("\nPresione Enter para continuar...")
            
        elif opcion == "4":
            print("Regresando al Menú Principal...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")