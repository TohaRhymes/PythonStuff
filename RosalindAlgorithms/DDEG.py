from collections import defaultdict


def add_degree(degrees, vertex):
    degrees += [0] * (vertex - len(degrees))
    degrees[vertex - 1] += 1
    return degrees


with open('input.txt', 'r') as input_f:
    edges = input_f.readlines()

degrees = []
neighbours = defaultdict(list)
for edge in edges[1:]:
    a, b = map(int, edge.split())
    degrees = add_degree(degrees, a)
    degrees = add_degree(degrees, b)
    neighbours[a].append(b)
    neighbours[b].append(a)

vertexes = int(edges[0].split()[0])

for i in range(vertexes):
    if i not in neighbours:
        neighbours[i] = []
degrees += [0] * (vertexes - len(degrees))

double_degrees = [0] * vertexes

for vertex in range(len(double_degrees)):
    for neighbour in neighbours[vertex + 1]:
        double_degrees[vertex] += degrees[neighbour - 1]

with open('output.txt', 'w') as output_f:
    output_f.write(' '.join(map(str, double_degrees)))
