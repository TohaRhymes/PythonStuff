def factorial(a):
    b=1
    for i in range(2, a+1, 1):
        b*=i
    return b
# inFile = open('input.txt')
inFile = open('rosalind_pmch.txt')
outFile = open('output.txt', 'w')
s = inFile.read()
inFile.close()
AU = 0
GC = 0
for char in s:
    if (char == 'A'):
        AU += 1
    if (char == 'G'):
        GC += 1
outFile.write(str(factorial(AU)*factorial(GC)))
outFile.close()