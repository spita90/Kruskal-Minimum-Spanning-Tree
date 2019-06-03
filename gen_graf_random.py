import numpy as np
import random
from grafo import Grafo


def graf_random_diretto(n, peso_max=5, perc_conn=50):
    if check_params(n, peso_max, perc_conn):
        counter_cambiamenti = int(round(n * perc_conn / 100))
        matrice_adiacenza = np.zeros((n, n))
        for i in range(n):
            for j in range(counter_cambiamenti):
                matrice_adiacenza[i, random.choice(range(n))] = random.choice(range(peso_max+1))
            matrice_adiacenza[i, i] = 0
        grafo = Grafo(matrice_adiacenza, n, True)
        return grafo
    else:
        return None


def graf_random_indiretto(n, peso_max=5, perc_conn=50):
    if check_params(n, peso_max, perc_conn):
        matrice_adiacenza = np.zeros((n, n))
        for i in range(n):
            valori = np.zeros(n-i)
            counter_cambiamenti = int(round((n-i) * perc_conn / 100))
            for j in range(counter_cambiamenti):
                valori[random.choice(range(n-i))] = random.choice(range(peso_max+1))
            matrice_adiacenza[i, range(i, n)] = valori
            matrice_adiacenza[range(i, n), i] = valori
            matrice_adiacenza[i, i] = 0
        grafo = Grafo(matrice_adiacenza, n, False)
        return grafo
    else:
        return None


def check_params(n, peso_max, perc_conn):
    if n <= 0:
        print("Valore di n non accettabile. Serve un valore positivo")
        return False
    if peso_max <= 0:
        print("Valore di peso_max non accettabile. Serve un valore positivo.")
        return False
    if perc_conn < 0 or perc_conn > 100:
        print("Valore di perc_conn non accettabile. Serve 0<=perc_conn<=100")
        return False
    return True
