import sys, os
sys.path.insert(0, os.path.abspath('..'))
from WeekX.LinkedList import LinkedList
from WeekX.Queue import Queue
from WeekX.Stack import Stack

class EdgeWeightedGraph(object):
	def __init__(self,V):
		self._V = V
		self._adj = [LinkedList(None) for _ in range(self._V)]
		self._E = 0

	def addEdge(self,e):
		v = e.either()
		self._adj[v].append(e)
		self._adj[e.other(v)].append(e)
		self._E += 1

	def adjEdges(self,v):
		return self._adj[v]