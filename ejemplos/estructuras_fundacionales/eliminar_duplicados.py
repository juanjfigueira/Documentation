#!/usr/bin/env python3
"""eliminar_duplicados.py
Eliminar duplicados manteniendo el orden de primera aparición.
"""

def eliminar_duplicados_manteniendo_orden(seq):
    """
    Retorna una nueva lista con duplicados removidos, manteniendo
    el orden de la primera aparición.
    """
    visto = set()
    resultado = []
    for x in seq:
        if x not in visto:
            visto.add(x)
            resultado.append(x)
    return resultado

if __name__ == '__main__':
    entrada = [3, 1, 2, 3, 2, 4]
    salida = eliminar_duplicados_manteniendo_orden(entrada)
    print("Entrada:", entrada)
    print("Salida (sin duplicados):", salida)
