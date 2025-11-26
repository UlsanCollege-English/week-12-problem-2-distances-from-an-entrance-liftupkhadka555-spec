from collections import deque

def bfs_distances(graph, start):
    if start not in graph:
        return {}
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        for neigh in graph.get(node, []):
            if neigh not in dist:
                dist[neigh] = dist[node] + 1
                q.append(neigh)
    return dist

if __name__ == "__main__":
    sample_graph = {
        "Gate": ["Stage1", "Stage2"],
        "Stage1": ["Gate", "Stage3"],
        "Stage2": ["Gate"],
        "Stage3": ["Stage1"],
    }
    d = bfs_distances(sample_graph, "Gate")
    print(d)
