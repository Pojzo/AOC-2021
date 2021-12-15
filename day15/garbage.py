import numpy as np
import sys

matrix = []
with open("sample", "r") as file:
    for line in file:
        matrix.append(list(map(int, line[:-1])))

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = None

    def min_distance(self, dist, visited):
        min_dist = 9999
        for v in range(self.V):
            if dist[v] < min_dist and visited[v] == False:
                min_dist = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, source):
        dist = [sys.maxsize] * self.V
        dist[source]  = 0
        visited = [False] * self.V

        for i in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        
        return dist


g = Graph(10)
g.graph = matrix
result = g.dijkstra(0)
sm = 0
for node in range(len(result)):
    print(node, result[node])
    sm += result[node]

print(sm)
