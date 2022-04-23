from collections import defaultdict 

def init_graph():

    graph = {
        # RED nodes
            '0': {'1' : 80},
            '1': {'0' : 80, '2' : 420, '7' : 310},
            '2': {'1' : 420, '3' : 100, '4': 220, '6':300},
            '3': {'2' : 100, '4' : 250, '5': 300, '22': 360},
            '4': {'3' : 250, '2' : 220},
            '5': {'3' : 300, '6' : 310, '12' : 90, '21' : 200},
            '6': {'2' : 300, '5' : 310, '10' : 710},
            '7': {'1' : 310, '8' : 550},
            '8': {'7' : 550, '9' : 110, '13' : 360, '14' : 430},
            '9': {'8' : 110, '10' : 110, '15' : 370},
            '10': {'6': 710, '9' : 110, '11' : 120, '16' : 360},
            '11': {'10' : 120, '12' : 570, '17' : 360, '18' : 250},
            '12': {'5' : 290, '11' : 570, '19' : 110, '20' : 100},

        # GREEN nodes
            '13': {'8' : 360},
            '14': {'8' : 430},
            '15': {'9' : 370},
            '16': {'10': 360},
            '17': {'11': 360},
            '18': {'11': 250},
            '19': {'12': 110},
            '20': {'12': 100},
            '21': {'5' : 200},
            '22': {'3' : 360}
    }
            
    return graph

def dijkstra(graph, search):

    atual_node = {}; path = {}; controller = {}
    unvisiteds = []
    atual_node['0'] = 0
    atual = '0'

    
    for nodes in graph:
        unvisiteds.append(nodes)    
        path[nodes] = 999999 
    
    path[atual] = [0,'0']

    unvisiteds.remove(atual)
    #print(f'{atual} visitado')

    while unvisiteds:
        for previous, distance in graph[atual].items():
             #print(atual_node)
             peso = distance + atual_node[atual]
             #print(f'Peso aresta {atual} = {peso}')

             if path[previous] == 999999 or path[previous][0] > peso:
                 path[previous] = [peso, atual]
                 controller[previous] = peso
       
        min_node = min(controller.items(), key=lambda x: x[1])
        #print(f'Menor nó vizinho: {min_node[1]}')

        atual=min_node[0]; atual_node[atual] = min_node[1]
        
        unvisiteds.remove(atual)
        #print(f'{atual} visitado')
        del controller[atual]

    #print('Node   Menor_distancia\n----------------')
    for nodes in path:
        #print(f' {nodes}  ->   {path[nodes][0]}')
        if (nodes == search):
            return_distance = path[nodes][0]

    print(f'Distância: {return_distance}')

    small_path = [str(return_distance), search]
    x = search

    for names in path:
        if x == '0': break

        x = path[x][1]
        small_path.append(x)
    
    print(small_path[::-1])

    return small_path[::-1]


# if __name__ == "__main__":
	
#     graph = init_graph()
#     brabissimo = dijkstra(graph, '18')

