import codecs

def do (block):
    lines = block.split(' ')
    global tab
    w=''
    for j in range(tab):
        w = w+"\t"
    l = len(lines)
    for j in range(l):
        if(str(lines[j])=="{"):
            tab+=1
        if(str(lines[j]) == "}" or str(lines[j]) == "},"):
            tab-=1
        a = str(lines[j].replace("{", ""))
        a = a.replace("},", "")
        a = a.replace("}", "")
        if (a == "\"\""):
            a = "\'\'"
        if(a.endswith(",")):
            a = a.rstrip(",")
        if not(a.startswith("\"?")):
            a = a.lstrip("\"")
            a = a.replace("\":", ":")
        if (a.endswith("\"")):
            a = a.replace("\"", "")
        w = w + a
        w = w + " "
    return w


inFile = codecs.open('inputlab4.json', 'r', 'utf-8')
outFile = codecs.open('outputlab4.yaml', 'w', 'utf-8')
write = '---'
boxes = inFile.read().split('\n')
tab = -1
for block in boxes[0:-1]:
    write = write + do(block)+'\n'
write = write.rstrip()
outFile.write(write)
inFile.close
outFile.close
