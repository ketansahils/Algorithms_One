from WDEdge import WDEdge
from EdgeWeightedDigraph import EdgeWeightedDigraph
from IndexMinPQ import IndexMinPQ

class Dijkstra(object):
	def __init__(self,EDG,source):
		self._EDG = EDG
		self._pq = IndexMinPQ(self._EDG._V)
		self._edgeTo = [None] * self._EDG._V
		self._disTo = [float('inf')] * self._EDG._V
		self._marked = [False] * self._EDG._V

		self._pq.insert(source,0)
		self._disTo[source] = 0
		while not self._pq.isEmpty():
			Min = self._pq.delMin()
			self._marked[Min] = True
			#print "Min:",Min
			for edge in self._EDG.adjEdges(Min).traverse():
				self.relax(edge)

	def relax(self,edge):
		v, w = edge.From(), edge.To()
		#print "V:",v,"W:",w
		if self._disTo[w] > self._disTo[v] + edge.weight:
			self._disTo[w] = self._disTo[v] + edge.weight
			self._edgeTo[w] = edge
			if not self._marked[edge.To()]:
				if self._pq.contains(edge.To()):
				#print "contains:",edge.To()
				#print "Edge to:",edge.To(),"Dist to:",self._disTo[w]
					self._pq.decreaseKey(edge.To(),self._disTo[w])
				else:
					self._pq.insert(edge.To(),self._disTo[w])
			#self._pq.show()


if __name__ == '__main__':
	edg = EdgeWeightedDigraph(8)
	edg.addEdge(WDEdge(0,1,5))
	edg.addEdge(WDEdge(0,4,9))
	edg.addEdge(WDEdge(0,7,8))
	edg.addEdge(WDEdge(1,2,12))
	edg.addEdge(WDEdge(1,3,15))
	edg.addEdge(WDEdge(1,7,4))
	edg.addEdge(WDEdge(2,3,3))
	edg.addEdge(WDEdge(2,6,11))
	edg.addEdge(WDEdge(3,6,9))
	edg.addEdge(WDEdge(4,5,4))
	edg.addEdge(WDEdge(4,6,20))
	edg.addEdge(WDEdge(4,7,5))
	edg.addEdge(WDEdge(5,2,1))
	edg.addEdge(WDEdge(5,6,13))
	edg.addEdge(WDEdge(7,5,6))
	edg.addEdge(WDEdge(7,2,7))

	# edg2 = EdgeWeightedDigraph(4)
	# edg2.addEdge(WDEdge(0,1,1))
	# edg2.addEdge(WDEdge(0,2,0))
	# edg2.addEdge(WDEdge(0,3,99))
	# edg2.addEdge(WDEdge(1,2,1))
	# edg2.addEdge(WDEdge(3,1,-300))

	d = Dijkstra(edg,0)
	print d._disTo
	print map(lambda x: x.From() if x is not None else x,d._edgeTo)

# [0, 5, 14, 17, 9, 13, 25, 8]
# [None, 0, 5, 2, 0, 4, 2, 0]
