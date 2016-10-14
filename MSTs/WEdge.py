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