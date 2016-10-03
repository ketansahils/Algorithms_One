from NodeBST import NodeBST

class NodeRBT(NodeBST):
	def __init__(self,key,val,color):
		NodeBST.__init__(self,key,val)
		self._color = color


if __name__ == '__main__':
	k = NodeRBT(1,2,'RED')
	print k._color
	print k._val
	print k._key