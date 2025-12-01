import os

# --- 1. FUNCIÓN PARA LEER EL ARCHIVO ---
def leer_grafo():

    grafo = {}
    
    if os.path.exists('edges.txt'):
        f = open('edges.txt', 'r')
        lines = f.readlines()
        f.close()

        for linea in lines:
       
            datos = linea.strip().split(',')
            
            if len(datos) == 3:
                origen = datos[0]
                destino = datos[1]
                peso = datos[2]

                if origen not in grafo:
                    grafo[origen] = []

                grafo[origen].append({'vecino': destino, 'peso': peso})

                if destino not in grafo:
                    grafo[destino] = []
        return grafo
    else:
        print("No encontré el archivo edges.txt. Corre primero el programa de C#.")
        return {}

# --- 2. EJERCICIO 3: SECUENCIA DE GRADOS ---
def obtener_secuencia_grados(grafo):
    lista_grados = []
    
    for nodo in grafo:
        cantidad_vecinos = len(grafo[nodo])
        lista_grados.append(cantidad_vecinos)
    
    lista_grados.sort(reverse=True)
    return lista_grados

# --- 3. EJERCICIO 4: VALIDACIONES ---
def validar_grafo(grafo):
    print("\n--- Validando el Grafo ---")
    
    # Calcular suma de grados
    suma_total = 0
    maximo_grado = 0
    nodos = list(grafo.keys())
    n = len(nodos)

    for nodo in grafo:
        grado = len(grafo[nodo])
        suma_total = suma_total + grado
        if grado > maximo_grado:
            maximo_grado = grado

  
    if suma_total % 2 == 0:
        print("1. Suma de grados (" + str(suma_total) + "): ES PAR (Correcto)")
    else:
        print("1. Suma de grados (" + str(suma_total) + "): ES IMPAR (Error)")

 
    if maximo_grado <= (n - 1):
        print("2. Grado máximo (" + str(maximo_grado) + "): Correcto")
    else:
        print("2. Grado máximo es muy alto (Error)")

 
    if n > 0:
        visitados = []
        cola = []
        
        primer_nodo = nodos[0]
        cola.append(primer_nodo)
        visitados.append(primer_nodo)
        
        while len(cola) > 0:
            actual = cola.pop(0)
            vecinos = grafo[actual]
            
            for v in vecinos:
                nombre_vecino = v['vecino']
                if nombre_vecino not in visitados:
                    visitados.append(nombre_vecino)
                    cola.append(nombre_vecino)
        
        if len(visitados) == n:
            print("3. Conectividad: El grafo es CONEXO (Todos unidos)")
        else:
            print("3. Conectividad: NO es conexo (Hay islas)")

# --- 4. EJERCICIO 5: MATRIZ DE ADYACENCIA ---
def imprimir_matriz(grafo):
    print("\n--- Matriz de Adyacencia ---")
    
    nodos = list(grafo.keys())
    nodos.sort()
    n = len(nodos)

    print("      ", end="") 
    for nodo in nodos:
        
        print(nodo[0:3] + " ", end="") 
    print()

    contador_unos = 0

    for i in range(n):
        nodo_fila = nodos[i]
        print(nodo_fila[0:3] + " | ", end="") 
        
        for j in range(n):
            nodo_columna = nodos[j]
            
            hay_conexion = 0
            vecinos = grafo[nodo_fila]
            
            for v in vecinos:
                if v['vecino'] == nodo_columna:
                    hay_conexion = 1
                    contador_unos = contador_unos + 1
            
            print(str(hay_conexion) + "   ", end="")
        print() 

    aristas_en_lista = 0
    for nodo in grafo:
        aristas_en_lista += len(grafo[nodo])
    
    print("\nVerificación:")
    print("Total en lista: " + str(aristas_en_lista))
    print("Total en matriz (unos): " + str(contador_unos))
    
    if aristas_en_lista == contador_unos:
        print("Resultado: CONSISTENTE")
    else:
        print("Resultado: ERROR")

# --- BLOQUE PRINCIPAL ---
mi_grafo = leer_grafo()

if len(mi_grafo) > 0:
    # Ejercicio 3
    secuencia = obtener_secuencia_grados(mi_grafo)
    print("Secuencia de grados: " + str(secuencia))
    
    # Ejercicio 4
    validar_grafo(mi_grafo)
    
    # Ejercicio 5
    imprimir_matriz(mi_grafo)