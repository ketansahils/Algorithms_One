from NodeBST import NodeBST
import os, sys
sys.path.insert(0,os.path.abspath('..'))
from WeekX.Queue import Queue

class BST(object):
	
	def __init__(self,key,value):
		if key == None and value == None:
			self._root = None
			return
		self._root = NodeBST(key,value)

	def delMin(self):
		self._root = self._delMin(node._root)

	def _delMin(self,node):
		if node._left == None:
			return node._right
		node._left = self._delMin(node._left)
		node._count = 1 + self.size(node._left) + self.size(node._right)
		return node

	def minNode(self,node):
		if node == None:
			return None
		while node._left != None:
			node = node._left
		return node

	def delete(self,key):
		self._root = self._delete(self._root,key)

	def _delete(self,node,key):
		if node == None:
			return None
		if node._key > key:
			node._left = self._delete(node._left,key)
		elif node._key < key:
			node._right = self._delete(node._right,key)
		else: 
			if node._left == None:
				return node._right
			if node._right == None:
				return node._left

			t = node
			node = self.minNode(t._right)
			node._right = self._delMin(t._right)
			node._left = t._left

		node._count = 1 + self.size(node._left) + self.size(node._right)
		return node

	def inorder(self):
		q = Queue(None)
		self._inorder(self._root,q)
		while not q.isEmpty():
			k = q.dequeue()
			print k._val._key, k._val._val, k._val._count
		print

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
		self._root = self._putx(self._root,key,value)

	def _putx(self,node,key,value):
		if node == None:
			node = NodeBST(key,value)

		else:
			if node._key == key:
				node._val = value

			elif node._key > key:
				node._left = self._putx(node._left,key,value)

			# node._key < key:
			else:
				node._right = self._putx(node._right,key,value)

			node._count = 1 + self.size(node._left) + self.size(node._right)
		return node


if __name__ == '__main__':
	import random
	l = range(0,10)
	random.shuffle(l)
	print l
	k = BST(l[0],l[0]*10)
	for item in l[1:]:
		k.put(item,10*item)
	k.inorder()
	k.delete(7)
	k.inorder()
	m = BST(None,None)
	for item in l:
		m.put(item,10*item)
	m.inorder()
	m.delete(7)
	m.inorder()
