from collections import defaultdict, deque

def sol(n, edges):
    """
    n = number of vertices (labelled 1..n)
    edges = list of (u, v) pairs
    """
    # Build adjacency list
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Keep track of levels
    levels = {}
    round_num = 1

    # Find initial leaves (degree 1 vertices)
    leaves = deque([v for v in range(1, n+1) if len(graph[v]) == 1])

    count = 0
    while leaves:
        new_leaves = []
        count += 1
        while leaves:
            v = leaves.popleft()
            if v in levels:   # already removed
                continue
            levels[v] = round_num
            # Remove v from its neighbors
            for nei in list(graph[v]):
                graph[nei].remove(v)
            graph[v].clear()

        # After removal, find new leaves
        for i in range(1, n+1):
            if i not in levels and len(graph[i]) == 1:
                new_leaves.append(i)

        leaves = deque(new_leaves)
        round_num += 1

    return count

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(sol(n, edges=edges))