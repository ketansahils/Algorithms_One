from Node import Node

class LinkedList(object):
	def __init__(self,val):
		if val == None:
			self._head = None
			self._tail = None
			self._size = 0
			return
		self._head = Node(val,None)
		self._tail = self._head
		self._size = 1

	def addLast(self,val):
		new_node = Node(val,None)
		if self._tail:
			self._tail._next = new_node
			self._tail = self._tail._next
		else:
			self._head = new_node
			self._tail = self._head
		self._size += 1

	def addFirst(self,val):
		new_node = Node(val,self._head)
		self._head = new_node
		if not self._tail:
			self._tail = self._head
		self._size += 1

	def addAfter(self,val,newVal):
		node = self._head
		while node and node._val != val:
			node = node._next
		if node:
			node._next = Node(newVal,node._next)
			self._size += 1

	def addBefore(self,val,newVal):
		node = self._head
		if node and node._val == val:
			self._head = Node(newVal,self._head)
			self._size += 1
			return
		while node._next and node._next._val != val:
			node = node._next
		if node._next:
			node._next = Node(newVal,node._next)
			self._size += 1

	def delete(self,val):
		if self._size == 0:
			return
		node = self._head
		if node and node._val == val:
			self._head = None
			self._tail = None
			self._size = 0
			return
		while node._next and node._next._val != val:
			node = node._next
		if node._next:
			if node._next == self._tail:
				node._next = None
				self._tail = node
			else:
				node._next = node._next._next
			self._size -= 1

	def traverse(self):
		node = self._head
		arr = [None] * self._size
		i = 0
		while i < self._size:
			arr[i] = node._val
			node = node._next
			i += 1
		return arr

if __name__ == '__main__':
	k = LinkedList(None)
	l = range(10)
	#import random
	#random.shuffle(l)
	for item in l:
		k.addLast(item)
	print k.traverse()
	for item in range(9,4,-1):
		k.delete(item)
	print k.traverse()
	for item in l:
		k.addLast(item)
	k.addLast('last')
	k.addBefore(0,'Before zero')
	k.addBefore(5,'before 5')
	k.addAfter(0,'after zero')
	k.addFirst(89898)
	k.delete('after zero')
	print k.traverse()


