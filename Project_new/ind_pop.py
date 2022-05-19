from data.vrp_data import distance_matrix
from copy import deepcopy
from operator import attrgetter
from random import choice, sample, random
import numpy as np


class Individual:

    def __init__(
            self,
            representation=None,
            size=None,
            replacement=True,
            valid_set=None,
            n_trucks=None,
    ):
        if representation is None:
            self.representation = self.get_representation(valid_set,n_trucks)
        else:
            self.representation = representation

        self.fitness = self.get_fitness()


    def get_fitness(self):
        raise Exception("You need to monkey patch the fitness path.")

    def get_representation(self,valid_set,n_trucks):
        np.random.shuffle(valid_set)
        routes = np.array_split(valid_set, n_trucks)
        return routes


class Population:
    def __init__(self, size, optim, n_trucks, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.n_trucks = n_trucks
        for _ in range(size):
            self.individuals.append(
                Individual(
                    size=kwargs["sol_size"],
                    replacement=kwargs["replacement"],
                    valid_set=kwargs["valid_set"],
                    n_trucks= n_trucks
                )
            )

    def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism):
        for gen in range(gens):
            new_pop = []

            if elitism:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

                while len(new_pop) < self.size:
                    parent1, parent2 = select(self), select(self)
                    # Crossover
                    if random() < co_p:
                        offspring1, offspring2 = crossover(parent1,parent2,self.n_trucks)
                    else:
                        offspring1, offspring2 = parent1, parent2

                    #Mutation
                    if random() < mu_p:
                        offspring1 = mutate(offspring1)
                    if random() < mu_p:
                        offspring2 = mutate(offspring2)

                    new_pop.append(Individual(representation=offspring1))
                    if len(new_pop) < self.size:
                        new_pop.append(Individual(representation=offspring2))

                if elitism:
                    if self.optim == "max":
                        least = min(new_pop, key=attrgetter("fitness"))
                    elif self.optim == "min":
                        least = max(new_pop, key=attrgetter("fitness"))
                    new_pop.pop(new_pop.index(least))
                    new_pop.append(elite)

                self.individuals = new_pop

                if self.optim == "max":
                    print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
                elif self.optim == "min":
                    print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')

if __name__ == '__main__':
    ind = Individual(
        representation=[[2, 10, 3, 7], [5, 4, 11, 12], [1, 9, 8, 6]]
    )


