import os, sys
sys.path.insert(0, os.path.abspath('..'))
from WeekX.LinkedList import LinkedList

class Bag(LinkedList):
	def __init__(self,val):
		LinkedList.__init__(val)

	def addBefore(self,a,b):
		pass

	def addAfter(self,a,b):
		pass

	def addFirst(self,val):
		pass

	def addLast(self,val):
		pass

	def add(self,val):
		LinkedList.addLast(self,val)

class Graph(object):
	def __init__(self,V):
		self._V = V
		#self._adj = [[] for _ in range(V)]
		self._adj = [Bag(None) for _ in range(V)]

	def addEdge(self,a,b):
		self._adj[a].add(b)
		self._adj[b].add(a)

	def adjVertices(self,a):
		return self._adj[a].traverse()