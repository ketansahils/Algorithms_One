from Node import Node

class Stack(object):

	def __init__(self,val):
		self._first = Node(val,None)

	def isEmpty(self):
		return self._first == None

	def push(self,val):
		latest = Node(val,self._first)
		self._first = latest

	def pop(self):
		if not self.isEmpty():
			popped = self._first
			self._first = self._first._next
			return popped
		return

	def show(self):
		n = self._first
		while n:
			print n._val,
			n = n._next
		print


if __name__ == '__main__':
	s = Stack('ketan')
	text = "to be or not to - be - - that - - - is"
	for item in text.split():
		if item == '-':
			s.pop()
		else:
			s.push(item)
		s.show()

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