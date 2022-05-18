import matplotlib.pyplot as plt
from data.vrp_data_random import MAX_X, MAX_Y
import pandas as pd
from scipy.spatial import distance_matrix


def scatter_plot(file):
    data = []
    names = []

    with open(file) as f:
        for line in f:
            (name, x, y) = line.split()
            data.append([float(x), float(y)])
            names.append(name)
        f.close()

    plt.scatter(*zip(*data))
    plt.scatter(MAX_X/2, MAX_Y/2, c="r")

    df = pd.DataFrame(data,columns=["x","y"], index = names)
    distance_df = pd.DataFrame(distance_matrix(df.values,df.values),index=df.index,columns=df.index)
    print(distance_df)

    plt.show()


scatter_plot("data/random_data.txt")
