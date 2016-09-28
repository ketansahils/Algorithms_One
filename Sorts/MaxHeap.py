class MaxHeap(object):
	def __init__(self):
		self.__array = [None]
		self.__N = 0

	def _isEmpty(self):
		return self.__N == 0

	def insert(self,k):
		self.__array.append(k)
		self.__N += 1
		self._swim(self.__N)

	def _swim(self,i):
		while i > 1 and i <= self.__N:
			if self.__array[i] > self.__array[i/2]:
				self._exch(i,i/2,self.__array)
			i = i/2

	def _sink(self,i):
		while 2*i+1 <= self.__N and i >= 1:
			k = 2*i if self._larger(2*i, 2*i+1, self.__array) else 2*i+1
			if self.__array[i] < self.__array[k]:
				self._exch(i,k,self.__array)
			i = k

	def delMax(self):
		if not self._isEmpty():
			self._exch(1,self.__N,self.__array)
			self.__N -= 1
			self._sink(1)
			result = self.__array[self.__N+1]
			self.__array.pop()
			return result


	def _exch(self,i,j,arr):
		arr[i], arr[j] = arr[j], arr[i]

	def _larger(self,i,j,arr):
		return arr[i] > arr[j]

if __name__ == '__main__':
	k = MaxHeap()
	for i in range(10):
		k.insert(i)
	for i in range(10):
		print k.delMax()