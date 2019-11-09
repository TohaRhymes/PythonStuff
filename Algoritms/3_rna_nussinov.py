# %%
# functions
def recursive_pairs(next_i, next_j):
    while steps[next_i][next_j] != 'not':
        if type(steps[next_i][next_j]) == str and steps[next_i][next_j] == 'left':
            next_j -= 1
        elif type(steps[next_i][next_j]) == str and steps[next_i][next_j] == 'down':
            next_i += 1
        elif type(steps[next_i][next_j]) == str and steps[next_i][next_j] == 'pair':
            pairs.append([next_i, next_j])
            next_j -= 1
            next_i += 1
        else:
            recursive_pairs(steps[0][0], steps[0][1])
            recursive_pairs(steps[1][0], steps[1][1])

# %%
# test1

rna = 'GGACC'

# %%
# test2

rna = 'AAACAUGAGGAUUACCCAUGU'

# %%


# weight[i][j] = max amount of complemented digits in area [i,j]
weight = [[0] * len(rna) for i in range(len(rna))]
steps = [['not'] * len(rna) for i in range(len(rna))]
complementary_nucleotide = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
minimum_hairpin_length = 3

for i in range(minimum_hairpin_length + 1, len(rna)):
    for j in range(0, len(rna) - i):
        x = j
        y = j + i
        max_weight = float('-inf')
        step = 'not'
        if weight[x + 1][y] > max_weight:
            max_weight = weight[x + 1][y]
            step = 'down'
        if weight[x][y - 1] > max_weight:
            max_weight = weight[x][y - 1]
            step = 'left'
        if complementary_nucleotide[rna[x]] == rna[y] and weight[x + 1][y - 1] + 1 > max_weight:
            max_weight = weight[x + 1][y - 1] + 1
            step = 'pair'
        for k in range(x + 1, y - 1):
            if weight[x][k] + weight[k + 1][y] > max_weight:
                max_weight = weight[x][k] + weight[k + 1][y]
                step = [[x, k], [k + 1, y]]
        weight[x][y] = max_weight
        steps[x][y] = step

pairs = []
recursive_pairs(0, len(rna) - 1)

# and print answer
for i in range(0, len(pairs)):
    print(str(pairs[i]))
