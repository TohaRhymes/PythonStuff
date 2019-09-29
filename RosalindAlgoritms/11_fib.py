# inFile = open('input.txt')
inFile = open('rosalind_fib.txt')
outFile = open('output.txt', 'w')
n, k = map(int, inFile.read().split())
inFile.close
fib = [0] * n
fib[0] = 1
fib[1] = 1
print()
for i in range(2, n):
    fib[i] = k * fib[i - 2] + fib[i - 1]
outFile.write(str(fib[n - 1]))
outFile.close
