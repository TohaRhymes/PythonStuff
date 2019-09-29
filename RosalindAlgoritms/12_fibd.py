def sumArray(list):
    result = 0
    for i in range(len(list)):
        result += list[i]
    return result
# inFile = open('input.txt')
inFile = open('rosalind_fibd.txt')
outFile = open('output.txt', 'w')
n, m = map(int, inFile.read().split())
inFile.close
age = [[0] * m for i in range(n)]
age[0][0] = 1
age[1][1] = 1
sum = [0] * n
sum[0] = 1
sum[1] = 1
for i in range(2, n):
    for j in range(m - 1):
        age[i][j + 1] = age[i - 1][j]
    age[i][0] = sum[i - 1] - age[i - 1][0]
    sum[i] = sumArray(age[i])
outFile.write(str(sum[n - 1]))
outFile.close

