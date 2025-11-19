#!/usr/bin/env python3
"""pares_que_suman.py
Encontrar pares únicos que suman un objetivo.
"""

def pares_que_suman(arr, objetivo):
    """
    Devuelve una lista ordenada de tuplas (a, b) con a <= b
    y a + b == objetivo. Cada par es único.
    """
    vistos = set()
    pares = set()
    for x in arr:
        comp = objetivo - x
        if comp in vistos:
            a, b = (min(x, comp), max(x, comp))
            pares.add((a, b))
        vistos.add(x)
    return sorted(pares)

if __name__ == '__main__':
    arr = [1, 2, 3, 2, 4, -1, 5]
    objetivo = 4
    print("Entrada:", arr)
    print("Objetivo:", objetivo)
    print("Pares que suman objetivo:", pares_que_suman(arr, objetivo))
