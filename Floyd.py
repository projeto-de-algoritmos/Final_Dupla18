from math import inf
from itertools import product

def init_graph_floyd():

    graph = [
        # RED nodes
            [0, 1, 0],
            [1, 0, 0], [1, 2, 5], [1, 7, 4],
            [2, 1, 5], [2, 3, 1], [2, 4, 3], [2, 6, 2],
            [3, 2, 1], [3, 4, 2], [3, 5, 2], [3, 22, 3],
            [4, 3, 2], [4, 2, 3],
            [5, 3, 2], [5, 6, 4], [5, 12, 3], [5, 21, 1],
            [6, 2, 2], [6, 5, 4], [6, 10, 7],
            [7, 1, 4], [7, 6, 4],[7, 8, 10],
            [8, 7, 10], [8, 9, 1], [8, 13, 2], [8, 14, 6],
            [9, 8, 1], [9, 10, 2], [9, 15, 5],
            [10, 6, 7], [10, 9, 2], [10, 11, 2], [10, 16, 7],
            [11, 10, 2], [11, 12, 9], [11, 17, 8], [11, 18, 2],
            [12, 5, 3], [12, 11, 9], [12, 19, 1], [12, 20, 1],

        # GREEN nodes
            [13, 8 , 2],
            [14, 8 , 6],
            [15, 9 , 5],
            [16, 10, 7],
            [17, 11, 8],
            [18, 11, 2],
            [19, 12, 1],
            [20, 12, 1],
            [21, 5 , 1],
            [22, 3 , 3]
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