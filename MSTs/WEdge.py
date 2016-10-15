class WEdge(object):
	def __init__(self,v,w,weight):
		self.v = v
		self.w = w
		self.weight = weight

	def either(self):
		return self.v

	def other(self,v):
		if v == self.v:
			return self.w
		return self.v

	def compareTo(self,other):
		if self.weight > other.weight:
			return 1
		elif self.weight < other.weight:
			return -1
		return 0

	def __eq__(self,other):
		if type(other) != WEdge:
			return self.weight == other
		return self.weight == other.weight

	def __lt__(self,other):
		if type(other) != WEdge:
			return self.weight < other
		return self.weight < other.weight

	def __gt__(self,other):
		if type(other) != WEdge:
			return self.weight > other
		return self.weight > other.weight


if __name__ == '__main__':
	k = WEdge(1,2,15)
	l = WEdge(1,2,25)

	print "Should be False:", 
	print(k == l)
	print "Should be True:", 
	print(k < l)
	print "Should be False:", 
	print(k > l)
	print "Should be True:", 
	print(k <= l)
	print "Should be False:", 
	print(k >= l)

	print "Should be True:",
	print(k < 100)