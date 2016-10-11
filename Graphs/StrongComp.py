import sys,os
sys.path.insert(0,os.path.abspath('..'))
from Digraph import Digraph
from WeekX.Stack import Stack
from TopoSort import TopoSort

class StrongComp(TopoSort):
	def __init__(self,digraph):
		#TopoSort.__init__(self,digraph)
		self._digraph = digraph
		self._rev = digraph.reverse()
		self._marked = [False] * self._digraph._V
		self._edgeTo = [None] * self._digraph._V
		self._stack = Stack(None)
		self.postOrder(self._rev)

	def cc(self):
		self._marked = [False] * self._digraph._V
		ccArr = [None] * self._digraph._V
		count = 0
		while not self._stack.isEmpty():
			v = self._stack.pop()._val
			if not self._marked[v]:
				self._cc(v,ccArr,count)
				count += 1
		return ccArr

	def _cc(self,vertex,arr,count): 
		if self._marked[vertex]:
			return
		self._marked[vertex] = True
		arr[vertex] = count
		for v in self._digraph.adjVertices(vertex):
			self._cc(v,arr,count)


if __name__ == '__main__':
	dg = Digraph(13)
	dg.addEdge(0,5)
	dg.addEdge(0,1)
	dg.addEdge(2,0)
	dg.addEdge(6,0)
	dg.addEdge(3,5)
	dg.addEdge(5,4)
	dg.addEdge(4,2)
	dg.addEdge(4,3)
	dg.addEdge(3,2)
	dg.addEdge(2,3)
	dg.addEdge(6,4)
	dg.addEdge(11,4)
	dg.addEdge(6,8)
	dg.addEdge(8,6)
	dg.addEdge(7,6)
	dg.addEdge(6,9)
	dg.addEdge(9,11)
	dg.addEdge(11,12)
	dg.addEdge(12,9)
	dg.addEdge(10,12)
	dg.addEdge(9,10)
	dg.addEdge(7,9)

	sc = StrongComp(dg)
	print sc.cc()

# [1, 0, 1, 1, 1, 1, 3, 4, 3, 2, 2, 2, 2]
