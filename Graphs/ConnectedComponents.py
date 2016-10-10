import os, sys
sys.path.insert(0, os.path.abspath('..'))
from GraphAlt import Graph
from WeekX.Queue import Queue

class ConnectedComponents(object):
	def __init__(self,graph):
		self._graph = graph
		self._marked = [False] * self._graph._V
		self._id = [None] * self._graph._V

	def dfs(self,parent):
		self._id[parent] = parent
		self._marked[parent] = True
		self._dfs(parent,parent)

	def _dfs(self,parent,vertex):
		for item in self._graph.adjVertices(vertex):
			if not self._marked[item]:
				self._marked[item] = True
				self._id[item] = parent
				self._dfs(parent,item)

	def cc(self):
		count = 0
		for item in range(self._graph._V):
			if not self._marked[item]:
				self.dfs(item)
				count += 1
		return count

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
	
	cc = ConnectedComponents(graph)
	print cc.cc()

# 3