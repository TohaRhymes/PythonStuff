def dH(s1, s2):
    count = 0;
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            count += 1
    return count

inFile = open('rosalind_hamm.txt')
outFile = open('output.txt', 'w')
s=inFile.read().split('\n')
inFile.close
outFile.write(str(dH(s[0], s[1])))
outFile.close