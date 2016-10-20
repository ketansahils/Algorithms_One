import sys,os
sys.path.insert(0,os.path.abspath('..'))
from WeekX.Stack import Stack
from MSTs.EdgeWeightedDigraph import EdgeWeightedDigraph
from WDEdge import WDEdge

class TopoSortWDAG(object):
	def __init__(self,EDAG):
		self._EDAG = EDAG
		self._marked = [False] * self._EDAG._V
		self._stack = Stack()

	def topoSort(self):
		for vertex, edges in enumerate(self._EDAG._adj):
			#print vertex
			if not self._marked[vertex]:
				self._marked[vertex] = True
				self._topoSort(vertex)
				self._stack.push(vertex)

	def _topoSort(self,v):
		for edge in self._EDAG._adj[v].traverse():
			k = edge.To()
			if not self._marked[k]:
				self._marked[k] = True
				self._topoSort(k)
				self._stack.push(k)

	def topoSorted(self):
		self.topoSort()
		return self._stack.show()


if __name__ == '__main__':
	dag = EdgeWeightedDigraph(8)
	dag.addEdge(WDEdge(0,1,5))
	dag.addEdge(WDEdge(0,4,9))
	dag.addEdge(WDEdge(0,7,8))
	dag.addEdge(WDEdge(1,2,12))
	dag.addEdge(WDEdge(1,3,15))
	dag.addEdge(WDEdge(1,7,4))
	dag.addEdge(WDEdge(2,3,3))
	dag.addEdge(WDEdge(2,6,11))
	dag.addEdge(WDEdge(3,6,9))
	dag.addEdge(WDEdge(4,5,4))
	dag.addEdge(WDEdge(4,6,20))
	dag.addEdge(WDEdge(4,7,5))
	dag.addEdge(WDEdge(5,2,1))
	dag.addEdge(WDEdge(5,6,13))
	dag.addEdge(WDEdge(7,5,6))
	dag.addEdge(WDEdge(7,2,7))
	top = TopoSortWDAG(dag)
	from pprint import pprint
	pprint(top.topoSorted())

# [0, 4, 1, 7, 5, 2, 3, 6]