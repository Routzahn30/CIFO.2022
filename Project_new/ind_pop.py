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
        routes = np.stack(np.array_split(valid_set, n_trucks)).tolist()
        return routes

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}; Routes: {self.representation}"


class Population:
    def __init__(self, size, optim, n_trucks, valid_set, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.n_trucks = n_trucks
        self.valid_set = valid_set
        for _ in range(size):
            self.individuals.append(
                Individual(
                    size=kwargs["sol_size"],
                    replacement=kwargs["replacement"],
                    valid_set=valid_set,
                    n_trucks= n_trucks,
                )
            )

    def evolve(self, gens, select, crossover, reparations, mutate, co_p, mu_p, elitism):
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

                        #Reparataion
                        offspring1 = reparations(offspring1,self.valid_set)
                        offspring2 = reparations(offspring2,self.valid_set)
                    else:
                        offspring1, offspring2 = parent1.representation, parent2.representation

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


    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"

if __name__ == '__main__':
    ind = Individual(
        representation=[[2, 10, 3, 7], [5, 4, 11, 12], [1, 9, 8, 6]]
    )


