from Node import Node

class Queue(object):

	def __init__(self,val):
		self._first = Node(val,None)
		self._last = self._first

	def isEmpty(self):
		return self._first == None

	def enqueue(self,val):
		last = self._last
		latest = Node(val,None)
		self._last = latest
		if self.isEmpty():
			self._first = self._last
		else:
			last._next = latest

	def dequeue(self):
		if not self.isEmpty():
			oldFirst = self._first
			self._first = oldFirst._next
			if self.isEmpty():
				self._last = self._first
			return oldFirst

	def show(self):
		i = self._first
		while i:
			print i._val,
			i = i._next
		print


if __name__ == '__main__':
	q = Queue('ketan')
	text = "to be or not to - be - - that - - - is - - - - ketan sahil sharma -"
	for item in text.split():
		if item == '-':
			q.dequeue()
		else:
			q.enqueue(item)
		q.show()

# ketan to
# ketan to be
# ketan to be or
# ketan to be or not
# ketan to be or not to
# to be or not to
# to be or not to be
# be or not to be
# or not to be
# or not to be that
# not to be that
# to be that
# be that
# be that is
# that is
# is
# 
# 
# ketan
# ketan sahil
# ketan sahil sharma
# sahil sharma