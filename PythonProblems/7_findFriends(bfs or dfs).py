from collections import defaultdict
from typing import Set


def dfs(graph, root, visited: Set[int]):
    visited.add(root)
    for vertex in graph[root]:
        if vertex not in visited:
            dfs(graph, vertex, visited)
    return visited


def check_connection(friends_pairs, a, b):
    graph = defaultdict(list)
    for friend in friends_pairs:
        vertex_a, vertex_b = friend.split("-")
        # if vertex_a not in graph:
        #     graph[vertex_a] = []
        # if vertex_b not in graph:
        #     graph[vertex_b] = []
        graph[vertex_a].append(vertex_b)
        graph[vertex_b].append(vertex_a)
    print(graph)
    visited = dfs(graph, a, set())
    if a in visited and b in visited:
        return True
    return False


if __name__ == '__main__':
    print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True)
    print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False)
