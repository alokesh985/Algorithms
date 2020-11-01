#Using Adjacency Matrix Representation in Python3

import math

class Graph(): 

	def __init__(self, vertices): 
		self.vertices = vertices 
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 

	def show(self, distance_list): 
		print("The minimum distances/weights from the entered source vertex are as follows : \n")

		print("Vertex \t Weight")
		for vertex in range(self.vertices): 
			print(vertex, "\t ", distance_list[vertex]) 

	#Find the vertex with minimum distance value, from the set of vertices that are 
	# not yet included in shortest path tree list, 'SPTree' 
	def minDistance(self, distance_list, SPTree): 
		global minimum_index
		# Initially, making it infinite 
		minimum = math.inf

		# Search not nearest vertex not in the 
		# shortest path tree list, SPTree 
		for vertex in range(self.vertices): 
			if distance_list[vertex] < minimum and SPTree[vertex] == False: 
				minimum = distance_list[vertex] 
				minimum_index = vertex
		
		return minimum_index 

	 
	def Dijkstra(self, source): 

		distance_list = [math.inf] * self.vertices 
		distance_list[source] = 0
		SPTree = [False] * self.vertices 

		for vertex in range(self.vertices): 

			# Pick the minimum distance vertex from 
			# the set of vertices not yet finalized.
			 
			u = self.minDistance(distance_list, SPTree) 

			# Put the minimum distance vertex in the 
			# shotest path tree 
			SPTree[u] = True

			# Update distance list values of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and 
			# the vertex in not in the shotest path tree list 
			for v in range(self.vertices): 
				if self.graph[u][v] > 0 and SPTree[v] == False and distance_list[v] > distance_list[u] + self.graph[u][v]: 
						distance_list[v] = distance_list[u] + self.graph[u][v] 

		self.show(distance_list) 



def createGraph(r):
	graph = [[0 for columns in range(r)] for rows in range(r)]

	while(True):
		to,fro,weight = input("Enter Source, Destination and Weight : ").split()
		graph[int(to)][int(fro)] = int(weight)
		choice = input("Fo You Want To Add Another Edge (Y/N) : ")
		if(choice == 'Y'):
			continue
		else:
			break

	return graph

def main():
	print("Number the vertices starting from 0 to (n-1), where n is the number of vertices in the graph. If there is an edge from first to second node, the edge should be 0 --> 1 \nAlso note that this a DIRECTED, WEIGHTED graph \n")

	vertices = int(input("Enter Number Of Vertices in the graph : "))
	G = Graph(vertices)

	temp = createGraph(vertices)

	G.graph = temp

	source = int(input("Source Vertex from which Dijkstra is to begin : "))

	G.Dijkstra(source)

if __name__ == "__main__":
	main()
