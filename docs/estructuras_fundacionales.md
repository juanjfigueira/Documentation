# Estructuras de datos fundacionales en Python — Guía y ejemplos prácticos

Resumen
- Esta guía recoge las estructuras de datos fundacionales en Python (list, tuple, set, dict).
- Para cada estructura muestro: forma profesional de adicionar, extraer y —cuando aplica— ordenar datos.
- Incluye ejemplos resueltos de problemas reales y la complejidad temporal de cada enfoque.
- Código en Python 3, idiomático y comentado.

Índice
1. Listas (list)
2. Tuplas (tuple)
3. Conjuntos (set)
4. Diccionarios (dict)
5. Problemas reales (con soluciones)
   - Top-k más frecuentes
   - Eliminar duplicados manteniendo orden
   - Pares que suman un objetivo
   - Agrupar anagramas
   - Contar palabras y ordenar por frecuencia
   - Merge intervals
6. Recomendaciones finales

---

## 1. Listas (list)
- Propiedades: ordenadas, mutables, permiten duplicados.
- Usos típicos: secuencias con acceso por índice, acumulación de resultados.

Adición (forma profesional)
```python
mi_lista = []
mi_lista.append(10)        # agregar al final
mi_lista.extend([20, 30])  # agregar múltiples elementos
mi_lista.insert(1, 15)     # insertar en posición específica (costoso)
```

Extracción
```python
last = mi_lista.pop()      # obtiene y elimina el último elemento
first = mi_lista.pop(0)    # obtiene y elimina el primero (O(n))
mi_lista.remove(15)        # elimina por valor (lanza ValueError si no existe)
```

Ordenación
```python
mi_lista.sort()                       # ordena in-place (mutación)
mi_lista.sort(reverse=True)           # orden descendente
mi_lista_ordenada = sorted(mi_lista)  # retorna una nueva lista ordenada
```

Complejidad
- append: O(1) amortizado
- pop(): O(1); pop(0) e insert(0, x): O(n)
- sort: O(n log n)

---

## 2. Tuplas (tuple)
- Propiedades: ordenadas, inmutables, hashables si sus elementos lo son.
- Usos típicos: registros inmutables, claves en dict (si contienen solo elementos hashables), desempaquetado.

Adición (no mutan)
```python
t = (1, 2)
t = t + (3,)  # crea una nueva tupla
```

Acceso / extracción
```python
x = t[0]
a, b = t  # desempaquetado
```

Ordenar
- Para ordenar, convertir a lista, ordenar y volver a tupla:
```python
t_ordenada = tuple(sorted(t))
```

Complejidad
- Acceso por índice: O(1)

---

## 3. Conjuntos (set)
- Propiedades: no ordenados, sin duplicados, operaciones de conjunto eficientes.
- Usos: membership testing, eliminar duplicados, operaciones matemáticas (union, intersección, diferencia).

Adición
```python
s = set()
s.add(10)
s.update([20, 30])
```

Extracción
```python
elem = s.pop()         # elimina un elemento arbitrario
s.remove(20)           # KeyError si no existe
s.discard(40)          # no lanza error si no existe
```

Ordenar (si hace falta)
```python
lista_ordenada = sorted(s)  # devuelve lista ordenada
```

Complejidad
- add, remove, membership: O(1) promedio

---

## 4. Diccionarios (dict)
- Propiedades: mapeo clave → valor, desde Python 3.7 mantienen orden de inserción.
- Usos: contar frecuencias, índices por clave, caches.

Adición
```python
d = {}
d['a'] = 1
d.update({'b': 2, 'c': 3})
```

Extracción
```python
v = d.pop('a')           # elimina y devuelve el valor
k, v = d.popitem()       # elimina y devuelve el último par (clave, valor)
v = d.get('b', 0)        # obtiene con valor por defecto
```

Ordenar
- Por clave:
```python
for k in sorted(d):
    ...
```
- Por valor:
```python
for k, v in sorted(d.items(), key=lambda kv: kv[1]):
    ...
```

Complejidad
- access/insert/delete: O(1) promedio
- sorted: O(m log m) donde m = número de claves

---

## 5. Problemas reales (soluciones)

1) Top-k elementos más frecuentes (dict + sorted / Counter)
Enunciado: dado un arreglo `arr`, devolver los `k` elementos más frecuentes (frecuencia descendente, y por orden lexicográfico en caso de empate).

