import copy

# test1
n = 4
str_names = 'A,B,C,D'
names = str_names.split(',')
weights = [[16, 16, 10],
           [8, 8],
           [4]]

# test2
n = 6
str_names = 'A,B,C,D,E,F'
names = str_names.split(',')
weights = [[5, 4, 7, 6, 8],
           [7, 10, 9, 11],
           [7, 6, 8],
           [5, 9],
           [8]]



tree_matrix = [[float('+inf')] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    # all leaves, weight, newick formula
    tree_matrix[0][i] = [names[i - 1], 0, names[i - 1]]
    tree_matrix[i][0] = [names[i - 1], 0, names[i - 1]]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        tree_matrix[i][j] = weights[i - 1][j - i - 1]

while len(tree_matrix) > 2:
    # find max and index.
    min_el = float('+inf')
    i_min = -1
    j_min = -1
    for i in range(1, len(tree_matrix)):
        for j in range(i + 1, len(tree_matrix[i])):
            if tree_matrix[i][j] < min_el:
                min_el = tree_matrix[i][j]
                i_min = i
                j_min = j
    newick_sys = '(' + tree_matrix[0][i_min][2] + ':' + str(min_el / 2 - tree_matrix[0][i_min][1]) + ', ' + \
                 tree_matrix[0][j_min][2] + ':' + str(min_el / 2 - tree_matrix[0][j_min][1]) + ')'
    new_name = tree_matrix[0][i_min][0] + tree_matrix[0][j_min][0]
    new_point = [new_name, min_el / 2, newick_sys]

    new_matrix = copy.deepcopy(tree_matrix)
    # deleting rows and columns of merged points
    del new_matrix[max(i_min, j_min)]
    del new_matrix[min(i_min, j_min)]

    for i in range(0, len(new_matrix)):
        del new_matrix[i][max(i_min, j_min)]
        del new_matrix[i][min(i_min, j_min)]

    # adding new point
    new_matrix.append([float('+inf')] * (len(new_matrix[0])))
    new_matrix[len(new_matrix) - 1][0] = copy.deepcopy(new_point)
    new_matrix[0].append(copy.deepcopy(new_point))
    new_matrix[len(new_matrix) - 1].append(float('+inf'))
    for i in range(1, len(new_matrix) - 1):
        i_old = i
        if i_old >= min(i_min, j_min):
            i_old += 1
        if i_old >= max(i_min, j_min):
            i_old += 1
        # if i!=i_min and i!=j_min:
        distance1 = tree_matrix[min(i_old, i_min)][max(i_old, i_min)]
        distance2 = tree_matrix[min(i_old, j_min)][max(i_old, j_min)]
        avg = (distance1 + distance2) / 2
        new_matrix[i].append(avg)
    tree_matrix = new_matrix

answer = tree_matrix[0][len(tree_matrix[0]) - 1][2]
print(answer)
