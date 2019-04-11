# inFile = open('input.txt')
inFile = open('rosalind_subs.txt')
outFile = open('output.txt', 'w')
s = inFile.read().split('\n')
inFile.close
n = len(s[0])
nsub = len(s[1])
sAns=''
for i in range(n - nsub):
    if (s[0][i:i+nsub]==s[1]):
        sAns+=str(i+1)+' '
outFile.write(str(sAns))
outFile.close()
