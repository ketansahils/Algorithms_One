from Node import Node

class Stack(object):

	def __init__(self,val):
		if val == None:
			self._first = None
			self._size = 0
			return
		self._first = Node(val,None)
		self._size = 1

	def isEmpty(self):
		return self._first == None

	def push(self,val):
		latest = Node(val,self._first)
		self._first = latest
		self._size += 1

	def pop(self):
		if not self.isEmpty():
			popped = self._first
			self._first = self._first._next
			self._size -= 1
			return popped
		return

	def show(self):
		if self._size == 0:
			return None
		n = self._first
		arr = [None]*self._size
		for i in range(self._size):
			print n._val,
			arr[i] = n._val
			n = n._next
		print
		return arr


if __name__ == '__main__':
	s = Stack(None)
	text = "ketan to be or not to - be - - that - - - is"
	for item in text.split():
		if item == '-':
			s.pop()
		else:
			s.push(item)
		s.show()

# ketan
# to ketan
# be to ketan
# or be to ketan
# not or be to ketan
# to not or be to ketan
# not or be to ketan
# be not or be to ketan
# not or be to ketan
# or be to ketan
# that or be to ketan
# or be to ketan
# be to ketan
# to ketan
# is to ketan

