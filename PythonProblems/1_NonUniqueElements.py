a = input().replace('[', '').replace(']', '').replace('\'', '').replace(',', ' ').replace('  ', ' ').split(" ")
a = [int(i) for i in a]
i = 0
while i < len(a):
    single = True
    j = 0
    while j < len(a) and single:
        if a[i] == a[j] and i != j:
            single = False
        j += 1
    if single:
        a.pop(i)
        i -= 1
    i += 1
print(a)
