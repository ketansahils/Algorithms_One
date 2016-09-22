class SuccessorWithDelete(object):
	def __init__(self,N):
		self.__N = N
		self.__suc = [i+1 for i in range(N)]
		self.__suc[N-1] = N-1
		self.__pred = [i-1 for i in range(N)]
		self.__pred[0] = 0

	def remove(self,x):
		px = self.__pred[x]
		sx = self.__suc[x]
		if sx == x:
			self.__suc[px] = px
		elif px == x:
			self.__pred[sx] = sx
		else:
			self.__suc[px] = sx
			self.__pred[sx] = px
		self.__pred[x] = None
		self.__suc[x] = None

	def successor(self,x):
		return self.__suc[x]

	def predecessor(self,x):
		return self.__pred[x]


if __name__ == '__main__':
	k = SuccessorWithDelete(4)
	k.remove(1)
	print k.successor(2), k.predecessor(2)
	print k.successor(0), k.predecessor(0)

	k.remove(0)
	print k.successor(1), k.predecessor(1)
	print k.successor(2), k.predecessor(2)

