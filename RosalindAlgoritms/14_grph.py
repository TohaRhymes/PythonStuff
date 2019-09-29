# inFile = open('input.txt')
inFile = open('rosalind_grph.txt')
outFile = open('output.txt', 'w')
s = inFile.read()
s = s[1:len(s)]
sArray = s.split('>')
inFile.close()
proArray = [[''] * 2 for i in range(len(sArray))]
for i in range(0, len(sArray)):
    data = sArray[i].split('\n')
    proArray[i][0] = data[0]
    for j in range(1, len(data)):
        proArray[i][1]+=data[j]
for i in range(0, len(sArray)):
    for j in range(0, len(sArray)):
        if(i!=j and proArray[j][1][0:3]==proArray[i][1][len(proArray[i][1])-3:len(proArray[i][1])]):
            outFile.write(proArray[i][0]+' '+proArray[j][0]+"\n")
outFile.close()
