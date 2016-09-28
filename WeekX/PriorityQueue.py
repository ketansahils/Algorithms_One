class PriorityQueue(object):
	def __init__(self):
		self._array = []
		self._N = 0

	def insert(self,key):
		self._array.append(key)
		self._N += 1

	def delMax(self):
		if self.isEmpty():
			return
		xmax = 0
		for i in range(1,self._N):
			if self._array[i] > self._array[xmax]:
				xmax = i
		self.exch(xmax,self._N-1,self._array)
		self._N -= 1
		return self._array[self._N]

	def isEmpty(self):
		return self._N == 0

	def exch(self,i,j,arr):
		arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
	k = PriorityQueue()
	for item in [3,2,4,5,6,7,5,343,2]:
		k.insert(item)
	while not k.isEmpty():
		print k.delMax()

# Sample Output

# 343
# 7
# 6
# 5
# 5
# 4
# 3
# 2
# 2

