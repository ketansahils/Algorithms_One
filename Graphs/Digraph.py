import sys, os
sys.path.insert(0, os.path.abspath('..'))
from WeekX.LinkedList import LinkedList
from WeekX.Queue import Queue
from WeekX.Stack import Stack

class Digraph(object):
	def __init__(self,V):
		self._V = V
		self._adj = [LinkedList(None) for _ in range(self._V)]

	def addEdge(self,v,w):
		self._adj[v].addLast(w)

	def adjVertices(self,v):
		return self._adj[v].traverse()

class BreadthFirstSearch(object):
	def __init__(self,digraph,source):
		self._digraph = digraph
		self._marked = [False] * self._digraph._V
		self._edgeTo = [None] * self._digraph._V
		self._distTo = [None] * self._digraph._V
		self._source = source
		self.bfs()

	def bfs(self):
		q = Queue(self._source)
		self._distTo[self._source] = 0
		self._marked[self._source] = True
		while not q.isEmpty():
			node = q.dequeue()._val
			for item in self._digraph.adjVertices(node):
				if not self._marked[item]:
					self._marked[item] = True
					self._edgeTo[item] = node
					self._distTo[item] = 1 + self._distTo[node]
					q.enqueue(item)

	def bfsPath(self,vertex):
		if not self._marked[vertex]:
			return "Not Connected"
		s = Stack(vertex)
		node = vertex
		while node != self._source:
			node = self._edgeTo[node]
			s.push(node)
		return s.show()

	def bfsDist(self,vertex):
		return self._distTo[vertex]

	def showPath(self):
		print range(self._digraph._V)
		print self._edgeTo
		print self._distTo

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
	print "*" * 40
	print "{:^40}".format("Depth First Search")
	print "*" * 40
	for item in range(13):
		print "From Node {:<2} to Node {:<2}: ".format(0,item),
		print dfs.pathTo(item)

	print "*" * 40
	print "{:^40}".format("Breadth First Search")
	print "*" * 40
	bfs = BreadthFirstSearch(dg,0)
	for item in range(13):
		print "From Node {:<2} to Node {:<2}: ".format(0,item),
		print bfs.bfsPath(item),
		print bfs.bfsDist(item)

	print
	bfs = BreadthFirstSearch(dg,7)
	for item in [4,0]:
		print "Shortest path from {:<2} to {:<2}: ".format(7,item),
		print bfs.bfsPath(item),
		print bfs.bfsDist(item)

	bfs = BreadthFirstSearch(dg,10)
	for item in [12,9]:
		print "Shortest path from {:<2} to {:<2}: ".format(10,item),
		print bfs.bfsPath(item),
		print bfs.bfsDist(item)


# ****************************************
#            Depth First Search           
# ****************************************
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
# ****************************************
#           Breadth First Search          
# ****************************************
# From Node 0  to Node 0 :  [0] 0
# From Node 0  to Node 1 :  [0, 1] 1
# From Node 0  to Node 2 :  [0, 5, 4, 2] 3
# From Node 0  to Node 3 :  [0, 5, 4, 3] 3
# From Node 0  to Node 4 :  [0, 5, 4] 2
# From Node 0  to Node 5 :  [0, 5] 1
# From Node 0  to Node 6 :  Not Connected None
# From Node 0  to Node 7 :  Not Connected None
# From Node 0  to Node 8 :  Not Connected None
# From Node 0  to Node 9 :  Not Connected None
# From Node 0  to Node 10:  Not Connected None
# From Node 0  to Node 11:  Not Connected None
# From Node 0  to Node 12:  Not Connected None
# 
# Shortest path from 7  to 4 :  [7, 6, 4] 2
# Shortest path from 7  to 0 :  [7, 6, 0] 2
# Shortest path from 10 to 12:  [10, 12] 1
# Shortest path from 10 to 9 :  [10, 12, 9] 2
