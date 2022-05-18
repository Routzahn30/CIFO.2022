import chromossome
import crossover
import random
import numpy as np
from itertools import islice
from random import randint

def random_chunk(li, trucks):
    it = iter(li)
    while True:
        nxt = list(islice(it,randint(trucks,trucks)))
        if nxt:
            yield nxt
        else:
            break

if __name__ == "__main__":

    n_trucks = 3
    n_cities = 20

    routes = []
    routes_2 = []

    cities = [i for i in range(1, n_cities+1)]
    trucks = [i for i in range(1, n_trucks+1)]

    for i in trucks:
        route = random.sample(cities, 5)
        routes.append(route)

        route_2 = random.sample(cities, 5)
        routes_2.append(route_2)


    random_list = np.sort(np.append(random.sample(range(1, n_cities-2), n_trucks-1),19))
    print(random_list)


    flat_routes = [item for sublist in routes for item in sublist]
    flat_routes_2 = [item for sublist in routes_2 for item in sublist]
    print(flat_routes)
    print(flat_routes_2)

    crossover_result = crossover.single_point_co(flat_routes, flat_routes_2)
    offspring_1 = crossover_result[0]
    offspring_2 = crossover_result[1]

    i = 0
    for point in random_list:
        print(flat_routes[i:point])
        i = point

    print("VRP")
    print(routes)
    print(routes_2)
    print("\nTSP")
    print(cities)

