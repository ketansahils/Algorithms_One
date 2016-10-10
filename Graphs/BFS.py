import os, sys
sys.path.insert(0, os.path.abspath('..'))
from GraphAlt import Graph
from WeekX.Queue import Queue

class BreadthFirstSearch(object):
	def __init__(self,graph,source):
		self._source = source
		self._graph = graph
		self._edgeTo = [None]*self._graph._V
		self._distTo = [None]*self._graph._V
		self._marked = [False]*self._graph._V
		self.bfs()

	def bfs(self):
		q = Queue(self._source)
		self._marked[self._source] = True
		self._distTo[self._source] = 0
		while not q.isEmpty():
			node = q.dequeue()._val
			for item in self._graph.adjVertices(node):
				if not self._marked[item]:
					self._marked[item] = True
					self._edgeTo[item] = node
					self._distTo[item] = 1 + self._distTo[node]
					q.enqueue(item)

	def bfsPath(self,vertex):
		if not self._marked[vertex]:
			return "Not Connected"
		q = Queue(vertex)
		node = vertex
		while node != self._source:
			node = self._edgeTo[node]
			q.enqueue(node)
		return q.show()

	def bfsDist(self,vertex):
		return self._distTo[vertex]

	def showPath(self):
		print range(self._graph._V)
		print self._edgeTo
		print self._distTo


if __name__ == '__main__':
	graph = Graph(8)
	graph.addEdge(0,1)
	#graph.addEdge(0,5)
	graph.addEdge(0,2)
	graph.addEdge(5,2)
	graph.addEdge(1,3)
	graph.addEdge(3,4)
	graph.addEdge(5,4)
	graph.addEdge(7,6)

	bfs = BreadthFirstSearch(graph,0)
	print "Edges:", bfs._edgeTo
	print "Distances:", bfs._distTo
	print "Visited:", bfs._marked
	for item in range(bfs._graph._V):
		print "Path from %s to source %s:" % (item, bfs._source),
		print bfs.bfsPath(item),
		print bfs.bfsDist(item)

# Edges: [None, 0, 0, 1, 3, 2, None, None]
# Distances: [0, 1, 1, 2, 3, 2, None, None]
# Visited: [True, True, True, True, True, True, False, False]
# Path from 0 to source 0: [0] 0
# Path from 1 to source 0: [1, 0] 1
# Path from 2 to source 0: [2, 0] 1
# Path from 3 to source 0: [3, 1, 0] 2
# Path from 4 to source 0: [4, 3, 1, 0] 3
# Path from 5 to source 0: [5, 2, 0] 2
# Path from 6 to source 0: Not Connected None
# Path from 7 to source 0: Not Connected None