import sys, os
sys.path.insert(0, os.path.abspath('..'))
from Week1.QuickUnion import QuickUnion
from WeekX.Queue import Queue
from MinPQ import MinPQ
from WEdge import WEdge
from EdgeWeightedGraph import EdgeWeightedGraph

class KruskalMST(object):
	def __init__(self,G):
		minPQ = MinPQ()
		self._mst = Queue(None)
		for edge in G._edges:
			minPQ.insert(edge)

		qu = QuickUnion(G._V)
		while not minPQ.isEmpty() and self._mst._size < G._V:
			e = minPQ.delMin()
			v1 = e.either()
			v2 = e.other(v1)
			if not qu.connected(v1,v2):
				qu.union(v1,v2)
				self._mst.enqueue(e)

	def edges(self):
		k = map(lambda x: (x.v, x.w, x.weight),self._mst.show())
		return k



if __name__ == '__main__':
	a = EdgeWeightedGraph(8)
	a.addEdge(WEdge(4,5,0.35))
	a.addEdge(WEdge(1,2,0.36))
	a.addEdge(WEdge(4,7,0.37))
	a.addEdge(WEdge(0,4,0.38))
	a.addEdge(WEdge(6,2,0.40))
	a.addEdge(WEdge(3,6,0.52))
	a.addEdge(WEdge(6,0,0.58))
	a.addEdge(WEdge(6,4,0.93))
	a.addEdge(WEdge(2,7,0.34))
	a.addEdge(WEdge(1,5,0.32))
	a.addEdge(WEdge(1,3,0.29))
	a.addEdge(WEdge(5,7,0.28))
	a.addEdge(WEdge(0,2,0.26))
	a.addEdge(WEdge(1,7,0.19))
	a.addEdge(WEdge(2,3,0.17))
	a.addEdge(WEdge(0,7,0.16))

	K = KruskalMST(a)
	print K.edges()