Solución (idiomática):
```python
from collections import Counter

def top_k_frecuentes(arr, k):
    cnt = Counter(arr)
    # most_common devuelve (elemento, freq) ordenado por freq desc
    # si necesitas romper empates lexicográficamente:
    items = sorted(cnt.items(), key=lambda iv: (-iv[1], iv[0]))
    return [x for x, _ in items[:k]]

# Ejemplo
arr = ["apple","banana","apple","orange","banana","apple","pear"]
print(top_k_frecuentes(arr, 2))  # -> ['apple', 'banana']
```
Complejidad: O(n + m log m) (m = claves únicas).

2) Eliminar duplicados manteniendo orden (list + set)
Enunciado: dada una lista, eliminar duplicados manteniendo el primer orden de aparición.

Solución:
```python
def eliminar_duplicados_manteniendo_orden(seq):
    visto = set()
    resultado = []
    for x in seq:
        if x not in visto:
            visto.add(x)
            resultado.append(x)
    return resultado

print(eliminar_duplicados_manteniendo_orden([3,1,2,3,2,4]))  # -> [3,1,2,4]
```
Complejidad: O(n)

3) Pares únicos que suman un objetivo (set + tuplas)
Enunciado: devolver todos los pares únicos (a,b) con a <= b que suman `objetivo`.

Solución:
```python
def pares_que_suman(arr, objetivo):
    vistos = set()
    pares = set()
    for x in arr:
        comp = objetivo - x
        if comp in vistos:
            a, b = (min(x, comp), max(x, comp))
            pares.add((a, b))
        vistos.add(x)
    return sorted(pares)

print(pares_que_suman([1,2,3,2,4,-1,5], 4))  # -> [(-1,5),(1,3),(2,2)]
```
Complejidad: O(n log p) por la ordenación final.

4) Agrupar anagramas (dict + tuple)
Enunciado: agrupa palabras que son anagramas.

Solución:
```python
from collections import defaultdict

def agrupar_anagramas(palabras):
    grupos = defaultdict(list)
    for w in palabras:
        clave = tuple(sorted(w))
        grupos[clave].append(w)
    return list(grupos.values())

print(agrupar_anagramas(["eat","tea","tan","ate","nat","bat"]))
# -> [['eat','tea','ate'], ['tan','nat'], ['bat']]
```
Complejidad: O(n * L log L) (L = longitud media palabra).

5) Contar palabras y ordenar por frecuencia y lexicográficamente (dict + sorted)
Enunciado: dado un texto, devolver pares (palabra, freq) ordenados por freq desc y palabra asc.

Solución:
```python
import re
from collections import Counter

def contar_palabras_ordenadas(texto):
    palabras = re.findall(r"\w+", texto.lower())
    cnt = Counter(palabras)
    return sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))

texto = "Hola hola mundo. Mundo grande, mundo pequeño."
print(contar_palabras_ordenadas(texto))
# -> [('mundo', 3), ('hola', 2), ('grande',1), ('pequeño',1)]
```
Complejidad: O(n log m)

6) Merge Intervals (listas ordenadas de tuplas)
Enunciado: fusionar intervalos solapados en una lista de pares (start, end).

Solución:
```python
def merge_intervals(intervalos):
    if not intervalos:
        return []
    intervalos = sorted(intervalos, key=lambda iv: iv[0])
    resultado = []
    cur_start, cur_end = intervalos[0]
    for s, e in intervalos[1:]:
        if s &lt;= cur_end:
            cur_end = max(cur_end, e)
        else:
            resultado.append((cur_start, cur_end))
            cur_start, cur_end = s, e
    resultado.append((cur_start, cur_end))
    return resultado

print(merge_intervals([(1,3),(2,6),(8,10),(15,18)]))
# -> [(1,6),(8,10),(15,18)]
```
Complejidad: O(n log n) por ordenación.

---

## 6. Recomendaciones finales
- Usa listas para secuencias que necesiten orden y acceso por índice.
- Usa tuplas para registros inmutables o claves hashables.
- Usa sets para eliminar duplicados y operaciones de pertenencia con O(1).
- Usa dicts para mapeos, conteos y lookups por clave.
- Para problemas grandes, piensa en la complejidad: evita pop(0) en listas; prefiere deque si necesitas pops desde ambos extremos frecuentemente.
- Mantén código legible, usa collections (Counter, defaultdict, deque) cuando aporten claridad y rendimiento.

---

Si necesitas que adapte el idioma, añada tests unitarios o ejemplos adicionales, o coloque el archivo en otra ruta, indícalo y lo ajusto antes de crear el PR.
