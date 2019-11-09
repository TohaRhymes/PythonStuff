#%%


DNA1 = 'TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC'
DNA2 = 'AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC'

DNA1 = '-' + DNA1
DNA2 = '-' + DNA2

#%%
# test1
match = 1
mismatch = -1
gap_open = 0
gap_extension = -1

#%%
# test2
match = 1
mismatch = -1
gap_open = -100
gap_extension = -0.01

#%%
# test3
match = 1
mismatch = -1
gap_open = 0.5
gap_extension = -0.3


#%%


# 0 - horizontal, 1 - main, 2 - vertical

level_weight = [[[0] * len(DNA2) for i in range(len(DNA1))] for j in range(3)]
steps = [[['not'] * len(DNA2) for i in range(len(DNA1))] for j in range(3)]

for i in range(len(DNA2)):
    level_weight[0][0][i] = i * gap_extension + gap_open
    level_weight[1][0][i] = i * gap_extension + gap_open
    level_weight[2][0][i] = float('-inf')

for i in range(len(DNA1)):
    level_weight[2][i][0] = i * gap_extension + gap_open
    level_weight[1][i][0] = i * gap_extension + gap_open
    level_weight[0][i][0] = float('-inf')

# level_weight[0][0][0] = 0
level_weight[1][0][0] = 0
# level_weight[2][0][0] = 0

for i in range(3):
    steps[i][0][0] = 'start'

for i in range(1, len(DNA1)):
    for j in range(1, len(DNA2)):
        this_way = 'not'
        max_weight = float('-inf')
        if level_weight[2][i - 1][j] + gap_extension > max_weight:
            max_weight = level_weight[2][i - 1][j] + gap_extension
            this_way = 'this'
        if level_weight[1][i - 1][j] + gap_extension + gap_open > max_weight:
            max_weight = level_weight[1][i - 1][j] + gap_extension + gap_open
            this_way = 'down'
        level_weight[2][i][j] = max_weight
        steps[2][i][j] = this_way

        max_weight = float('-inf')
        if level_weight[0][i][j - 1] + gap_extension > max_weight:
            max_weight = level_weight[0][i][j - 1] + gap_extension
            this_way = 'this'
        if level_weight[1][i][j - 1] + gap_extension + gap_open > max_weight:
            max_weight = level_weight[1][i][j - 1] + gap_extension + gap_open
            this_way = 'up'
        level_weight[0][i][j] = max_weight
        steps[0][i][j] = this_way

        max_weight = float('-inf')
        if level_weight[0][i][j] > max_weight:
            max_weight = level_weight[0][i][j]
            this_way = 'down'
        if level_weight[2][i][j] > max_weight:
            max_weight = level_weight[2][i][j]
            this_way = 'up'
        if DNA1[i] == DNA2[j] and level_weight[1][i - 1][j - 1] + match > max_weight:
            max_weight = level_weight[1][i - 1][j - 1] + match
            this_way = 'this'
        if DNA1[i] != DNA2[j] and level_weight[1][i - 1][j - 1] + mismatch > max_weight:
            max_weight = level_weight[1][i - 1][j - 1] + mismatch
            this_way = 'this'
        level_weight[1][i][j] = max_weight
        steps[1][i][j] = this_way

# now find alignments
alignment_DNA1 = ''
alignment_DNA2 = ''
next_i = len(DNA1) - 1
next_j = len(DNA2) - 1
this_level = 1
this_way = steps[this_level][next_i][next_j]
while next_i != 0 and next_j != 0:
    if this_level == 1:
        if this_way == 'this':
            alignment_DNA1 += DNA1[next_i]
            alignment_DNA2 += DNA2[next_j]
            next_i -= 1
            next_j -= 1
            this_way = steps[this_level][next_i][next_j]
            continue
        elif this_way == 'up':
            this_level += 1
        elif this_way == 'down':
            this_level -= 1
        this_way = steps[this_level][next_i][next_j]
    if this_level == 0:
        if this_way == 'this':
            alignment_DNA2 += DNA2[next_j]
            alignment_DNA1 += '-'
            next_j -= 1
            this_way = steps[this_level][next_i][next_j]
            continue
        elif this_way == 'up':
            this_level += 1
            alignment_DNA2 += DNA2[next_j]
            alignment_DNA1 += '-'
            next_j -= 1
            this_way = steps[this_level][next_i][next_j]
            continue
    if this_level == 2:
        if this_way == 'this':
            alignment_DNA1 += DNA1[next_i]
            alignment_DNA2 += '-'
            next_i -= 1
            this_way = steps[this_level][next_i][next_j]
            continue
        elif this_way == 'down':
            this_level -= 1
            alignment_DNA1 += DNA1[next_i]
            alignment_DNA2 += '-'
            next_i -= 1
            this_way = steps[this_level][next_i][next_j]
            continue

if this_way != 'start':
    if next_i == 0:
        while next_j > 0:
            alignment_DNA2 += DNA2[next_j]
            alignment_DNA1 += '-'
            next_j -= 1
            this_way = steps[this_level][next_i][next_j]
    if next_j == 0:
        while next_i > 0:
            alignment_DNA1 += DNA1[next_i]
            alignment_DNA2 += '-'
            next_i -= 1
            this_way = steps[this_level][next_i][next_j]

alignment_DNA1 = alignment_DNA1[::-1]
alignment_DNA2 = alignment_DNA2[::-1]

# and print it
print(alignment_DNA1)
print(alignment_DNA2)


