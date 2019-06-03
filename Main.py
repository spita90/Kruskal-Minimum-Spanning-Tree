import networkx as nx
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from gen_graf_random import graf_random_diretto, graf_random_indiretto
from union_find import connected_components
from kruskal import mst_kruskal


def main():
    grafo_diretto = graf_random_diretto(5, 5, 50)      # parametri: dimensione, peso massimo archi, percentuale massima di variazione sul peso degli archi
    grafo_indiretto = graf_random_indiretto(10, 50, 30)
    union_find = connected_components(grafo_indiretto)
    mst = mst_kruskal(grafo_indiretto, "grafo")                  # restituisce il mst di grafo_indiretto

    gr1 = nx.from_numpy_matrix(grafo_indiretto.matrice)
    gr2 = nx.from_numpy_matrix(mst.matrice)
    nx.draw(gr1, with_labels=True)
    plt.show()
    nx.draw(gr2, with_labels=True)
    plt.show()
    print("")

    # INIZIO TEST
    print("INIZIO TEST\n")

    # Test con n crescente e percentuale peso archi fissa all'80%
    print("Test con n crescente e percentuale peso archi fissa all'80%")
    n = 1
    while n <= 1000:
        start = timer()
        g_diretto = graf_random_diretto(n, 10, 80)
        stop = timer()
        print("\nCreata matrice di adiacenza di grafo DIRETTO con "+str(n)+" nodi e percentuale archi del 80% in "+str(stop-start)+" secondi")

        start = timer()
        union_find = connected_components(g_diretto)
        stop = timer()
        print("Creata union-find di tale grafo in "+str(stop-start)+" secondi")

        start = timer()
        g_indiretto = graf_random_indiretto(n, 10, 80)
        stop = timer()
        print("\nCreata matrice di adiacenza di grafo INDIRETTO con "+str(n)+" nodi e percentuale archi del 80% in "+str(stop-start)+" secondi")

        start = timer()
        union_find = connected_components(g_indiretto)
        stop = timer()
        print("Creata union-find di tale grafo in "+str(stop-start)+" secondi")

        start = timer()
        mst = mst_kruskal(g_indiretto, "union_find")
        stop = timer()
        print("Creata union-find del MST (Kruskal) di tale grafo in "+str(stop-start)+" secondi")

        n *= 10

    # Test con percentuale peso archi crescente e n fisso a 1000
    print("\nTest con percentuale peso archi crescente e n fisso a 1000")
    perc = 0
    while perc <= 100:
        start = timer()
        g_diretto = graf_random_diretto(1000, 10, perc)
        stop = timer()
        print("\nCreata matrice di adiacenza di grafo DIRETTO con 1000 nodi e percentuale archi del "+str(perc)+"% in "+str(stop-start)+" secondi")

        start = timer()
        union_find = connected_components(g_diretto)
        stop = timer()
        print("Creata union-find di tale grafo in "+str(stop-start)+" secondi")

        start = timer()
        g_indiretto = graf_random_indiretto(1000, 10, perc)
        stop = timer()
        print("\nCreata matrice di adiacenza di grafo INDIRETTO con 1000 nodi e percentuale archi del "+str(perc)+"% in "+str(stop-start)+" secondi")

        start = timer()
        union_find = connected_components(g_indiretto)
        stop = timer()
        print("Creata union-find di tale grafo in "+str(stop-start)+" secondi")

        start = timer()
        mst = mst_kruskal(g_indiretto, "union_find")
        stop = timer()
        print("Creata union-find del MST (Kruskal) di tale grafo in "+str(stop-start)+" secondi")

        perc += 20


if __name__ == "__main__":
    main()
