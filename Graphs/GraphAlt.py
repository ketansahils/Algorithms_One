import os, sys
sys.path.insert(0, os.path.abspath('..'))
from WeekX.LinkedList import LinkedList
from WeekX.Stack import Stack

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


class DepthFirstSearch(object):
	def __init__(self,graph,source):
		self._graph = graph
		self._visited = [False] * self._graph._V
		self._edge = [_ for _ in range(self._graph._V)]
		self._source = source
		#self._marked = False

	def _dfs(self,vertex):
		self._visited[vertex] = True
		for v in self._graph.adjVertices(vertex):
			if not self._visited[v]:
				self._dfs(v)
				self._edge[v] = vertex

	def dfPaths(self):
		self._dfs(self._source)
		#self._marked = True
		return self._edge

	def hasPathTo(self,vertex):
		#if not self._marked:
		#	print "Run DFS first. Tip: Instance Method dfPaths()."
		#	return
		return self._visited[vertex]

	def pathTo(self,vertex):
		if not self.hasPathTo(vertex):
			return
		node = vertex
		path = Stack(vertex)
		while node != self._source:
			path.push(self._edge[node])
			node = self._edge[node]
		return path

	def ppath(self,vertex):
		st = self.pathTo(vertex)
		if st is not None:
			st.show()
			return
		print "No Path"

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
	print "*"*40
	print "{:^40}".format("Adjacency Lists")
	print "*"*40
	for item in range(13):
		print graph.adjVertices(item)
	print
	print "*"*40
	print "{:^40}".format("DFS Paths")
	print "*"*40
	dfs = DepthFirstSearch(graph,0)
	print dfs.dfPaths()
	print
	print "*"*40
	print "Path from source %s to each node." % (dfs._source)
	print "*"*40
	for item in range(13):
		print "Path from 0 to",item,": ",
		dfs.ppath(item)
	print

# ****************************************
#             Adjacency Lists             
# ****************************************
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
# ****************************************
#                DFS Paths                
# ****************************************
# [0, 0, 0, 5, 3, 0, 4, 7, 8, 9, 10, 11, 12]
# 
# ****************************************
# Path from source 0 to each node.
# ****************************************
# Path from 0 to 0 :  0
# Path from 0 to 1 :  0 1
# Path from 0 to 2 :  0 2
# Path from 0 to 3 :  0 5 3
# Path from 0 to 4 :  0 5 3 4
# Path from 0 to 5 :  0 5
# Path from 0 to 6 :  0 5 3 4 6
# Path from 0 to 7 :  No Path
# Path from 0 to 8 :  No Path
# Path from 0 to 9 :  No Path
# Path from 0 to 10 :  No Path
# Path from 0 to 11 :  No Path
# Path from 0 to 12 :  No Path 