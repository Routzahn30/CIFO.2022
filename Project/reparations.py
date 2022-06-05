from data.vrp_data import distance_matrix


def reparations(p, valid_set):
    cutoffs = [0]
    for route in p:
        cutoffs.append(len(route) + cutoffs[-1:][0])

    p_flat = [item for sublist in p for item in sublist]

    seen_set = []
    repeated = {}

    for i in range(len(p_flat)):
        if p_flat[i] not in seen_set:
            seen_set.append(p_flat[i])
        else:
            repeated[i] = p_flat[i]

    # List of points not represented in an individual
    difference = set(valid_set).difference(set(seen_set))

    # Replace repeated values with unseen values
    for k in repeated:
        p_flat[k] = difference.pop()

    new_list = []
    for cutoff in range(len(cutoffs) - 1):
        list_slice = p_flat[cutoffs[cutoff]:cutoffs[cutoff + 1]]
        new_list.append(list_slice)

    return new_list


if __name__ == "__main__":
    valid_set = [i for i in range(1, len(distance_matrix[0]))]
    test = [[12, 1, 11, 8, 4, 2, 2], [7], [3, 5, 7, 7]]
    print(reparations(test, valid_set))
