#!/usr/bin/env python3
"""contar_palabras.py
Contar palabras en un texto y ordenar por frecuencia (desc) y palabra (asc).
"""

import re
from collections import Counter

def contar_palabras_ordenadas(texto):
    """
    Extrae palabras, cuenta y devuelve una lista de tuples (palabra, freq)
    ordenada por freq desc y palabra asc.
    """
    palabras = re.findall(r"\w+", texto.lower())
    cnt = Counter(palabras)
    return sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))

if __name__ == '__main__':
    texto = "Hola hola mundo. Mundo grande, mundo pequeño."
    print("Texto:", texto)
    print("Conteo ordenado:", contar_palabras_ordenadas(texto))
