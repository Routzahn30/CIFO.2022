from random import uniform, choice
from operator import attrgetter
import random
from numpy.random import choice as np_choice


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
        individuals = population.individuals
        sorted_pop = sorted(individuals, key=lambda x: x.fitness, reverse=False)

        weights = []
        for k, v in enumerate(sorted_pop):
            weights.append((k + 1) / sum(range(len(sorted_pop) + 1)))

        draw = random.choices(sorted_pop, weights, k=1)[0]

    elif population.optim == "min":
        individuals = population.individuals
        sorted_pop = sorted(individuals, key=lambda x: x.fitness, reverse=True)

        weights = []
        for k, v in enumerate(sorted_pop):
            weights.append((k + 1) / sum(range(len(sorted_pop) + 1)))

        draw = random.choices(sorted_pop, weights, k=1)[0]

    return draw


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        # Sum total fitness
        individuals = [choice(population.individuals) for i in range(1, len(population.individuals))]
        sorted_pop = individuals.sort(key=attrgetter('fitness'), reverse=True)

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
