def get(namesp, var):
    if var in data[namesp]:
        return namesp
    elif namesp == 'global':
        return 'None'
    else:
        return get(parents[namesp], var)


n = int(input())
data = {'global': []}
parents = {}
for i in range(n):
    cmd, namespace, arg = input().split()
    if cmd == 'create':
        namespace, arg = arg, namespace
        parents.update({arg: namespace})
        localData = data.pop(namespace)
        localData.append([arg])
        data.update({namespace: localData})
        data.update({arg: []})
    elif cmd == 'add':
        localData = data.pop(namespace)
        localData.append(arg)
        data.update({namespace: localData})
    elif cmd == 'get':
        print(get(namespace, arg))
