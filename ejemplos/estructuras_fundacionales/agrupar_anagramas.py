#!/usr/bin/env python3
"""agrupar_anagramas.py
Agrupar palabras que son anagramas entre sí.
"""

from collections import defaultdict

def agrupar_anagramas(palabras):
    """
    Agrupa palabras anagramas. Retorna una lista de listas.
    """
    grupos = defaultdict(list)
    for w in palabras:
        clave = tuple(sorted(w))
        grupos[clave].append(w)
    return list(grupos.values())

if __name__ == '__main__':
    palabras = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grupos = agrupar_anagramas(palabras)
    print("Entrada:", palabras)
    print("Grupos de anagramas:")
    for g in grupos:
        print(" ", g)
