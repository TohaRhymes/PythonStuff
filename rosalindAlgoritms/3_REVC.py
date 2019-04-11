def reverse(s):
    return s[::-1]

inFile = open('rosalind_revc.txt')
outFile = open('output.txt', 'w')
s=str(inFile.read())
inFile.close
s2=''
for char in s:
    if (char == 'A'):
        s2+='T'
    if (char == 'C'):
        s2 += 'G'
    if (char == 'G'):
        s2 += 'C'
    if (char == 'T'):
        s2 += 'A'
s2=reverse(s2)
outFile.write(s2)
outFile.close