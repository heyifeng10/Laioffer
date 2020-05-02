import heapq
from collections import defaultdict


def dijkstra(edges, start, goal):
    graph = defaultdict(list)
    for nodeI, nodeJ, dist in edges:
        graph[nodeI].append((nodeJ, dist))
    # q: (distance from start node, target node, path)
    q, visited, mins = [(0, start, None)], set(), {start: 0}
    while q:
        (cost, v1, path) = heapq.heappop(q)
        if v1 not in visited:
            visited.add(v1)
            path = "{} -> {}".format(path, v1)
            if v1 == goal:
                print("The shortest distance from node {} is {}".format(start, cost))
                print("The shortest path is {}".format(path))
                return ""
            for j, l in graph.get(v1):
                if j in visited:
                    continue
                prev = mins.get(j, None)
                next = cost + l
                if prev is None or next < prev:
                    mins[j] = next
                    heapq.heappush(q, (next, j, path))


def enumerate(nodes):
    print("=== Dijkstra ===")
    for item in nodes:
        print("{} -> 5:".format(item))
        print(dijkstra(edges, item, "5"))


if __name__ == "__main__":
    edges = [
        ("1", "2", 2),
        ("1", "3", 8),
        ("2", "3", 5),
        ("3", "2", 6),
        ("2", "4", 3),
        ("3", "5", 0),
        ("4", "3", 1),
        ("4", "5", 7),
        ("4", "6", 6),
        ("5", "4", 4),
        ("6", "5", 2)
    ]
nodes = ("1", "2", "3", "4", "5", "6")
enumerate(nodes)