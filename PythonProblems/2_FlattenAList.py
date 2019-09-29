a = input().replace('[', '').replace(']', '').replace('\'', '').replace(',', ' ').replace('  ', ' ').split(" ")
print([int(i) for i in a])
