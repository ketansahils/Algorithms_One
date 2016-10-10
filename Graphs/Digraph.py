import sys, os
sys.path.insert(0, os.path.abspath('..'))
from WeekX.LinkedList import LinkedList

class Digraph(object):
	def __init__(self,V):
		self._V = V
		self._adj = [LinkedList(None) for _ in range(self._V)]

	def addEdge(self,v,w):
		self._adj[v].addLast(w)

	def adjVertices(self,v):
		return self._adj[v].traverse()
