class SuccessorWithDelete(object):
	def __init__(self,N):
		self._N = N
		self._suc = [i+1 for i in range(N)]
		self._suc[N-1] = N-1
		self._pred = [i-1 for i in range(N)]
		self._pred[0] = 0

	def remove(self,x):
		px = self._pred[x]
		sx = self._suc[x]
		if sx == x:
			self._suc[px] = px
		elif px == x:
			self._pred[sx] = sx
		else:
			self._suc[px] = sx
			self._pred[sx] = px
		self._pred[x] = None
		self._suc[x] = None

	def successor(self,x):
		return self._suc[x]

	def predecessor(self,x):
		return self._pred[x]


if __name__ == '__main__':
	k = SuccessorWithDelete(4)
	k.remove(1)
	print k.successor(2), k.predecessor(2)
	print k.successor(0), k.predecessor(0)

	k.remove(0)
	print k.successor(1), k.predecessor(1)
	print k.successor(2), k.predecessor(2)

# Sample Output

# 3 0
# 2 0
# None None
# 3 2