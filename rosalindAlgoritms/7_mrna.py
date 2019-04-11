Mass_table = {
    'A': 4,
    'C': 2,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 4,
    'H': 2,
    'I': 3,
    'K': 2,
    'L': 6,
    'M': 1,
    'N': 2,
    'P': 4,
    'Q': 2,
    'R': 6,
    'S': 6,
    'T': 4,
    'V': 4,
    'W': 1,
    'Y': 2
}
# inFile = open('input.txt')
inFile = open('rosalind_mrna.txt')
outFile = open('output.txt', 'w')
s = str(inFile.read())
inFile.close
result = 3
for char in s:
    result *= Mass_table[char]
    result = result % 1000000
outFile.write(str(result))
outFile.close
