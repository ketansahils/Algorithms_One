class QuickFind(object):
	def __init__(self,N):
		self._N = N
		self._array = [_ for _ in range(N)]

	def union(self,p,q):
		if self.connected(p,q): return
		pval = self._array[p]
		for i,j in enumerate(self._array):
			self._array[i] = self._array[q] \
			if j == pval else self._array[i]

	def connected(self,p,q):
		return self._array[p] == self._array[q]

	def find(self,p):
		return self._array[p]

	def connComps(self):
		return len(set(self._array))

	def show(self):
		print ("{:<3}"*self._N).format(*range(self._N))
		print ("{:<3}"*self._N).format(*self._array)


if __name__ == '__main__':
	k = QuickFind(10)
	k.union(0,5)
	k.union(5,6)
	k.union(1,2)
	k.union(7,2)
	k.union(3,8)
	k.union(4,3)
	k.union(9,3)
	k.union(3,9)

	print "0 --- 1 ",k.connected(0,1)
	print "0 --- 3 ",k.connected(0,3)
	print "7 --- 6 ",k.connected(7,6)
	print "9 --- 3 ",k.connected(9,3)

	k.show()
	print k.connComps()

	# 0 --- 1  False
	# 0 --- 3  False
	# 7 --- 6  False
	# 9 --- 3  True
	# 0  1  2  3  4  5  6  7  8  9  
	# 6  2  2  8  8  6  6  2  8  8  
	# 3
