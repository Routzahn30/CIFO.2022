import random
from random import sample, choice

import numpy as np


def swap_mutation(individual):

    # Remember where the list was cut
    cutoffs = [0]
    for route in individual:
        cutoffs.append(len(route)+cutoffs[-1:][0])

    # Get a flat list of all the routes
    p_flat = [item for sublist in individual for item in sublist]
    #


    mut_points = sample(range(len(p_flat)), 2)

    p_flat[mut_points[0]], p_flat[mut_points[1]] = p_flat[mut_points[1]], p_flat[mut_points[0]]

    # Organizing the arrays again according to the original cuts
    new_list = []
    for cutoff in range(len(cutoffs) - 1):
        list_slice = p_flat[cutoffs[cutoff]:cutoffs[cutoff + 1]]
        new_list.append(list_slice)
    #

    return new_list


def inversion_mutation(individual):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """

    # Remember where the list was cut
    cutoffs = [0]
    for route in individual:
        cutoffs.append(len(route) + cutoffs[-1:][0])

    # Get a flat list of all the routes
    p_flat = [item for sublist in individual for item in sublist]
    #

    # Position of the start and end of substring
    mut_points = sample(range(len(p_flat)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation
    p_flat[mut_points[0]:mut_points[1]] = p_flat[mut_points[0]:mut_points[1]][::-1]

    # Organizing the arrays again according to the original cuts
    new_list = []
    for cutoff in range(len(cutoffs) - 1):
        list_slice = p_flat[cutoffs[cutoff]:cutoffs[cutoff + 1]]
        new_list.append(list_slice)
    #

    return new_list


def scramble_mutation(individual):
    cutoffs = [0]
    for route in individual:
        cutoffs.append(len(route) + cutoffs[-1:][0])

    # Get a flat list of all the routes
    p_flat = [item for sublist in individual for item in sublist]
    #

    # Position of the start and end of substring
    mut_points = sample(range(len(p_flat)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation

    p_flat[mut_points[0]:mut_points[1]] = sorted(p_flat[mut_points[0]:mut_points[1]], key=lambda x: random.random())


    # Organizing the arrays again according to the original cuts
    new_list = []
    for cutoff in range(len(cutoffs) - 1):
        list_slice = p_flat[cutoffs[cutoff]:cutoffs[cutoff + 1]]
        new_list.append(list_slice)
    #

    return new_list


if __name__ == '__main__':

    test = [[14,  2, 12, 11,  1, 18, 19], [8, 13, 15, 16, 20, 10,  4], [17,  9,  7,  6,  3,  5]]

    mutated = scramble_mutation(test)
    print(mutated)