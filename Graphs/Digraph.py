import sys, os
sys.path.insert(0, os.path.abspath('..'))
from WeekX.LinkedList import LinkedList

class Digraph(object):
	def __init__(self,V):
		self._V = V
		self._adj = [LinkedList(None) for _ in range(self._V)]

	def addEdge(self,v,w):
		self._adj[v].addLast(w)

	def adjVertices(self,v):
		return self._adj[v].traverse()

class DepthFirstSearch(object):
	def __init__(self,digraph,source):
		self._digraph = digraph
		self._marked = [False] * self._digraph._V
		self._edgeTo = [None] * self._digraph._V
		self._source = source
		self.dfs()

	def dfs(self):
		self._marked[self._source] = True
		self._dfs(self._source)

	def _dfs(self,vertex):
		for item in self._digraph.adjVertices(vertex):
			if not self._marked[item]:
				self._marked[item] = True
				self._edgeTo[item] = vertex
				self._dfs(item)

	def pathTo(self,vertex):
		if not self._marked[vertex]:
			return "Not Connected"

		ll = LinkedList(vertex)
		while vertex != self._source:
			vertex = self._edgeTo[vertex]
			ll.addFirst(vertex)
		return ll.traverse()

if __name__ == '__main__':
	dg = Digraph(13)
	dg.addEdge(0,5)
	dg.addEdge(0,1)
	dg.addEdge(2,0)
	dg.addEdge(6,0)
	dg.addEdge(3,5)
	dg.addEdge(5,4)
	dg.addEdge(4,2)
	dg.addEdge(4,3)
	dg.addEdge(3,2)
	dg.addEdge(2,3)
	dg.addEdge(6,4)
	dg.addEdge(11,4)
	dg.addEdge(6,8)
	dg.addEdge(8,6)
	dg.addEdge(7,6)
	dg.addEdge(6,9)
	dg.addEdge(9,11)
	dg.addEdge(11,12)
	dg.addEdge(12,9)
	dg.addEdge(10,12)
	dg.addEdge(9,10)
	dg.addEdge(7,9)

	dfs = DepthFirstSearch(dg,0)
	for item in range(13):
		print "From Node {:<2} to Node {:<2}: ".format(0,item),
		print dfs.pathTo(item)


# From Node 0  to Node 0 :  [0]
# From Node 0  to Node 1 :  [0, 1]
# From Node 0  to Node 2 :  [0, 5, 4, 2]
# From Node 0  to Node 3 :  [0, 5, 4, 2, 3]
# From Node 0  to Node 4 :  [0, 5, 4]
# From Node 0  to Node 5 :  [0, 5]
# From Node 0  to Node 6 :  Not Connected
# From Node 0  to Node 7 :  Not Connected
# From Node 0  to Node 8 :  Not Connected
# From Node 0  to Node 9 :  Not Connected
# From Node 0  to Node 10:  Not Connected
# From Node 0  to Node 11:  Not Connected
# From Node 0  to Node 12:  Not Connected
