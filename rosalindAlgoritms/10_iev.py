# inFile = open('input.txt')
inFile = open('rosalind_iev.txt')
outFile = open('output.txt', 'w')
a, b, c, d, e, f = map(int, inFile.read().split())
inFile.close
percentage = (a + b + c + 3 * d / 4 + e / 2)
outFile.write(str(percentage * 2))
outFile.close()
