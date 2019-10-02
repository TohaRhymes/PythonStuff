def checkio(data):
    i = 0
    while i < len(data):
        single = True
        j = 0
        while j < len(data) and single:
            if data[i] == data[j] and i != j:
                single = False
            j += 1
        if single:
            data.pop(i)
            i -= 1
        i += 1
    return data
