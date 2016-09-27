import random

class QuickSort(object):
	def __init__(self,array):
		self._array = array
		self._N = len(array)
		random.shuffle(self._array)

	def sort(self):
		start = 0
		lcursor = 1
		rcursor = self._N - 1
		self._sorter(start,lcursor,rcursor)
		return self._array

	def _sorter(self,start,left,right):
		if left > right:
			return
		istart = start
		iright = right
		while left <= right:
			if self._array[left] < self._array[start]:
				left += 1
			elif self._array[right] >= self._array[start]:
				right -= 1
			else:
				self._array[left], self._array[right] = \
				self._array[right], self._array[left]
		self._array[start], self._array[right] = \
		self._array[right], self._array[start]
		self._sorter(istart,istart+1,right-1)
		self._sorter(right+1,right+2,iright)

if __name__ == '__main__':
	for l in range(20):
		arr = [_ for _ in range(l,-4,-1)]
		k = QuickSort(arr)
		print k.sort()