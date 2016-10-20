import sys, os
sys.path.insert(0, os.path.abspath('..'))
from WeekX.Queue import Queue
from MinPQ import MinPQ
from WEdge import WEdge
from EdgeWeightedGraph import EdgeWeightedGraph
 
class PrimsLazy(object):
	def __init__(self,G):
		self.mst = Queue()
		self.minPQ = MinPQ()
		self.marked = [False] * G._V

		self._addNonConnected(0,G)

		while not self.minPQ.isEmpty():
			minEdge = self.minPQ.delMin()
			a = minEdge.either()
			b = minEdge.other(a)
			#print "minEdge:",a,b,minEdge.weight

			if self.marked[a] and self.marked[b]:
				continue
			self.mst.enqueue(minEdge)

			if self.marked[a]:
				self._addNonConnected(b,G)
			else:
				self._addNonConnected(a,G)

	def _addNonConnected(self,x,G):
		self.marked[x] = True
		#print "new vertex: ",x
		#m = []
		for edge in G.adjEdges(x).traverse():
			if not self.marked[edge.other(x)]:
		#		m.append([edge.v,edge.w,edge.weight])
				self.minPQ.insert(edge)
		#print "edges: ",m
		#print "marked: ",self.marked
		#import copy
		#a = copy.deepcopy(self.minPQ)
		#while not a.isEmpty():
		#	k = a.delMin()
		#	print k.v,k.w,k.weight
		#print

	def edges(self):
		k = map(lambda x: (x.v, x.w, x.weight),self.mst.show())
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

	from pprint import pprint
	P = PrimsLazy(a)
	pprint(P.edges())

# [(0, 7, 0.16),
#  (1, 7, 0.19),
#  (0, 2, 0.26),
#  (2, 3, 0.17),
#  (5, 7, 0.28),
#  (4, 5, 0.35),
#  (6, 2, 0.4)]