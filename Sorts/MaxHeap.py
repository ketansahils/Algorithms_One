class MaxHeap(object):
	def __init__(self):
		self._array = [None]
		self._N = 0

	def _isEmpty(self):
		return self._N == 0

	def insert(self,k):
		self._array.append(k)
		self._N += 1
		self._swim(self._N)

	def _swim(self,i):
		while i > 1 and i <= self._N:
			if self._array[i] > self._array[i/2]:
				self._exch(i,i/2,self._array)
			i = i/2

	def _sink(self,i):
		while 2*i <= self._N and i >= 1:
			k = 2*i if self._larger(2*i, 2*i+1, self._array) else 2*i+1
			if self._array[i] < self._array[k]:
				self._exch(i,k,self._array)
			i = k

	def delMax(self):
		if not self._isEmpty():
			self._exch(1,self._N,self._array)
			self._N -= 1
			self._sink(1)
			result = self._array.pop()
			return result


	def _exch(self,i,j,arr):
		arr[i], arr[j] = arr[j], arr[i]

	def _larger(self,i,j,arr):
		if j > self._N:
			return True
		return arr[i] > arr[j]


if __name__ == '__main__':
	k = MaxHeap()
	for j in range(10):
		for i in range(j):
			k.insert(i)
		for i in range(j):
			print k.delMax(),
		print

# Sample Output

# 0
# 1 0
# 2 1 0
# 3 2 1 0
# 4 3 2 1 0
# 5 4 3 2 1 0
# 6 5 4 3 2 1 0
# 7 6 5 4 3 2 1 0
# 8 7 6 5 4 3 2 1 0