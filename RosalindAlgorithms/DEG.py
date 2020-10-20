def add_degree(degrees, vertex):
    degrees += [0] * (vertex - len(degrees))
    degrees[vertex - 1] += 1
    return degrees


with open('input.txt', 'r') as input_f:
    edges = input_f.readlines()

degrees = []
for edge in edges[1:]:
    a, b = map(int, edge.split())
    degrees = add_degree(degrees, a)
    degrees = add_degree(degrees, b)

with open('output.txt', 'w') as output_f:
    output_f.write(' '.join(map(str, degrees)))
