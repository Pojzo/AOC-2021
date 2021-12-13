from collections import defaultdict

def is_lower(c):
    if c[0] >= 'a' and c[0] <= 'z':
        return True

    return False

graph = dict()

count = 0
paths = []

def dfs(path, current, graph, visited):
    print(path)
    path.append(current)
    if current == 'end':
        paths.append(path)

    else:
        for x in graph[current]:
            if is_lower(x) and not x == 'end':
                new_visited = dict(visited)
                if not x in new_visited:
                    new_visited[x] = 1
                    dfs(list(path), x, graph, dict(new_visited))
                else:
                    if new_visited[x] == 1:
                        new_visited[x] += 1
                        dfs(list(path), x, graph, new_visited)
            else:
                dfs(list(path), x, graph, dict(visited))
            
    return

graph['start'] = []
with open("input", "r") as file:
    for line in file:
        x = line[:-1].split('-') 
        if 'start' == x[1]:
            x[0], x[1] = x[1], x[0]

        if x[0] in graph:
            graph[x[0]].append(x[1])
        else:
            graph[x[0]] = [x[1]]

        if x[0] == 'start':
            continue
        if x[1] in graph:
            graph[x[1]].append(x[0])
        else:
            graph[x[1]] = [x[0]]


del graph['end']

visited = dict()
dfs([], 'start', graph, dict(visited))

for path in paths:
    print(path)
print(len(paths))

