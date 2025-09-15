from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

def breadth_first_search(ginput, start):
    order = []
    parent = {start: None}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in ginput.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)


    return order, parent

if __name__ == "__main__":
    o, p = breadth_first_search(graph, 'B')
    print(o)
    print(p)