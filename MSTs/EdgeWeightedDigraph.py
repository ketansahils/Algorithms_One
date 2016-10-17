import sys, os
sys.path.insert(0, os.path.abspath('..'))
from WeekX.LinkedList import LinkedList
from WDEdge import WDEdge

class EdgeWeightedDigraph(object):
	def __init__(self,V):
		self._V = V
		self._adj = [LinkedList(None) for _ in range(self._V)]
		self._E = 0
		self._edges = []

	def addEdge(self,e):
		v = e.From()
		self._adj[v].addLast(e)
		self._edges.append(e)
		self._E += 1

	def adjEdges(self,v):
		return self._adj[v]

	def edges(self):
		return self._edges

	def addEdgeBreak(self,to,From,weight):
		self.addEdge(WDEdge(to,From,weight))