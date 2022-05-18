import chromossome
import crossover
import random
import numpy as np
from itertools import islice
from random import randint
from crossover import multipoint_crossover
from mutation import swap_mutation

if __name__ == "__main__":

    n_trucks = 3
    n_cities = 20

    cities = [i for i in range(1, n_cities+1)]
    trucks = [i for i in range(1, n_trucks+1)]

    np.random.shuffle(cities)
    routes = np.array_split(cities, n_trucks)

    np.random.shuffle(cities)
    routes_2 = np.array_split(cities, n_trucks)

    print(routes)
    print(routes_2)

    o1, o2 = multipoint_crossover(routes, routes_2, n_trucks)

    print(o1)
    print(o2)
    mutated = swap_mutation(o1)

    print(mutated)

    print("VRP")
    print(routes)
    print(routes_2)
    print("\nTSP")
    print(cities)

