import chromossome
import crossover
import random
import numpy as np
from itertools import islice
from random import randint
from crossover import multipoint_crossover
from mutation import swap_mutation
from data.vrp_data import distance_matrix
from ind_pop import Population, Individual
from selection import tournament
from crossover import multipoint_crossover
from mutation import swap_mutation
from reparations import reparations


def get_fitness(self):
    fitness = 0

    for truck in range(len(self.representation)):
        # print(truck)
        truck_distance = 0
        for route in range(0, len(self.representation[truck])):
            # print(route)
            current = self.representation[truck][route]

            if route == 0:
                previous = 0
            else:
                previous = self.representation[truck][route - 1]
            distance = distance_matrix[previous][current]
            truck_distance += distance

        # Add distance from last delivery spot to depot

        current = 0
        previous = self.representation[truck][-1:][0]
        distance = distance_matrix[previous][current]
        truck_distance += distance

        fitness += truck_distance


    return fitness

# Monkey patching
Individual.get_fitness = get_fitness


pop = Population(
    size=20,
    sol_size=len(distance_matrix[0])-1,
    valid_set=[i for i in range(1,len(distance_matrix[0]))],
    replacement=False,
    optim="min",
    n_trucks=2,
)

pop.evolve(
    gens=100,
    select=tournament,
    crossover=multipoint_crossover,
    mutate=swap_mutation,
    reparations=reparations,
    co_p=0.9,
    mu_p=0.1,
    elitism=True
)

