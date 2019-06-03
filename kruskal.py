import numpy as np
from union_find import *
from grafo import Grafo


def mst_kruskal(grafo, return_grafo_o_union_find):
    if grafo is not None:
        if not grafo.diretto:
            union_find = UnionFind()
            nodi = get_nodi(grafo)
            for v in nodi:
                make_set(v, union_find)

            archi = get_archi(grafo, nodi)
            archi.sort(key=lambda a: a.peso)
            archi_mst = []
            for e in archi:
                x = find_set(e.sorgente)
                y = find_set(e.destinazione)
                if x is not y:
                    union(x, y, union_find)
                    archi_mst.append(e)
            if return_grafo_o_union_find == "union_find":
                return union_find
            elif return_grafo_o_union_find == "grafo":
                mst_matrix = archi_to_matrix(archi_mst, False, len(nodi))
                mst = Grafo(mst_matrix, len(nodi), False)
                return mst
            else:
                print("Tipo di ritorno non riconosciuto. Serve \"grafo\" o \"union_find\"")
                return None
        else:
            print("Kruskal può essere eseguito solo su grafi indiretti")
            return None
    else:
        print("Grafo non valido")
        return None


def get_nodi(g):
    nodi = []
    for l in range(0, g.dim):
        nodi.append(Nodo(l))
    return nodi


def get_archi(g, nodi):
    archi = []
    for i in range(g.dim):
        for j in range(i, g.dim):
            if g.matrice[i, j] != 0:
                archi.append(Arco(False, nodi[i], nodi[j], g.matrice[i, j]))
    return archi


def archi_to_matrix(array_di_archi, grafo_diretto, dim):
    matrix = np.zeros((dim, dim))
    for e in array_di_archi:
        matrix[e.sorgente.numero, e.destinazione.numero] = e.peso
        if not grafo_diretto:
            matrix[e.destinazione.numero, e.sorgente.numero] = e.peso
    return matrix
