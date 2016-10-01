from NodeBST import NodeBST
import os, sys
sys.path.insert(0,os.path.abspath('..'))
from WeekX.Queue import Queue

class BST(object):
	
	def __init__(self,key,value):
		self._root = NodeBST(key,value)

	def delMin(self):
		return self._delMin(node._root)

	def _delMin(self,node):
		if node._left == None:
			return node._right
		node._left = self._delMin(node._left)
		node._count = 1 + self.size(node._left) + self.size(node._right)
		return node

	#def delete(self,node):


	def inorder(self):
		q = Queue(None)
		self._inorder(self._root,q)
		q.show()

	def _inorder(self,node,q):
		if node == None:
			return
		self._inorder(node._left,q)
		q.enqueue(node)
		self._inorder(node._right,q)

	def rank(self,key):
		return self._rank(self._root,key)

	def _rank(self,node,key):
		if node == None:
			return 0
		if node._key == key:
			return self.size(node._left)
		if node._key > key:
			return self._rank(node._left,key)
		if node._key < key:
			return 1 + self._size(node._left) + self._rank(node._right,key)

	def size(self,node):
		if node == None:
			return 0
		return node._count

	def floor(self,key):
		return self._floorx(self,self._root,key)

	def _floorx(self,node,key):
		if node == None:
			return None
		if node._key == key:
			return node
		if node._key > key:
			return self._floorx(node._left,key)
		t = self._floorx(node._right,key)
		if t == None:
			t = Node
		return t

	def get(self,key):
		k = self._root
		while k:
			if k._key == key:
				return k._val
			if k._key > key:
				k = k._left
			else:
				k = k._right
		return None

	def put(self,key,value):
		return self._putx(self._root,key,value)

	def _putx(self,node,key,value):
		if node == None:
			node = NodeBST(key,value)

		elif node._key == key:
			node._val = value

		if node._key > key:
			node._left = self._putx(node._left,key,value)

		if node._key < key:
			node._right = self._putx(node._right,key,value)

		node._count = 1 + self.size(node._left) + self.size(node._right)
		return node
