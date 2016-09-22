class QuickFindWeighted(object):
	def __init__(self,N):
		self.__N = N
		self.__array = [_ for _ in range(N)]
		self.__size = [1 for _ in range(N)]

	def root(self, p):
		while self.__array[p] != p:
			p = self.__array[p]
		return p

	def rootFlatten(self, p):
		while self.__array[p] != p:
			temp = p
			p = self.__array[p]
			self.__array[temp] = self.root(p)
		return p

	def union(self, p, q):
		if not self.connected(p,q):
			idp = self.rootFlatten(p)
			idq = self.rootFlatten(q)
			if self.__size[idp] >= self.__size[idq]:
				self.__size[idp] += self.__size[idq]
				self.__array[idq] = idp
			else:
				self.__size[idq] += self.__size[idp]
				self.__array[idp] = idq

	def find(self, p):
		return self.__array[p]

	def connected(self, p, q):
		return self.root(p) == self.root(q)

	def connComps(self):
		arrOfRoots = map(lambda x: self.root(x),self.__array)
		return len(set(arrOfRoots))

	def show(self):
		print ("{:<3}"*self.__N).format(*range(self.__N))
		print ("{:<3}"*self.__N).format(*self.__array)


if __name__ == '__main__':
	k = QuickFindWeighted(10)
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

	k.union(5,2)
	print "After joining",5,2
	k.show()
	print k.connComps()

	k.union(3,5)
	print "After joining",3,5
	k.show()
	print k.connComps()

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
