import crossover
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from itertools import islice
from random import randint
from crossover import multipoint_crossover
from mutation import swap_mutation
#from data.vrp_data import distance_matrix
from data.data_vrp_bangladesh import distance_matrix as distance_matrix
from ind_pop import Population, Individual
from selection import tournament, fps, rank
from crossover import multipoint_crossover, single_point_co, uniform_crossover
from mutation import swap_mutation, inversion_mutation, scramble_mutation
from reparations import reparations

DEPOT = 0


def get_fitness(self):
    fitness = 0

    for truck in range(len(self.representation)):
        truck_distance = 0

        # For each point the truck has to travel, the distance to the previous point will be measured
        for point in range(0, len(self.representation[truck])):
            current = self.representation[truck][point]

            # If it is the starting point of a route, the previous point will be the depot
            if point == 0:
                previous = DEPOT
            else:
                previous = self.representation[truck][point - 1]

            distance = distance_matrix[previous][current]

            truck_distance += distance

        # After adding the distance to all points,
        # the distance of the final point to the depot will be added to the total
        current = DEPOT

        # previous = last point of the truck route
        previous = self.representation[truck][-1:][0]

        distance = distance_matrix[previous][current]
        truck_distance += distance

        # Fitness is equal to the total of the distances done by each truck
        fitness += truck_distance

    return fitness


# Monkey patching
Individual.get_fitness = get_fitness

best_individuals = []


#VARIABLES

N_TRIES = 5

SIZE = 200
N_TRUCKS = 5
GENS = 100
OPTIM = "min"
SELECT = tournament
CROSSOVER = multipoint_crossover
MUTATION = inversion_mutation
CO_P = 0.8
MU_P = 0.3


for i in range(N_TRIES):

    pop = Population(
        size=SIZE,
        sol_size=len(distance_matrix[0]) - 1,
        valid_set=[i for i in range(0, len(distance_matrix[0])) if i is not DEPOT],
        replacement=False,
        optim=OPTIM,
        n_trucks=N_TRUCKS,
    )

    fitness_info, best_individual = pop.evolve(
        gens=GENS,
        select=SELECT,
        crossover=CROSSOVER,
        mutate=MUTATION,
        reparations=reparations,
        co_p=CO_P,
        mu_p=MU_P,
        elitism=True
    )

    best_individuals.append(best_individual)
    plt.plot(fitness_info)

image_name = f"N_tries- {N_TRIES},SIZE- {SIZE},N_TRUCKS- {N_TRUCKS},GENES- {GENS},SELECT- {SELECT.__name__}," \
             f"CROSSOVER-{CROSSOVER.__name__},MUTATION- {MUTATION.__name__},CO_P- {CO_P},MU_P- {MU_P}," \
             f"DATETIME- {datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p')} "

plt.ylabel("Fitness")
plt.xlabel("Genes")
plt.savefig(f"plots/{image_name}.png")



for ind in best_individuals:
    print(ind)

plt.show()

