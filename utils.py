from graph import Graph
import json

def read_graph_from_file(path_to_file:str):
    """ reads graph from a json file and returns its data"""
    ## store the json content into a string
    try :
        file = open(path_to_file)
        data = file.read()
    
        file.close()
        ## and parse it using the json library
        graph_object = json.loads(data)
        return graph_object
    except:
        print("an error occured whilst reading graph at path {}".format(path_to_file))
    

def save_graph_to_file(graph_data:Graph):
    pass




if __name__ == "__main__":
    print("utils.py tests :")
    print("test 1 -- reading a graph from a file")
    print(read_graph_from_file("./saved_graphs/myTestGraph.json"))



    