from collections import deque

# Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 🔹 BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# 🔹 DFS Function (Recursive)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        print("\nDFS:", end=" ")

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# 🔹 Run both
bfs(graph, 'A')
dfs(graph, 'A')    