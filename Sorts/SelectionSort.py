class SelectionSort(object):
	def __init__(self,array):
		self._array = array

	def sort(self):
		N = len(self._array)
		for k in range(N):
			minx = k
			for i in range(k+1,N):
				if self._array[i] < self._array[minx]:
					minx = i

			self._array[k], self._array[minx] = self._array[minx], self._array[k]
		return self._array

if __name__ == '__main__':
	arr = [3,4,5,3,3,-2,2,33,5,6,7,8,-8,55]
	k = SelectionSort(arr)
	print k.sort()


# Sample Output
# [-8, -2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 33, 55]