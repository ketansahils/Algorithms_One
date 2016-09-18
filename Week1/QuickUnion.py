class QuickUnion(object):
	def __init__(self,N):
		self.__N = N
		self.__array = [_ for _ in range(N)]

	def root(self,i):
		if self.__array[i] == i: return i
		return self.root(self.__array[i])

	def connected(self,i,j):
		return self.root(i) == self.root(j)

	def union(self,i,j):
		k = self.root(i)
		self.__array[k] = self.root(j)

	def connComps(self):
		arrOfRoots = map(lambda x: self.root(x),self.__array)
		return len(set(arrOfRoots))

	def show(self):
		print ("{:<3}"*self.__N).format(*range(self.__N))
		print ("{:<3}"*self.__N).format(*self.__array)


if __name__ == '__main__':
	k = QuickUnion(10)
	k.union(6,5)
	k.union(5,0)
	print "0 --- 1 ",k.connected(0,1)
	k.union(0,1)
	k.union(2,1)
	k.union(7,1)
	k.union(1,8)
	k.union(4,3)
	print "0 --- 3 ",k.connected(0,3)
	k.union(3,8)
	k.union(9,8)

	print "7 --- 6 ",k.connected(7,6)
	print "9 --- 3 ",k.connected(9,3)

	k.show()
	print k.connComps()

	# 0 --- 1  False
	# 0 --- 3  False
	# 7 --- 6  True
	# 9 --- 3  True
	# 0  1  2  3  4  5  6  7  8  9  
	# 1  8  1  8  3  0  5  1  8  8
	# 1
