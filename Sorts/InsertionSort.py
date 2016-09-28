class InsertionSort(object):

	def __init__(self,arr):
		self._arr = arr
		self._N = len(arr)

	def sort(self):
		for i in range(1,self._N):
			for j in range(i,0,-1):
				if self._arr[j] < self._arr[j-1]:
					self._arr[j], self._arr[j-1] = \
					self._arr[j-1], self._arr[j]
		return self._arr



if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7,8,7,6,5,4,3,2,1]
	k = InsertionSort(arr)
	print k.sort()

# Sample Output
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]