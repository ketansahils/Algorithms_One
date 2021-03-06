class MergeSortBottomUp(object):
	def __init__(self,array):
		self._array = array
		self._N = len(array)
		self._aux = [None]*self._N

	def __merge(self,aux,start,mid,end):
		for i in range(start,end+1):
			aux[i] = self._array[i]

		a,b,c = start,mid+1,start

		while c <= end:
			if a > mid:
				self._array[c] = aux[b]
				b += 1
			elif b > end:
				self._array[c] = aux[a]
				a += 1
			elif aux[a] < aux[b]:
				self._array[c] = aux[a]
				a += 1
			else:
				self._array[c] = aux[b]
				b += 1
			c += 1

	def sort(self):
		chunk = 1
		while chunk < self._N:
			i = 0
			while i < self._N - 1:
				start = i
				mid = i + chunk - 1
				end = min(start + 2*chunk - 1,self._N-1)
				self.__merge(self._aux,start,mid,end)
				i = i + 2 * chunk
			chunk = chunk + chunk
		return self._array

if __name__ == '__main__':
	for l in range(20):
		arr = [_ for _ in range(l,0,-2)]
		k = MergeSortBottomUp(arr)
		print k.sort()

# Sample Output
# []
# [1]
# [2]
# [1, 3]
# [2, 4]
# [1, 3, 5]
# [2, 4, 6]
# [1, 3, 5, 7]
# [2, 4, 6, 8]
# [1, 3, 5, 7, 9]
# [2, 4, 6, 8, 10]
# [1, 3, 5, 7, 9, 11]
# [2, 4, 6, 8, 10, 12]
# [1, 3, 5, 7, 9, 11, 13]
# [2, 4, 6, 8, 10, 12, 14]
# [1, 3, 5, 7, 9, 11, 13, 15]
# [2, 4, 6, 8, 10, 12, 14, 16]
# [1, 3, 5, 7, 9, 11, 13, 15, 17]
# [2, 4, 6, 8, 10, 12, 14, 16, 18]
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]