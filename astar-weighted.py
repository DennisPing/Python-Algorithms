import heapq
from scipy.spatial.distance import cityblock

class PriorityQueue:
    """ Borrowed from UC Berkeley Pacman project """
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_,_,item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self.heap):
            i_vertex = i[0]

            item_vertex = item[0]

            if i_vertex == item_vertex:
                if p >= priority: # FLIP THIS EQUALITY IF YOUR SEARCH IS GOING BACKWARDS.
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

class Vertex:
    def __init__(self, letter, row, col):
        self.letter = letter
        self.coord = (row, col)
    
    # The __str__() method built into the dict class uses the __repr__() method of the dict items.
    # https://stackoverflow.com/questions/35459473/print-dict-with-custom-class-as-values-wont-call-their-string-method
    def __repr__(self):
        return self.letter

class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices_no = 0
    
    def getGraph(self):
        return self.graph

    # Add a vertex to the dictionary
    def add_vertex(self, v):
        if v in self.graph:
            print("Vertex ", v, " already exists.")
        else:
            self.vertices_no = self.vertices_no + 1
            self.graph[v] = []

    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e):
        # Check if vertex v1 is a valid vertex
        if v1 not in self.graph:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self.graph:
            print("Vertex ", v2, " does not exist.")
        else:
            vector = [v2, e]
            if vector not in self.graph[v1]:
                self.graph[v1].append(vector)

            reflection = [v1, e]
            if reflection not in self.graph[v2]:
                self.graph[v2].append(reflection)

    # Print the graph in readable form
    def print_graph(self):
        for vertex in self.getGraph().items():
            print(vertex)

    # Print the build order of the graph
    def print_graph_build(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

class Algorithm:
    def __init__(self):
        self.visited = []
        self.openSet = PriorityQueue()

    def manhattanDist(self, vertex, goal):
        coord1 = vertex.coord
        coord2 = goal.coord
        dist = cityblock(coord1, coord2)
        return dist * 10 # Weight is factor of 10

    def astar(self, graph, vertex, goal):
        self.visited = [vertex]
        parentMap = {vertex: None}
        actualCost = 0

        data = (vertex, actualCost)
        
        self.openSet.push(data, 0)
        while not self.openSet.isEmpty():
            vertex, actualCost = self.openSet.pop()

            for neighbor in graph.getGraph()[vertex]:
                # Remember that all neighbors are composed of [vertex, weight]
                if neighbor[0] == goal:
                    parentMap[neighbor[0]] = vertex
                    return self.rebuild_path(goal, parentMap)
                
                if neighbor[0] not in self.visited:
                    parentMap[neighbor[0]] = vertex
                    self.visited.append(neighbor[0])

                    neighborCost = neighbor[1]
                    actualCost += neighborCost

                    fCost = actualCost + self.manhattanDist(neighbor[0], goal)
                    newData = (neighbor[0], actualCost)
                    self.openSet.update(newData, fCost)
                    #print(f"Enqueue: {neighbor[0]}, previous: {vertex}")
    
    # Rebuild the path going backwards from goal node to start node.
    def rebuild_path(self, current, parentMap, path=[]):
        if current is None: # Reached the start node
            return path
        else:
            return self.rebuild_path(parentMap[current], parentMap, [current] + path)
    
    def get_visited(self):
        return self.visited

    def get_openSet(self):
        openList = []
        while not self.openSet.isEmpty():
            vertex_and_cost = self.openSet.pop()
            openList.append(vertex_and_cost)
        return openList


def main():
    graph = Graph()

    A = Vertex('A', 0, 3)
    B = Vertex('B', 0, 4)
    C = Vertex('C', 0, 6)
    D = Vertex('D', 1, 1)
    E = Vertex('E', 1, 8)
    F = Vertex('F', 2, 0)
    G = Vertex('G', 6, 8)
    H = Vertex('H', 2, 4)
    I = Vertex('I', 3, 1)
    J = Vertex('J', 3, 3)
    K = Vertex('K', 2, 6)
    L = Vertex('L', 4, 0)
    M = Vertex('M', 4, 3)
    N = Vertex('N', 4, 6)
    O = Vertex('O', 5, 1)
    P = Vertex('P', 5, 4)
    Q = Vertex('Q', 5, 8)
    R = Vertex('R', 6, 2)
    S = Vertex('S', 0, 0)
    T = Vertex('T', 6, 8)

    graph.add_vertex(A)
    graph.add_vertex(B)
    graph.add_vertex(C)
    graph.add_vertex(D)
    graph.add_vertex(E)
    graph.add_vertex(F)
    graph.add_vertex(G)
    graph.add_vertex(H)
    graph.add_vertex(I)
    graph.add_vertex(J)
    graph.add_vertex(K)
    graph.add_vertex(L)
    graph.add_vertex(M)
    graph.add_vertex(N)
    graph.add_vertex(O)
    graph.add_vertex(P)
    graph.add_vertex(Q)
    graph.add_vertex(R)
    graph.add_vertex(S)
    graph.add_vertex(T)

    graph.add_edge(A, D, 32)
    graph.add_edge(A, B, 11)
    graph.add_edge(A, H, 36)

    graph.add_edge(B, C, 24)
    graph.add_edge(B, K, 42)

    graph.add_edge(C, E, 40)

    graph.add_edge(D, F, 24)
    graph.add_edge(D, S, 25)
    graph.add_edge(D, I, 26)

    graph.add_edge(E, K, 32)

    graph.add_edge(F, L, 27)

    graph.add_edge(G, T, 32)
    graph.add_edge(G, N, 42)

    graph.add_edge(H, J, 22)
    graph.add_edge(H, K, 28)
    graph.add_edge(H, N, 44)

    graph.add_edge(I, L, 21)
    graph.add_edge(I, M, 32)

    graph.add_edge(J, M, 20)

    graph.add_edge(K, N, 27)
    graph.add_edge(K, Q, 62)

    graph.add_edge(L, O, 26)

    graph.add_edge(M, P, 23)

    graph.add_edge(N, Q, 32)

    graph.add_edge(O, R, 27)

    graph.add_edge(R, T, 52)

    #graph.print_graph_build()
    #graph.print_graph()

    algo = Algorithm()
    path = algo.astar(graph, S, G)
    print(f"Shortest path: {path}")

    print(f"Visited: {algo.get_visited()}")
    print(f"OpenSet: {algo.get_openSet()}")

if __name__ == "__main__":
    main()