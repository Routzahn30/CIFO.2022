import numpy as np
import matplotlib.pyplot as plt
import random


NUMBER_POINTS = 10
MAX_X = 100
MAX_Y = 100

if __name__ == '__main__':

    with open('random_data.txt', 'w') as f:
        for i in range(1, NUMBER_POINTS+1):
            x = random.randint(0,MAX_X)
            y = random.randint(0,MAX_Y)
            f.write(f"{i} {x} {y}\n")
        f.close()
