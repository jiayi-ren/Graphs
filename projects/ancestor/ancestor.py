from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1) # bi-directional
        else:
            raise IndexError("nonexistent vertex")

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        g.add_edge(pair[1],pair[0])
    
    # dfs
    # s = deque()
    # s.append([starting_node])
    # max_path_length = 1
    # earl_anc = -1
    # while len(s) > 0:
    #     path = s.pop()
    #     v = path[-1]

    #     if len(path) > max_path_length or (len(path) == max_path_length and v < earl_anc):
    #         max_path_length = len(path)
    #         earl_anc = v
        
    #     for parent in g.vertices[v]:
    #         new_path = list(path)
    #         new_path.append(parent)
    #         s.append(new_path)
    # return earl_anc

    # bfs
    q = deque()
    q.append([starting_node])

    max_path_length = 1
    earl_anc = -1
    while len(q) > 0:
        path = q.popleft()
        v = path[-1]

        if len(path) > max_path_length or (len(path) == max_path_length and v < earl_anc):
            max_path_length = len(path)
            earl_anc = v
        
        for parent in g.vertices[v]:
            new_path = list(path)
            new_path.append(parent)
            q.append(new_path)
    return earl_anc