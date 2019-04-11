from __future__ import print_function

f = open('inputFilelab3.txt')
inf = []
a = []
i = 0
line = f.readline()
while line:
    a = line.split()
    x = []
    for j in range(len(a)):
        x.append(a[j])
    inf.append(x)
    line = f.readline()
    i += 1
f.close()
d = True
j = 0
n = len(inf)
while j < n - 1 and d:
    d = False
    for k in range(n-2, j-1, -1):
        if inf[k][0] < inf[k + 1][0] or inf[k][0] == inf[k + 1][0] and inf[k][1] < inf[k + 1][1]:
            inf[k], inf[k+1] = inf[k+1], inf[k]
            d = True
    j += 1
ee = 0
for q in range(len(inf)):
    for k in range(len(inf[q])):
        if k == 1 or k == 2:
            print(inf[q][k], end=' | ')
        else:
            print(inf[q][k], end=' ')
    print(' ->', end=' ')
    ee = (int(inf[q][3]) + int(inf[q][4])+int(inf[q][5]))/3
    if (int(ee)-ee) != 0:
        print('{:10.3f}'.format(ee))
    else:
        print('{:<10.0f}'.format(ee))
