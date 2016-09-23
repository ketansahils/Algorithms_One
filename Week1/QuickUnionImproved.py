class QuickFindWeighted(object):
	def __init__(self,N):
		self._N = N
		self._array = [_ for _ in range(N)]
		self._size = [1 for _ in range(N)]
		self._largest = [_ for _ in range(N)]

	def root(self, p):
		while self._array[p] != p:
			p = self._array[p]
		return p


	def union(self, p, q):
		if not self.connected(p,q):
			idp = self.root(p)
			idq = self.root(q)
			if self._largest[idp] > self._largest[idq]:
				self._largest[idq] = self._largest[idp]
			else:
				self._largest[idp] = self._largest[idq]

			if self._size[idp] >= self._size[idq]:
				self._size[idp] += self._size[idq]
				self._array[idq] = idp
			else:
				self._size[idq] += self._size[idp]
				self._array[idp] = idq

	def find(self, p):
		return self._array[p]

	def connected(self, p, q):
		return self.root(p) == self.root(q)

	def connComps(self):
		arrOfRoots = map(lambda x: self.root(x),self._array)
		return len(set(arrOfRoots))

	def show(self):
		print ("{:<3}"*self._N).format(*range(self._N))
		print ("{:<3}"*self._N).format(*self._array)

	def largest(self,i):
		return self._largest[self.root(i)]


if __name__ == '__main__':
	k = QuickFindWeighted(10)
	k.union(0,5)
	k.union(5,6)
	print k.largest(0)
	k.union(1,2)
	k.union(7,2)
	print k.largest(1)
	k.union(3,8)
	k.union(4,3)
	print k.largest(3)
	k.union(9,3)
	k.union(3,9)
	print k.largest(3)


	print "0 --- 1 ",k.connected(0,1)
	print "0 --- 3 ",k.connected(0,3)
	print "7 --- 6 ",k.connected(7,6)
	print "9 --- 3 ",k.connected(9,3)

	k.show()
	print k.connComps()

	k.union(5,2)
	print "After joining",5,2
	k.show()
	print k.connComps()

	k.union(3,5)
	print "After joining",3,5
	k.show()
	print k.connComps()
	print k.largest(0)

	# 0 --- 1  False
	# 0 --- 3  False
	# 7 --- 6  False
	# 9 --- 3  True
	# 0  1  2  3  4  5  6  7  8  9  
	# 0  1  1  3  3  0  0  1  3  3  
	# 3

	# After joining 5 2
	# 0  1  2  3  4  5  6  7  8  9  
	# 0  0  1  3  3  0  0  1  3  3  
	# 2

	#After joining 3 5
	# 0  1  2  3  4  5  6  7  8  9  
	# 0  0  1  0  3  0  0  1  3  3  
	# 1
