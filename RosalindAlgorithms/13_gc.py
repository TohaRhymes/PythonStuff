def gc(str):
    n = 0
    for char in str:
        if (char == 'C' or char == 'G'):
            n += 1
    return n


# inFile = open('input.txt')
inFile = open('rosalind_gc.txt')
outFile = open('output.txt', 'w')
s = inFile.read()
s = s[1:len(s)]
sArray = s.split('>')
maxGC = -1
imaxGC = -1
inFile.close()
for i in range(0, len(sArray)):
    data = sArray[i].split('\n')
    gcNumber = 0
    totNumber = 0
    for j in range(1, len(data)):
        gcNumber += gc(data[j])
        totNumber += len(data[j])
    thisGC =gcNumber / totNumber * 100
    if (thisGC > maxGC):
        maxGC=thisGC
        imaxGC=i
outFile.write(sArray[imaxGC].split('\n')[0]+'\n'+str(maxGC))
outFile.close()
