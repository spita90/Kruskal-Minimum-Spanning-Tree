from nodo import Nodo
from arco import Arco


class UnionFind:
    def __init__(self):
        self.s = []

    def append(self, insieme):
        self.s.append(insieme)

    def remove(self, insieme):
        self.s.remove(insieme)


class Insieme:
    def __init__(self, nodo):
        nodo.insieme = self
        self.head = nodo
        self.tail = nodo
        self.size = 1

    def append(self, insieme):
        it = insieme.size
        ptr = insieme.head
        while it > 0:
            ptr.insieme = self
            ptr = ptr.prossimo
            it -= 1
        self.tail.prossimo = insieme.head
        self.tail = insieme.tail
        self.size += insieme.size


def connected_components(g):
    if g is not None:
        union_find = UnionFind()
        nodi = get_nodi(g)
        for v in nodi:
            make_set(v, union_find)
        archi = get_archi(g, nodi)
        for e in archi:
            x = find_set(e.sorgente)
            y = find_set(e.destinazione)
            if x is not y:
                union(x, y, union_find)
        return union_find
    else:
        return None


def get_nodi(g):
    nodi = []
    for l in range(0, g.dim):
        nodi.append(Nodo(l))
    return nodi


def get_archi(g, nodi):
    archi = []
    if g.diretto:
        for i in range(g.dim):
            for j in range(g.dim):
                if g.matrice[i, j] != 0:
                    archi.append(Arco(True, nodi[i], nodi[j], g.matrice[i, j]))
    else:
        for i in range(g.dim):
            for j in range(i, g.dim):
                if g.matrice[i, j] != 0:
                    archi.append(Arco(False, nodi[i], nodi[j], g.matrice[i, j]))
    return archi


def make_set(nodo, union_find):
    union_find.append(Insieme(nodo))


def find_set(nodo):
    return nodo.insieme


def union(sx, sy, union_find):
    if sx.size < sy.size:
        sy.append(sx)
        union_find.remove(sx)
    else:
        sx.append(sy)
        union_find.remove(sy)
