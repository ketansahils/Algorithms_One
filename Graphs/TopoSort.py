import sys,os
sys.path.insert(0,os.path.abspath('..'))
from Digraph import Digraph
from WeekX.Stack import Stack

class TopoSort(object):
	def __init__(self,dag):
		self._dag = dag
		self._stack = Stack(None)
		self._marked = [False] * self._dag._V
		self._edgeTo = [None] * self._dag._V
		self.postorder()

	def postorder(self):
		for v in range(self._dag._V):
			if not self._marked[v]:
				self._marked[v] = True
				self._edgeTo[v] = v
				self._postorder(v)
				self._stack.push(v)

	def _postorder(self,vertex):
		for v in self._dag.adjVertices(vertex):
			if not self._marked[v]:
				self._marked[v] = True
				self._edgeTo[v] = vertex
				self._postorder(v)
				self._stack.push(v)

	def topoSorted(self):
		return self._stack.show()


if __name__ == '__main__':
	dag = Digraph(7)
	dag.addEdge(0,1)
	dag.addEdge(0,2)
	dag.addEdge(0,5)
	dag.addEdge(3,6)
	dag.addEdge(3,5)
	dag.addEdge(3,4)
	dag.addEdge(5,2)
	dag.addEdge(6,4)
	dag.addEdge(6,0)
	dag.addEdge(3,2)
	dag.addEdge(1,4)

	top = TopoSort(dag)
	print top.topoSorted()

# [3, 6, 0, 5, 2, 1, 4]