# %%

# imports
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
distance_to_every = [0 for i in range(n)]
for i in range(len(distance_to_every)):
    for j in range(len(distance_to_every)):
        if i != j:
            cur_i = min(i, j)
            cur_j = max(i, j)
            distance_to_every[i] += weights[cur_i][cur_j - cur_i - 1]

for i in range(1, n + 1):
    # all leaves, weight, newick formula
    tree_matrix[0][i] = [names[i - 1], 0, names[i - 1]]
    tree_matrix[i][0] = [names[i - 1], 0, names[i - 1]]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        tree_matrix[i][j] = weights[i - 1][j - i - 1]

while len(tree_matrix) > 3:
    # find max and index.
    min_pair_distance = float('+inf')
    i_min = -1
    j_min = -1
    for i in range(1, len(tree_matrix)):
        for j in range(i + 1, len(tree_matrix[i])):
            # Делим на len(tree_matrix)-3, а не -2, т.к. там одна строчка (нулевая) служебная
            distance = tree_matrix[i][j] - (distance_to_every[i - 1] - tree_matrix[i][j]) / (len(tree_matrix) - 3) - (
                    distance_to_every[j - 1] - tree_matrix[i][j]) / (len(tree_matrix) - 3)
            if distance < min_pair_distance:
                min_pair_distance = distance
                i_min = i
                j_min = j
    i_min, j_min = [min(i_min, j_min), max(i_min, j_min)]
    distance_from_point_to_i = 0.5 * (
            tree_matrix[i_min][j_min] + (distance_to_every[i_min - 1] - tree_matrix[i_min][j_min]) / (
            len(tree_matrix) - 3) - (distance_to_every[j_min - 1] - tree_matrix[i_min][j_min]) / (
                    len(tree_matrix) - 3))
    distance_from_point_to_j = 0.5 * (
            tree_matrix[i_min][j_min] - (distance_to_every[i_min - 1] - tree_matrix[i_min][j_min]) / (
            len(tree_matrix) - 3) + (distance_to_every[j_min - 1] - tree_matrix[i_min][j_min]) / (
                    len(tree_matrix) - 3))
    # todo проверить надо ли вычитать в следующей строчке
    newick_sys = '(' + tree_matrix[0][i_min][2] + ':' + str(distance_from_point_to_i) + ', ' + \
                 tree_matrix[0][j_min][2] + ':' + str(distance_from_point_to_j) + ')'
    new_name = tree_matrix[0][i_min][0] + tree_matrix[0][j_min][0]
    new_point = [new_name, 0, newick_sys]

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
        if i_old >= i_min:
            i_old += 1
        if i_old >= j_min:
            i_old += 1
        dis_to_i = 0.5 * (tree_matrix[min(i_old, j_min)][max(i_old, j_min)] + tree_matrix[min(i_old, i_min)][
            max(i_old, i_min)] - tree_matrix[i_min][j_min])

        new_matrix[i].append(dis_to_i)
    tree_matrix = new_matrix
    # изменим матрицу расстоений от i до всех
    distance_to_every = [0 for i in range(len(new_matrix) - 1)]
    for i in range(len(distance_to_every)):
        for j in range(len(distance_to_every)):
            if i != j:
                distance_to_every[i] += tree_matrix[min(i, j) + 1][max(i, j) + 1]


# В википедии написано: "When an unrooted tree is represented in Newick notation, an arbitrary node is chosen as its
# root." Так как получаем неукорененное дерево, то корень подвешиваю за середину расстояния между 2мя оставшимися вершинами.
distance_from_root = tree_matrix[1][2] / 2
answer = '(' + tree_matrix[0][len(tree_matrix[0]) - 2][2] + ':' + str(distance_from_root) + ', ' + \
         tree_matrix[0][len(tree_matrix[0]) - 1][2] + ':' + str(distance_from_root) + ')'


# answer
print(answer)
