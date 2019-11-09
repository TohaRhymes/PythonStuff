
DNA1 = 'TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC'
DNA2 = 'AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC'



DNA1 = '-' + DNA1
DNA2 = '-' + DNA2

weight = [[0] * len(DNA2) for i in range(len(DNA1))]
steps = [['not'] * len(DNA2) for i in range(len(DNA1))]


# scoring system test 1
match = 1
mismatch = -1
indel = -1


for i in range(0, len(DNA1)):
    for j in range(0, len(DNA2)):
        best_step = 'not'
        max_weight = float("-inf")
        # Find the best step.
        if i > 0 and j > 0 and DNA1[i] == DNA2[j] and weight[i - 1][j - 1] + match > max_weight:
            best_step = 'up_left'
            max_weight = weight[i - 1][j - 1] + match
        if i > 0 and j > 0 and DNA1[i] != DNA2[j] and weight[i - 1][j - 1] + mismatch > max_weight:
            best_step = 'up_left'
            max_weight = weight[i - 1][j - 1] + mismatch
        if i > 0 and weight[i - 1][j] + indel > max_weight:
            best_step = 'up'
            max_weight = weight[i - 1][j] + indel
        if j > 0 and weight[i][j - 1] + indel > max_weight:
            best_step = 'left'
            max_weight = weight[i][j - 1] + indel
            # if the best step exists (it doesn't exist only if i==0 and j==0), save this step.
        if best_step != 'not':
            weight[i][j] = max(0,max_weight)
            steps[i][j] = best_step

# now find alignments
alignment_DNA1 = ''
alignment_DNA2 = ''
next_i = len(DNA1) - 1
next_j = len(DNA2) - 1
while steps[next_i][next_j] != 'not':
    if steps[next_i][next_j] == 'up_left':
        alignment_DNA1 += DNA1[next_i]
        alignment_DNA2 += DNA2[next_j]
        next_i -= 1
        next_j -= 1
    elif steps[next_i][next_j] == 'up':
        alignment_DNA1 += DNA1[next_i]
        alignment_DNA2 += '-'
        next_i -= 1
    elif steps[next_i][next_j] == 'left':
        alignment_DNA2 += DNA2[next_j]
        alignment_DNA1 += '-'
        next_j -= 1
alignment_DNA1 = alignment_DNA1[::-1]
alignment_DNA2 = alignment_DNA2[::-1]

# and print it
print(alignment_DNA1)
print(alignment_DNA2)
