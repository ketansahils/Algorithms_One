class IndexMinPQ(object):
	def __init__(self,N):
		self._N = N
		self._n = 0
		self._keys = [None] * (self._N+1)
		self._pq = [None] * (self._N+1)
		self._qp = [None] * (self._N+1)

	def findKey(self,index,key):
		return self._keys[index]

	def changeKey(self,index,key):
		self._keys[index] = key
		self._swim(self._qp[index])
		self._sink(self._qp[index])

	def decreaseKey(self,index,key):
		#print "Index:",index,"Key:",key
		#print "Keys:",self._keys
		#print "QP:",self._qp
		#print "PQ:",self._pq
		self._keys[index] = key
		self._swim(self._qp[index])

	def delMin(self):
		Min = self._pq[1]
		self._exch(1,self._n)
		self._n -= 1
		self._sink(1)

		self._pq[self._n+1] = None
		self._qp[Min] = None
		return Min

	def insert(self,i,key):
		self._n += 1
		self._keys[i] = key
		self._qp[i] = self._n
		self._pq[self._n] = i
		self._swim(self._n)

	def isEmpty(self):
		return self._n == 0

	def contains(self,index):
		return self._keys[index] is not None

	def size(self):
		return self._n

	def _exch(self,i,j):
		self._pq[i], self._pq[j] = self._pq[j], self._pq[i]
		self._qp[self._pq[i]] = i
		self._qp[self._pq[j]] = j

	def _swim(self,i):
		if i/2 == 0:
			return
		if self._keys[self._pq[i]] < self._keys[self._pq[i/2]]:
			self._exch(i,i/2)
			i = i/2
			self._swim(i)
			return

	def _sink(self,i):
		if 2*i > self._n:
			return
		j = self._lesser(2*i, 2*i+1)
		if self._keys[self._pq[i]] > self._keys[self._pq[j]]:
			self._exch(i,j)
			self._sink(j)
			return

	def _lesser(self,i,j):
		if i <= self._n and j <= self._n:
			if self._keys[self._pq[i]] > self._keys[self._pq[j]]:
				return j
			return i
		if i > self._n:
			return j
		return i
