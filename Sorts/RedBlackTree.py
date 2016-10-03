from NodeRBT import NodeRBT
from BST import BST
import os, sys
sys.path.insert(0,os.path.abspath('..'))
from WeekX.Queue import Queue

class RedBlackTree(BST):
	RED = True
	BLACK = False

	def __init__(self,key,value,color):
		if key == None and value == None:
			self._root = None
			return
		self._root = NodeRBT(key,value,RedBlackTree.BLACK)

	def _rotateLeft(self,node):
		x = node._right
		node._right = x._left
		x._left = node
		x._color = node._color
		node._color = RedBlackTree.RED
		return x

	def _rotateRight(self,node):
		x = node._left
		node._left = x._right
		x._right = node
		x._color = node._color
		node._color = RedBlackTree.RED
		return x

	def _flipColors(self,node):
		node._color = RedBlackTree.RED
		node._left._color = RedBlackTree.BLACK
		node._right._color = RedBlackTree.BLACK

	def put(self,key,val):
		self._root = self._putx(self._root,key,val)
		if self._root._color:
			self._root._color = RedBlackTree.BLACK

	def isRed(self,node):
		if node == None:
			return None
		return node._color == RedBlackTree.RED

	def _putx(self,node,key,val):
		if node == None:
			return NodeRBT(key,val,RedBlackTree.RED)
		if node._key < key:
			node._right = self._putx(node._right,key,val)
		elif node._key > key:
			node._left = self._putx(node._left,key,val)
		else:
			node._val = val
		if self.isRed(node._right) and not self.isRed(node._left):
			node = self._rotateLeft(node)
		if self.isRed(node._left) and self.isRed(node._left._left):
			node = self._rotateRight(node)
		if self.isRed(node._right) and self.isRed(node._left):
			self._flipColors(node)
		return node

	def inorder(self):
		q = Queue(None)
		self._inorder(self._root,q)
		while not q.isEmpty():
			k = q.dequeue()
			print k._val._key, k._val._color
		print


if __name__ == '__main__':
	k = RedBlackTree(None,None,None)
	import random
	l = range(10)
	random.shuffle(l)
	print l
	for item in l:
		k.put(item,item*10)
		k.inorder()
