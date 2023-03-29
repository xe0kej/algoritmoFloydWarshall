"""
Algoritmo de Floyd-Warshall
Jesus Perez - C.I: 27.877.780
"""

import sys

class Graph():
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.graphEdge = []

    def set0toInf(self):
        INF = 99999  
        for i in range(self.V):  
            for j in range(self.V):
                if self.graph[i][j] == 0 and i != j:
                    self.graph[i][j] = INF

    def setInfto0(self):
        INF = 99999  
        for i in range(self.V):  
            for j in range(self.V):
                if self.graph[i][j] > 90000 :
                    self.graph[i][j] = 0

    def addEdges(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != 0:
                    self.graphEdge.append([i, j, self.graph[i][j]])

    def printSolution(self, dist):
        print("Distancia del vertice desde el nodo inicial:")
        print("")
        for node in range(self.V):
            print("Desde el vertice inicial ",node, " para llegar a: ", dist[node])

    def minDistance(self, dist, sptSet):

        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def FloydWarshall(self,src):
        self.set0toInf()
        copyG = self.graph
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if copyG[i][j] > copyG[i][k] + copyG[k][j]:
                        copyG[i][j] = copyG[i][k] + copyG[k][j]
        print("Matriz completa: ")
        print("")
        print(copyG)
        print("")
        dist = copyG[src]
        self.printSolution(dist)

g = Graph(9)
g.graph = [[0, 4, 9, 99999, 99999, 99999, 99999, 99999, 99999],
           [99999, 0, 11, 99999, 9, 99999, 99999, 99999, 99999],
           [99999, 99999, 0, 7, 99999, 1, 99999, 99999, 99999],
           [99999, 99999, 99999, 0, 99999, 6, 99999, 99999, 99999],
           [99999, 99999, 99999, 2, 0, 99999, 99999, 4, 99999],
           [99999, 99999, 99999, 99999, 99999, 0, 99999, 2, 99999],
           [99999, 99999, 99999, 99999, 7, 99999, 0, 99999, 10],
           [99999, 99999, 99999, 99999, 99999, 99999, 15, 0, 11],
           [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 0]]
g.addEdges()

g.FloydWarshall(0)
