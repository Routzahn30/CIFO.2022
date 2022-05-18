from population import Population
from individual import Individual

from crossover import cycle_co, pmx_co
from selection import fps, tournament
from mutation import swap_mutation, inversion_mutation
from node import Node
from scipy.spatial import distance_matrix
import numpy as np
import pandas as pd


def distance(index, city):
    return distances.get(index)[city]


def get_fitness(chromosome):

    fitness = 0
    for(k, v) in chromosome:
        if k not in trucks:
            next_city = list(chromosome[k])[0]
            if next_city not in trucks:
                fitness += distance(k, next_city)

    return fitness


def decode_vrp(chromosome):
    chr_list = []
    for(k, v) in chromosome:
        if k in trucks[:(num_trucks-1)]:
            chr_list.append("-------")
            continue
        chr_list.append(cities.get(k))


cities = {0:'Almeria',1:'Cadiz',2:'Cordoba',3:'Granada',4:'Huelva',5:'Jaen',6:'Malaga',7:'Sevilla'}
w0 = [999, 454, 317, 165, 528, 222, 223, 410]
w1 = [453, 999, 253, 291, 210, 325, 234, 121]
w2 = [317, 252, 999, 202, 226, 108, 158, 140]
w3 = [165, 292, 201, 999, 344, 94, 124, 248]
w4 = [508, 210, 235, 346, 999, 336, 303, 94]
w5 = [222, 325, 116, 93, 340, 999, 182, 247]
w6 = [223, 235, 158, 125, 302, 185, 999, 206]
w7 = [410, 121, 141, 248, 93, 242, 199, 999]
distances = {0: w0, 1: w1, 2: w2, 3: w3, 4: w4, 5: w5, 6: w6, 7: w7}
trucks = ["truck1","truck2"]
num_trucks = len(trucks)
print(distances)