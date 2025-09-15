from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def dfs(node, visited, grph):
    visited.add(node)

    for neighbor in grph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, grph)

if __name__ == "__name__":
    visited_nodes = set()
    dfs('A', visited_nodes, graph)