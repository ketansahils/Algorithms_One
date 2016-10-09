import os, sys
sys.path.insert(0, os.path.abspath('..'))
from WeekX.LinkedList import LinkedList

class Bag(LinkedList):
	def __init__(self,val):
		LinkedList.__init__(self,val)

	def addBefore(self,a,b):
		pass

	def addAfter(self,a,b):
		pass

	def addFirst(self,val):
		pass

	def addLast(self,val):
		pass

	def add(self,val):
		LinkedList.addLast(self,val)

class Graph(object):
	def __init__(self,V):
		self._V = V
		#self._adj = [[] for _ in range(V)]
		self._adj = [Bag(None) for _ in range(V)]

	def addEdge(self,a,b):
		self._adj[a].add(b)
		self._adj[b].add(a)

	def adjVertices(self,a):
		return self._adj[a].traverse()


class Paths(object):
	def __init__(self,graph,source):
		self._graph = graph
		self._source = graph[source]

	def hasPathTo(self,vertex):
		node = self._source._head
		while node:
			if node._val == vertex:
				return True
			node = node._next
		return False


class DepthFirstPaths(object):
	def __init__(self,graph):
		self._graph = graph
		self._visited = [False] * self._graph._V
		self._edge = [_ for _ in range(self._graph._V)]

	def dfs(self,vertex):
		self._visited[vertex] = True
		for v in self._graph.adjVertices(vertex):
			if not self._visited[v]:
				self.dfs(v)
				self._edge[v] = vertex

	def dfPaths(self,vertex):
		self.dfs(vertex)
		return self._edge


if __name__ == '__main__':
	graph = Graph(13)
	graph.addEdge(0,1)
	graph.addEdge(0,5)
	graph.addEdge(0,2)
	graph.addEdge(0,6)
	graph.addEdge(3,4)
	graph.addEdge(5,3)
	graph.addEdge(5,4)
	graph.addEdge(4,6)
	graph.addEdge(7,8)
	graph.addEdge(10,9)
	graph.addEdge(12,9)
	graph.addEdge(11,9)
	graph.addEdge(11,12)
	print "Adjacency Lists"
	for item in range(13):
		print graph.adjVertices(item)

	dfs = DepthFirstPaths(graph)
	print dfs.dfPaths(0)

# Possible result
# Adjacency Lists
# [1, 5, 2, 6]
# [0]
# [0]
# [4, 5]
# [3, 5, 6]
# [0, 3, 4]
# [0, 4]
# [8]
# [7]
# [10, 12, 11]
# [9]
# [9, 12]
# [9, 11]
# 
# [0, 0, 0, 5, 3, 0, 4, 7, 8, 9, 10, 11, 12]