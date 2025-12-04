## README del Repositorio – Proyecto Semanal (8 Semanas)
##José Emiliano Espericueta González

Este repositorio contiene **8 mini-proyectos**, organizados por semanas, desarrollados en **Python**, **C# (C-Sharp)** o **ambos**, según las instrucciones del curso.
Cada semana es independiente y contiene su propio proyecto, su código y sus pruebas automáticas.

La estructura general es:

```
/semana_1
/semana_2
/semana_3
...
/semana_8
```

Cada carpeta incluye:

* Código fuente.
* Archivo `run.py` o proyecto C# según corresponda.
* Carpeta `tests/` para pruebas automáticas.
* Dependencias (`requirements.txt`) solo en semanas que usan Python.

---

# 1. Ejecución de proyectos en **C# (C-Sharp)**

Algunas semanas contienen proyectos hechos en C#.
Para ejecutarlos:

### **Requisitos**

* Visual Studio (el editor morado tradicional).
* .NET SDK instalado (la versión utilizada en el curso).

### **Pasos**

1. Abrir **Visual Studio**.
2. Seleccionar **Open a project or solution**.
3. Navegar a la carpeta de la semana, por ejemplo:

```
/semana_4_csharp/
```

4. Abrir el archivo `.csproj` o `.sln` incluido.
5. Compilar y ejecutar desde **F5** o con **Run**.

No requiere entorno virtual ni dependencias adicionales.

---

# 2. Ejecución de proyectos en **Python**

Varias semanas incluyen un proyecto escrito completamente en Python.

### **Requisitos**

* Python 3.11+
* pip
* pytest

---

## 2.1. Crear entorno virtual

Dentro de la carpeta de la semana (ejemplo: `semana_6_algoritmos`), ejecutar:

```bash
python -m venv venv
```

Activar el entorno virtual:

### Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

### Git Bash

```bash
source venv/Scripts/activate
```

---

## 2.2. Instalar dependencias

Cada semana que use Python incluye un archivo `requirements.txt`.

Instalarlo:

```bash
pip install -r requirements.txt
```

---

## 2.3. Ejecutar el proyecto

Todas las semanas en Python incluyen un archivo ejecutable llamado:

```
run.py
```

Ejecutarlo así:

```bash
python run.py
```

Esto ejecuta todas las demostraciones, algoritmos o módulos correspondientes a esa semana.

---

# 3. Ejecución de pruebas (Tests)

Cada semana con Python tiene una carpeta:

```
/tests/
```

Para ejecutar las pruebas:

1. Activar el entorno virtual.
2. Ejecutar pytest:

```bash
pytest -v
```

Esto valida la correcta implementación de las estructuras, algoritmos y funciones entregadas.

---

# 4. Resumen por semana

Cada semana contiene un mini-proyecto independiente.
La modalidad varía:

| Semana   | Lenguaje    | Descripción general                                  |
| -------- | ----------- | ---------------------------------------------------- |
| Semana 1 | C# o Python | Algoritmos iniciales según instrucciones del curso   |
| Semana 2 | C# / Python | Implementaciones según el archivo HTML de la semana  |
| Semana 3 | Python      | Algoritmos clásicos según guía                       |
| Semana 4 | C#          | Proyecto estructurado en Visual Studio               |
| Semana 5 | Python + C# | Implementación dual (como lo pidió el profesor)      |
| Semana 6 | Python      | Grafos ponderados y recorridos (Dijkstra / Floyd)    |
| Semana 7 | Python      | Algoritmos adicionales según el contenido            |
| Semana 8 | Python      | Árboles BST, AVL, Huffman, RPN (con tests completos) |

*(El detalle exacto puede variar según cada HTML entregado por el profesor.)*

---

# 5. Flujo de trabajo recomendado

## Para semanas en **Python**

```
cd semana_X
python -m venv venv
.\venv\Scripts\Activate.ps1    (o "source venv/Scripts/activate")
pip install -r requirements.txt
python run.py
pytest -v
```

## Para semanas en **C#**

```
Abrir Visual Studio → Open Project/Solution → seleccionar .sln o .csproj
Run / Debug
```

---

# 6. Notas adicionales

* Cada semana funciona de manera independiente.
* Los tests fueron creados para validar la implementación solicitada en los archivos HTML del curso.
* Es recomendable ejecutar cada semana por separado para evitar conflictos entre versiones o dependencias.

---