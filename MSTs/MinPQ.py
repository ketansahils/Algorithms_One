class MinPQ(object):
	def __init__(self):
		self._array = []
		self._N = 0

	def insert(self,key):
		self._array.append(key)
		self._N += 1

	def delMin(self):
		if self.isEmpty():
			return
		xmin = 0
		for i in range(1,self._N):
			if self._array[i] < self._array[xmin]:
				xmin = i
		self.exch(xmin,self._N-1,self._array)
		self._N -= 1
		return self._array[self._N]

	def isEmpty(self):
		return self._N == 0

	def exch(self,i,j,arr):
		arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
	k = MinPQ()
	for item in [3,2,4,5,6,7,5,343,2]:
		k.insert(item)
	while not k.isEmpty():
		print k.delMin()

# 2
# 2
# 3
# 4
# 5
# 5
# 6
# 7
# 343