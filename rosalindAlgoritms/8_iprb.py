# inFile = open('input.txt')
inFile = open('rosalind_iprb.txt')
outFile = open('output.txt', 'w')
m, n, k = map(int, inFile.read().split())
inFile.close
a = m + n + k
full = a * (a - 1) / 2
rec = k * (k - 1) / 2
geter = n * (n - 1) / 2
rg = n * k
outFile.write(str(1 - (rec + geter / 4 + rg / 2) / full))
outFile.close()
