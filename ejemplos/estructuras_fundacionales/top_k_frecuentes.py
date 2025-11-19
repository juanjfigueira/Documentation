#!/usr/bin/env python3
"""top_k_frecuentes.py
Ejemplo ejecutable para obtener los k elementos más frecuentes.
"""

from collections import Counter

def top_k_frecuentes(arr, k):
    """
    Devuelve los k elementos más frecuentes en arr.
    Rompe empates por orden lexicográfico (ascendente).
    """
    cnt = Counter(arr)
    items = sorted(cnt.items(), key=lambda iv: (-iv[1], iv[0]))
    return [x for x, _ in items[:k]]

if __name__ == '__main__':
    arr = ["apple", "banana", "apple", "orange", "banana", "apple", "pear"]
    print("Entrada:", arr)
    print("Top 2:", top_k_frecuentes(arr, 2))
