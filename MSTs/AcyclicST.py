# Only for Acyclic Weighted Digraphs
# EVEN IF EDGE WEIGHTS ARE NEGATIVE!!!

from TopoSortWDAG import TopoSortWDAG
from EdgeWeightedDigraph import EdgeWeightedDigraph

class AcyclicST(object):
	def __init__(self,EDAG,source):
		self._EDAG = EDAG
		self._distTo = [float('inf')] * self._EDAG._V
		self._edgeTo = [None] * self._EDAG._V
		self._distTo[source] = 0

		topoSorted = TopoSortWDAG(self._EDAG)
		topoSorted = topoSorted.topoSorted()

		for vertex in topoSorted:
			for edge in self._EDAG.adjEdges(vertex).traverse():
				self.relax(edge)

	def relax(self,edge):
		if self._distTo[edge.To()] > self._distTo[edge.From()] + edge.weight:
			self._distTo[edge.To()] = self._distTo[edge.From()] + edge.weight
			self._edgeTo[edge.To()] = edge

	def MST(self):
		print map(lambda x: (x.From(),x.To(),x.weight) if x else None,self._edgeTo)
		return self._distTo

if __name__ == '__main__':
	edag = EdgeWeightedDigraph(8)
	edag.addEdgeBreak(0,1,5)
	edag.addEdgeBreak(0,4,9)
	edag.addEdgeBreak(0,7,8)
	edag.addEdgeBreak(1,2,12)
	edag.addEdgeBreak(1,3,15)
	edag.addEdgeBreak(1,7,4)
	edag.addEdgeBreak(2,3,3)
	edag.addEdgeBreak(2,6,11)
	edag.addEdgeBreak(3,6,9)
	edag.addEdgeBreak(4,5,4)
	edag.addEdgeBreak(4,6,20)
	edag.addEdgeBreak(4,7,5)
	edag.addEdgeBreak(5,2,1)
	edag.addEdgeBreak(5,6,13)
	edag.addEdgeBreak(7,5,6)
	edag.addEdgeBreak(7,2,7)

	acst = AcyclicST(edag,0)
	print acst.MST()

# [None, (0, 1, 5), (5, 2, 1), (2, 3, 3), (0, 4, 9), (4, 5, 4), (2, 6, 11), (0, 7, 8)]
# [0, 5, 14, 17, 9, 13, 25, 8]

