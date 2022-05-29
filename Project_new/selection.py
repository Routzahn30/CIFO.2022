from random import uniform, choice
from operator import attrgetter
import random

def tournament(population, size=10):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select individuals based on tournament size
    tournament = [choice(population.individuals) for i in range(size)]
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")

def rank(population):

    if population.optim == "max":
        # Sum total fitness
        individuals = [choice(population.individuals) for i in range(1,len(population.individuals))]
        sorted_pop = individuals.sort(key=attrgetter('fitness'), reverse=True)
        print(individuals)

        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        positions = []
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            positions.append(position)
            if position > spin and position/sum(positions) > random.uniform(0, 1):
                return individual

    elif population.optim == "min":
        raise NotImplementedError

    else:
        raise Exception("No optimization specified (min or max).")

def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        # Sum total fitness
        individuals = [choice(population.individuals) for i in range(1,len(population.individuals))]
        sorted_pop = individuals.sort(key=attrgetter('fitness'), reverse=True)
        print(individuals)

        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual

    elif population.optim == "min":
        raise NotImplementedError

    else:
        raise Exception("No optimization specified (min or max).")


