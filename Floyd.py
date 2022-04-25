from math import inf
from itertools import product

def init_graph_floyd():

    graph = [
        # RED nodes
            [0, 1, 80],
            [1, 0, 80], [1, 2, 420], [1, 7, 310],
            [2, 1, 420], [2, 3, 100], [2, 4, 220], [2, 6, 300],
            [3, 2, 100], [3, 4, 250], [3, 5, 300], [3, 22, 360],
            [4, 3, 250], [4, 2, 220],
            [5, 3, 300], [5, 6, 310], [5, 12, 90], [5, 21, 200],
            [6, 2, 300], [6, 5, 310], [6, 10, 710],
            [7, 1, 310], [7, 8, 550],
            [8, 7, 550], [8, 9, 110], [8, 13, 360], [8, 14, 430],
            [9, 8, 110], [9, 10, 110], [9, 15, 370],
            [10, 6, 710], [10, 9, 110], [10, 11, 120], [10, 16, 360],
            [11, 10, 120], [11, 12, 570], [11, 17, 360], [11, 18, 250],
            [12, 5, 290], [12, 11, 570], [12, 19, 110], [12, 20, 100],

        # GREEN nodes
            [13, 8 , 360],
            [14, 8 , 430],
            [15, 9 , 370],
            [16, 10, 360],
            [17, 11, 360],
            [18, 11, 250],
            [19, 12, 110],
            [20, 12, 100],
            [21, 5 , 200],
            [22, 3 , 360]
    ]
            
    return graph


def floyd_warshall(n, edge, dest):
    rn = range(n)
    dist = [[inf] * n for i in rn]
    unvisited = [[0] * n for i in rn]

    #Zerar as posições
    for i in rn:
        dist[i][i] = 0

    for u, v, w in edge:
        dist[u - 1][v - 1] = w
        unvisited[u - 1][v - 1] = v - 1

    #Criação das tabelas de Warshal
    for k, i, j in product(rn, repeat=3):
        if dist[i][j] > dist[i][k] + dist[k][j]:
            dist[i][j] = dist[i][k] + dist[k][j]
            unvisited[i][j] = unvisited[i][k]

    for i, j in product(rn, repeat=2):
        if j == 22:
            break
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(unvisited[path[-1]][j])

            if dest == j+1:
                menor = dist[i][j]
                small_path = [menor, 0]
                for p in path:
                    small_path.append(p + 1)

    return small_path


# if __name__ == '__main__':
#     graph = init_graph_floyd()
#     brabissimo = floyd_warshall(23, graph, 5)
#     print(brabissimo)