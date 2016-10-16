class WDEdge(object):
	def __init__(self,v,w,weight):
		self.v = v
		self.w = w
		self.weight = weight

	def To(self):
		return self.w

	def From(self):
		return self.v

	def __eq__(self,other):
		if type(other) != WDEdge:
			return self.weight == other
		return self.weight == other.weight

	def __lt__(self,other):
		if type(other) != WDEdge:
			return self.weight < other
		return self.weight < other.weight

	def __gt__(self,other):
		if type(other) != WDEdge:
			return self.weight > other
		return self.weight > other.weight


if __name__ == '__main__':
	k = WDEdge(1,2,15)
	l = WDEdge(2,4,25)

	print "False:", 
	print(k == l)
	print "True:", 
	print(k < l)
	print "False:", 
	print(k > l)
	print "True:", 
	print(k <= l)
	print "False:", 
	print(k >= l)

	print "True:",
	print(k < 100)