from random import sample, choice

import numpy as np


def swap_mutation(individual):

    random_routes = sample(range(len(individual)), 2)
    random_route_1 = random_routes[0]
    random_point_1 = choice(range(len(individual[random_route_1])))

    random_route_2 = random_routes[1]
    random_point_2 = choice(range(len(individual[random_route_2])))

    individual[random_route_1][random_point_1], individual[random_route_2][random_point_2] = individual[random_route_2][random_point_2], individual[random_route_1][random_point_1]

    return individual


if __name__ == '__main__':

    test = [[14,  2, 12, 11,  1, 18, 19], [8, 13, 15, 16, 20, 10,  4], [17,  9,  7,  6,  3,  5]]

    mutated = swap_mutation(test)
    print(mutated)