# coding: utf-8

# In[99]:


DNA1 = 'CCGGGGGC'
DNA2 = 'GCGGGGGGGGGGGGGGGC'

# CCCATG
# ATGCCT


# In[100]:


DNA1 = '-' + DNA1
DNA2 = '-' + DNA2

# In[101]:


weight = [[0] * len(DNA2) for i in range(len(DNA1))]
steps = [['not'] * len(DNA2) for i in range(len(DNA1))]

# In[102]:


# new scoring system with Matrix of Weights
# A-A, T-T, G-G, C-C -- +1 (that's the best option); A-G and T-C -- +0.5 (they have the same length);
# A-T, A-C, G-T, G-C -- -0.5 (they don't have the same length); gap -- -1 (the worst situation)
letters_index = {'A': 0, 'T': 1, 'G': 2, 'C': 3, '-': 4}
scores = [[1, -0.5, 0.5, -0.5, -2],
          [-0.5, 1, -0.5, 0.5, -2],
          [0.5, -0.5, 1, -0.5, -2],
          [-0.5, 0.5, -0.5, 1, -2],
          [-2, -2, -2, -2, -2]]

# In[103]:


print(letters_index['T'])

# In[104]:


# Needleman - Wunsch
for i in range(0, len(DNA1)):
    for j in range(0, len(DNA2)):
        best_step = 'not'
        max_weight = float("-inf")
        # Find the best step.
        if i > 0 and j > 0 and weight[i - 1][j - 1] + scores[letters_index[DNA1[i]]][
            letters_index[DNA2[j]]] > max_weight:
            print(1)
            best_step = 'up_left'
            max_weight = weight[i - 1][j - 1] + scores[letters_index[DNA1[i]]][letters_index[DNA2[j]]]
        if i > 0 and weight[i - 1][j] + scores[letters_index[DNA1[i]]][letters_index['-']] > max_weight:
            print(2)
            best_step = 'up'
            max_weight = weight[i - 1][j] + scores[letters_index[DNA1[i]]][letters_index['-']]
        if j > 0 and weight[i][j - 1] + scores[letters_index[DNA2[j]]][letters_index['-']] > max_weight:
            print(3)
            best_step = 'left'
            max_weight = weight[i][j - 1] + scores[letters_index[DNA2[j]]][letters_index['-']]
            # if the best step exists (it doesn't exist only if i==0 and j==0), save this step.
        if best_step != 'not':
            print()
            weight[i][j] = max_weight
            steps[i][j] = best_step

# In[105]:


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

# In[106]:


# and print it
print(alignment_DNA1)
print(alignment_DNA2)
