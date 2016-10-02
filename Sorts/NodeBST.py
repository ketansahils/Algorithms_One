import os, sys
sys.path.insert(0, os.path.abspath('..'))
from WeekX.Node import Node

class NodeBST(Node):
	def __init__(self,key,val):
		Node.__init__(self,val,None)
		del self._next
		self._left = None
		self._right = None
		self._key = key
		self._count = 1


if __name__ == '__main__':
	k = NodeBST('ketan',424)
	print k._left
	print k._right
	print k._key
	print k._val