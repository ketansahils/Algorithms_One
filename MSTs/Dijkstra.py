from WDEdge import WDEdge
from EdgeWeightedDigraph import EdgeWeightedDigraph
from IndexMinPQ import IndexMinPQ

class Dijkstra(object):
	def __init__(self,EDAG,source):
		self._EDAG = EDAG
		self._pq = IndexMinPQ(self._EDAG._V)
		self._edgeTo = [None] * self._EDAG._V
		self._disTo = [float('inf')] * self._EDAG._V

		self._pq.insert(source,0)
		self._disTo[source] = 0
		while not self._pq.isEmpty():
			Min = self._pq.delMin()
			#print "Min:",Min
			for edge in self._EDAG.adjEdges(Min).traverse():
				self.relax(edge)

	def relax(self,edge):
		v, w = edge.From(), edge.To()
		#print "V:",v,"W:",w
		if self._disTo[w] > self._disTo[v] + edge.weight:
			self._disTo[w] = self._disTo[v] + edge.weight
			self._edgeTo[w] = edge

			if self._pq.contains(edge.To()):
				#print "Edge to:",edge.To(),"Dist to:",self._disTo[w]
				self._pq.decreaseKey(edge.To(),self._disTo[w])
			else:
				self._pq.insert(edge.To(),self._disTo[w])


if __name__ == '__main__':
	edag = EdgeWeightedDigraph(8)
	edag.addEdge(WDEdge(0,1,5))
	edag.addEdge(WDEdge(0,4,9))
	edag.addEdge(WDEdge(0,7,8))
	edag.addEdge(WDEdge(1,2,12))
	edag.addEdge(WDEdge(1,3,15))
	edag.addEdge(WDEdge(1,7,4))
	edag.addEdge(WDEdge(2,3,3))
	edag.addEdge(WDEdge(2,6,11))
	edag.addEdge(WDEdge(3,6,9))
	edag.addEdge(WDEdge(4,5,4))
	edag.addEdge(WDEdge(4,6,20))
	edag.addEdge(WDEdge(4,7,5))
	edag.addEdge(WDEdge(5,2,1))
	edag.addEdge(WDEdge(5,6,13))
	edag.addEdge(WDEdge(7,5,6))
	edag.addEdge(WDEdge(7,2,7))

	d = Dijkstra(edag,0)
	print d._disTo
	print map(lambda x: (x.To()) if x is not None else x,d._edgeTo)

