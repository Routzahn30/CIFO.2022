from random import randint, uniform, sample
import numpy as np
import random


def single_point_co(p1, p2, n_trucks=None):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    cutoffs_1 = [0]
    cutoffs_2 = [0]

    for route in p1:
        cutoffs_1.append(len(route) + cutoffs_1[-1:][0])
    for route in p2:
        cutoffs_2.append(len(route) + cutoffs_2[-1:][0])

    p1_flat = [item for sublist in p1.representation for item in sublist]
    p2_flat = [item for sublist in p2.representation for item in sublist]

    co_point = randint(1, len(p1_flat) - 2)

    offspring1 = p1_flat[:co_point] + p2_flat[co_point:]
    offspring2 = p2_flat[:co_point] + p1_flat[co_point:]

    result_1 = []
    for cutoff in range(len(cutoffs_1) - 1):
        list_slice = offspring1[cutoffs_1[cutoff]:cutoffs_1[cutoff + 1]]
        result_1.append(list_slice)
    #

    result_2 = []
    for cutoff in range(len(cutoffs_2) - 1):
        list_slice = offspring2[cutoffs_2[cutoff]:cutoffs_2[cutoff + 1]]
        result_2.append(list_slice)
    #

    return result_1, result_2


def multipoint_crossover(p1, p2, n_trucks):
    p1_flat = [item for sublist in p1.representation for item in sublist]
    p2_flat = [item for sublist in p2.representation for item in sublist]

    # Set a number of points equal to the number of trucks - 1
    # A final point is added equal to the total length of the individual
    # These points will serve as dividers between trucks
    # Example: If dividers = [3,9,13]
    # offspring shape: [[x,x,x][x,x,x,x,x,x],[x,x,x,x]]
    dividers = np.sort(np.append(random.sample(range(1, len(p1_flat) - 2), n_trucks - 1), len(p1_flat)))

    offspring_1 = []
    offspring_2 = []

    i = 0

    # Cross the parents to create multiple offsprings
    # offspring1 -> [x,x,x][y,y,y,y,y,y][x,x,x,x]
    # offspring2 -> [y,y,y][x,x,x,x,x,x][y,y,y,y]
    for index, point in enumerate(dividers):
        p1_section = p1_flat[i:point]
        p2_section = p2_flat[i:point]

        if index % 2 == 0:
            offspring_1.append(p1_section)
            offspring_2.append(p2_section)
        else:
            offspring_1.append(p2_section)
            offspring_2.append(p1_section)

        i = point

    return offspring_1, offspring_2


def uniform_crossover(p1, p2, n_trucks):
    p1_flat = [item for sublist in p1.representation for item in sublist]
    p2_flat = [item for sublist in p2.representation for item in sublist]
    dividers = np.sort(np.append(random.sample(range(1, len(p1_flat) - 2), n_trucks - 1), len(p1_flat)))

    offspring_1 = []
    offspring_2 = []
    number_list = [0, 1]
    # random item from list
    # print(random.choice(number_list))
    ran = []
    for i in range(0, len(p1_flat)):
        aux = 0
        to_switch = random.choice(number_list)
        ran.append(to_switch)
        if to_switch == 0:
            aux = p1_flat[i]
            p1_flat[i] = p2_flat[i]
            p2_flat[i] = aux
    dividers = np.sort(np.append(random.sample(range(1, len(p1_flat) - 2), n_trucks - 1), len(p1_flat)))
    offspring_1 = []
    offspring_2 = []
    i = 0
    for index, point in enumerate(dividers):
        p1_section = p1_flat[i:point]
        p2_section = p2_flat[i:point]

        if index % 2 == 0:
            offspring_1.append(p1_section)
            offspring_2.append(p2_section)
        else:
            offspring_1.append(p2_section)
            offspring_2.append(p1_section)

        i = point

    return offspring_1, offspring_2


if __name__ == '__main__':
    # p1, p2 = [9, 8, 4, 5, 6, 7, 1, 3, 2, 10], [8, 7, 1, 2, 3, 10, 9, 5, 4, 6]
    # p1, p2 = [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 3, 7, 8, 2, 6, 5, 1, 4]
    # p1, p2 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], [0.3, 0.2, 0.3, 0.2, 0.3, 0.2, 0.3, 0.2, 0.3]
    p1, p2 = [[6, 10, 5, 7], [9, 2, 3, 8], [11, 12, 1, 4]], [[2, 11, 5, 8], [6, 1, 12, 10], [7, 9, 4, 3]]
    #o1, o2 = single_point_co(p1, p2, 3)
    print(multipoint_crossover.__name__)
