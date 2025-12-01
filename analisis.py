import os

def cargar_grafo(nombre_archivo):
    grafo = {}
    
    try:
        with open(nombre_archivo, 'r') as f:
            for linea in f:
             
                partes = linea.strip().split(',')
                if len(partes) == 3:
                    origen, destino, peso = partes
                    
                 
                    if origen not in grafo:
                        grafo[origen] = []
                    
                
                    grafo[origen].append({'vecino': destino, 'peso': peso})
                    
               
                    if destino not in grafo:
                        grafo[destino] = []
                        
        return grafo

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        print("Asegúrate de haber ejecutado primero el código de C# (dotnet run).")
        return {}

def imprimir_info_vertices(grafo):
    print("\nResultados del Análisis:")
    print("-" * 50)
    print(f"{'Vértice':<15} | {'Grado Salida':<12} | {'Vecinos'}")
    print("-" * 50)
    
    for vertice, vecinos in grafo.items():
        grado_salida = len(vecinos)
     
        lista_vecinos = [v['vecino'] for v in vecinos]
        print(f"{vertice:<15} | {grado_salida:<12} | {lista_vecinos}")
    print("-" * 50)

# --- Ejecución ---
archivo = 'edges.txt'
mi_grafo = cargar_grafo(archivo)

if mi_grafo:
    imprimir_info_vertices(mi_grafo)