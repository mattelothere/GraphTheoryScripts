class Vertex():
    def __init__(self, vertex_label):
        self.label = vertex_label
    
    def get_in_degree():
        pass

    def get_out_degree():
        pass

class Link():
    id = 1
    def __init__(self, weight=None):
        self.weight = weight

class Arc(Link):
    """define weight, and id. Weight can be ommitted"""
    def __init__(self, weight=None):
        super().__init__(weight)
        
        self.id = Link.id + 1
        Link.id += 1

    def __repr__(self):
        return "Arc id of weight {}".format(self.weight)
        

class Graph():
    def __init__(self):
        self.vertices = []
        self.links = []
        self.adjacency_matrix = []
    
    def __init__(self, graph_dict):
        print("creating graph from dictionnary `{}`".format(graph_dict))
        self.vertices = graph_dict["vertices"]
        self.links = [[] * len(graph_dict["links"])]
        self.adjacency_matrix = []
        
        # initialize the adj_mat with 0 everywhere
        for i in range(len(self.vertices)):
            self.adjacency_matrix.append([0]*len(self.vertices))
        for link in graph_dict["links"]:
            self.adjacency_matrix[self.vertices.index(link[0])][self.vertices.index(link[1])] = 1

    def get_order(self):
        return len(self.vertices)

    def add_edge(self, vertex1:Vertex, vertex2:Vertex, edge_weight=None|int):
        self.links.append((vertex1, vertex2, edge_weight))

    def add_vertex(self, vertex_label: str):
        self.vertices.append(vertex_label)

    def get_adjacency_matrix(self):
        """Returns the adjacency matrix if available"""
        if self.adjacency_matrix != []:
            return self.adjacency_matrix

    def __repr__(self):
        res = "  "
        # Header row label printing
        for v in self.vertices:
            res += v + "  "
        res += "\n"

        # Cycling through the adjacency matrix list to print weights
        for i in range(len(self.adjacency_matrix)):
            res += self.vertices[i]
            res += str(self.adjacency_matrix[i]) + "\n"
        return res


if __name__ == "__main__":
    print("--------- Test 1 --------")
    print("Link id before creation of an Arc : {}".format(Link.id))
    A = Arc(10)
    print("Arc A's id : {}".format(A.id))
    print("Link id after creation of an Arc : {}".format(Link.id))

    print("--------- Test 2 --------")    ## write documentation for __repr__() 
    B = Arc()
    print(B)

    print("test 3 - displaying a graph")
    from utils import read_graph_from_file
    C = read_graph_from_file("./saved_graphs/myTestGraph.json")
    print(C)


    print("\nTEST 4 - adjacency matrices\n")
    C = Graph(C)
    print(C)
    print("getting adj mat :")
    print(C.get_adjacency_matrix())



    