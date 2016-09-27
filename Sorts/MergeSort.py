class MergeSort(object):
	def __init__(self,array):
		self._array = array
		self._N = len(array)
		self._aux = [None]*self._N

	def __merge(self, aux, start, mid, end):
		for k in range(start,end+1):
			aux[k] = self._array[k]

		a,b,c = start,mid+1,start

		while c <= end:
			if a > mid:
				self._array[c] = aux[b]
				b += 1
			elif b > end:
				self._array[c] = aux[a]
				a += 1
			elif aux[a] > aux[b]:
				self._array[c] = aux[b]
				b += 1
			else:
				self._array[c] = aux[a]
				a += 1
			c += 1

	def sort(self):
		start = 0
		end = self._N - 1
		mid = start + (end - start)/2
		self.__divide(start,mid,end)
		return self._array

	def __divide(self,start,mid,end):
		if start >= end:
			return
		midf = start + (mid - start)/2
		mids = (mid+1) + (end - (mid+1))/2
		self.__divide(start,midf,mid)
		self.__divide(mid+1,mids,end)
		self.__merge(self._aux,start,mid,end)


if __name__ == '__main__':
	arr = [_ for _ in range(100,0,-2)]
	k = MergeSort(arr)
	print k.sort()


