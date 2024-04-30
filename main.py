# Name: Peter Atef Fathi
# Section: 1
# B.N: 18
# ID: 9202395
from collections import deque

def DSR_route_discovery(n, edges, source, destination):
    """DSR route discovery algorithm

    Args:
        n (int): number of vertices
        edges (list): List of tuples representing the edges of the graph (bidirectional)
        source (int): source node
        destination (int): destination node

    Returns:
        tuple: a tuple containing a dictionary of paths and a set of visited nodes
    """
    # initialize the graph as a dictionary where the keys are the vertices and the values are list of neighbors
    graph = {i: [] for i in range(1, n+1)}
    for edge in edges:
        x, y = edge
        graph[x].append(y)
        graph[y].append(x)
    # initialize the visited set and the queue
    visited = set()
    queue = deque([source])
    
    paths = {i: [] for i in range(1, n+1)}
    # add the source node to its path
    paths[source] = [source]
    while queue:
        node = queue.popleft()
        if node == destination:
            continue
        visited.add(node)
        # because the destiantion node doesn't send to any neighbors
        for neighbor in sorted(graph[node]):
            list_queue = [i for i in queue]
            # if neighbor isn't visited
            if neighbor not in visited:
                # create new path
                path = paths[node] + [neighbor]
                # if the path is empty which means that this the first request to this node or the new path is shorter than the old path
                if paths[neighbor] == [] or len(path) < len(paths[neighbor]):
                    # update the path
                    paths[neighbor] = path
                # if the neighbor isn't in the queue
                if neighbor not in list_queue:
                    # add the neighbor to the queue
                    queue.append(neighbor)
    return paths,visited

def main():
    # Input
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    source, destination = map(int, input().split())

    # Run DSR route discovery
    paths,visited = DSR_route_discovery(n, edges, source, destination)
    # print(paths)
    # print(visited)
    # Output
    for i in range(1, n+1):
        if i not in visited:
            print(-1)
        else:
            print(" ".join(map(str,paths[i])))

if __name__ == '__main__':
    main()