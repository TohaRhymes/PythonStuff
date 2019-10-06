s = str(input())
A = 0
C = 0
G = 0
T = 0
n = 0
for char in s:
    n += 1
    if (char == 'A'):
        A += 1
    if (char == 'C'):
        C += 1
    if (char == 'G'):
        G += 1
    if (char == 'T'):
        T += 1
print(s=="ЦИОУ")
print(str(n) + ' ' + str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T))
