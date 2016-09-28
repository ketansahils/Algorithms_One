from MaxHeap import MaxHeap
import random

class HeapSort(MaxHeap):
	def __init__(self,arr):
		MaxHeap.__init__(self)
		self._array = [None] + arr
		self._N = len(arr)

	def insert(self,i):
		print "Cannot Insert"

	def sort(self):
		k = self._N/2
		while k > 0:
			self._sink(k)
			k -= 1
		arr = [None]*self._N
		while self._N > 0:
			arr[self._N] = self.delMax()
		return arr

if __name__ == '__main__':
	for j in range(10):
		arr = [i for i in range(j)]
		random.shuffle(arr)
		k = HeapSort(arr)
		#print arr
		print k.sort()

# Sample Output

# []
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]