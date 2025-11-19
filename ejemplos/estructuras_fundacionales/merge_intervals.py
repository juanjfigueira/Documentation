#!/usr/bin/env python3
"""merge_intervals.py
Fusionar intervalos solapados.
"""

def merge_intervals(intervalos):
    """
    Dado una lista de intervalos (start, end), devuelve la lista
    de intervalos fusionados y no solapados, ordenada por start.
    """
    if not intervalos:
        return []
    intervalos = sorted(intervalos, key=lambda iv: iv[0])
    resultado = []
    cur_start, cur_end = intervalos[0]
    for s, e in intervalos[1:]:
        if s <= cur_end:
            cur_end = max(cur_end, e)
        else:
            resultado.append((cur_start, cur_end))
            cur_start, cur_end = s, e
    resultado.append((cur_start, cur_end))
    return resultado

if __name__ == '__main__':
    intervalos = [(1, 3), (2, 6), (8, 10), (15, 18)]
    print("Entrada:", intervalos)
    print("Intervalos fusionados:", merge_intervals(intervalos))
